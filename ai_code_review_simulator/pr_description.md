# Pull Request: Add Multi-Criteria Telemetry Filtering & CSV Export

## Summary
Implements multi-criteria telemetry filtering (`filter_telemetry_readings`) and CSV export serialization (`export_filtered_to_csv`) for transit shaft sensor logs, enabling operators to query readings by station name, minimum heat pump COP threshold, ambient temperature, operational status, and ISO-8601 time range.

## Changes
- Added `filter_telemetry_readings()`, `_parse_iso_timestamp()`, `export_filtered_to_csv()`, and custom `TelemetryFilterError` exception in `ai_code_review_simulator/telemetry_filter.py` (~115 LOC).
- Added 5 comprehensive unit tests covering station filtering, COP thresholds, time-window bounds, invalid parameter error handling, and CSV formatting in `ai_code_review_simulator/test_telemetry_filter.py` (~85 LOC).

## Context
- **Total Size**: ~200 LOC across implementation and test suite (~115 LOC core feature code).
- **Related Issue**: #18 — Enable filtered telemetry inspection and one-click CSV feasibility exports for transit hub operators.
- **Motivation**: Municipal transit engineers and district heating planners need to isolate high-efficiency waste heat intervals (COP ≥ 3.8) per station and export clean datasets without manual log parsing.
- **Verification**: All 5 unit tests pass via `python3 -m unittest test_telemetry_filter.py`.
