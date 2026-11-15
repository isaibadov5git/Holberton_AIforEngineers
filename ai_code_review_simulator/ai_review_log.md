# AI Code Review Log - PR: Multi-Criteria Telemetry Filtering & CSV Export

## Reviewer Personas Used
- **Security Auditor Persona**: Checked input validation, CSV formula injection risks, and exception handling.
- **Performance Engineer Persona**: Evaluated algorithmic complexity, memory allocation, and timestamp parsing overhead.
- **Maintainability & Clean Code Reviewer Persona**: Assessed cyclomatic complexity, type annotations, and edge-case test coverage.

---

### Inline Comments

- **(telemetry_filter.py, line 11)** `[Security]` `_parse_iso_timestamp()` lets `ValueError` from `datetime.fromisoformat()` propagate uncaught when malformed date strings are supplied; wrap it in a `try/except ValueError` block and raise `TelemetryFilterError` for consistent API error handling.
- **(telemetry_filter.py, line 32)** `[Security]` Add finite-number validation (`math.isfinite`) when checking `min_cop` and `min_temp_c` so `NaN` or `inf` inputs cannot bypass filter bounds.
- **(telemetry_filter.py, line 53)** `[Security]` Converting `record.get("estimated_cop")` and `record.get("ambient_temp_c")` directly via `float(...)` will raise an unhandled `ValueError` or `TypeError` if a corrupted sensor packet contains a non-numeric string; guard with a safe numeric helper.
- **(telemetry_filter.py, line 64)** `[Performance]` `_parse_iso_timestamp(str(raw_ts))` is invoked inside the inner loop for every record; if timestamps are normalized to UTC ISO-8601 strings on ingestion, direct lexicographical string comparison avoids repeated `datetime` object allocation.
- **(telemetry_filter.py, line 85)** `[Security]` `export_filtered_to_csv()` writes `station_name` directly to CSV without sanitizing leading `=`, `+`, `-`, or `@` characters, which could trigger CSV formula injection when opened in spreadsheet software.
- **(telemetry_filter.py, line 76)** `[Performance]` `export_filtered_to_csv()` builds the entire CSV payload in memory via `io.StringIO()`; for large multi-month exports, provide a generator-based streaming helper (`yield`) alongside the string return.
- **(test_telemetry_filter.py, line 58)** `[Maintainability]` Add unit test coverage for malformed ISO-8601 timestamp inputs, timezone-offset comparisons (e.g., `+04:00` vs `Z`), and empty `readings` lists.

---

### Global Feedback

- **[Maintainability] Decompose Filter Predicates**: `filter_telemetry_readings()` currently handles parameter validation, timestamp parsing, and 5 sequential filter conditions inside a single 50-line function. Extract individual record matching into a helper `_matches_criteria()` to reduce cyclomatic complexity.
- **[Maintainability] Replace Raw Dictionaries with Typed Dataclasses**: Passing untyped `Dict[str, Any]` records relies on magic string keys (`"estimated_cop"`, `"ambient_temp_c"`). Introduce a `@dataclass` or `TypedDict` schema (`TelemetryRecord`) to enable static type checking and prevent key typos.
- **[Performance] Add Pagination / Limit Support**: When querying tens of thousands of historical tunnel readings, `filter_telemetry_readings()` scans and returns the entire matching list at once. Add optional `limit` and `offset` parameters to support paginated dashboard queries.
- **[Security] Enforce Timezone-Aware Timestamp Comparisons**: Mixing naive ISO timestamps (without offset) and timezone-aware timestamps (`Z` / `+00:00`) in Python raises a `TypeError` during `rec_dt < parsed_start` comparisons. Normalize all parsed `datetime` objects to UTC (`timezone.utc`).
