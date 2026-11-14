# Copilot Productivity Sprint – Benchmark Coding Tasks

## Task 1 – REST API Telemetry Ingestion Endpoint (Python / FastAPI or Flask)
**Requirements**: Implement a `POST /api/v1/telemetry` endpoint that accepts incoming sensor readings from transit tunnel IoT nodes, validates the payload structure and value ranges, and returns a stored record with a generated UUID and UTC timestamp.  
**Inputs**: JSON payload containing `{ "node_id": string, "airflow_mps": float, "temp_celsius": float }`  
**Outputs**: JSON object representing the stored reading with added `"reading_id"` (UUIDv4) and `"recorded_at"` (ISO-8601 timestamp).  
**Acceptance Criteria**:  
- Returns HTTP `201 Created` with the stored JSON object when all fields are valid.  
- Returns HTTP `400 Bad Request` with a descriptive error message if `node_id` is empty, `airflow_mps` is negative, or `temp_celsius` is outside `-20.0` to `150.0`.  
- Includes at least 2 unit tests verifying both valid ingestion and validation rejection.

## Task 2 – Heat Pump Coefficient of Performance (COP) Time-Series Aggregator (Python)
**Requirements**: Write a data-processing function `analyze_cop_logs(records)` that parses a list of hourly thermal sensor dictionaries, filters out corrupted or offline readings, calculates the Coefficient of Performance ($\text{COP} = \frac{Q_{\text{out}}}{W_{\text{in}}}$) for each valid hour, and summarizes overall efficiency.  
**Inputs**: List of dictionaries: `[{"timestamp": str, "status": str, "thermal_output_kw": float, "electrical_input_kw": float}, ...]`  
**Outputs**: Summary dictionary: `{"valid_hours": int, "average_cop": float, "peak_cop": float, "below_threshold_timestamps": list[str]}` (where threshold is `3.8`).  
**Acceptance Criteria**:  
- Skips records where `status != "ONLINE"` or `electrical_input_kw <= 0` without raising a `ZeroDivisionError`.  
- Rounds `average_cop` and `peak_cop` to 2 decimal places.  
- Accurately lists all timestamps where calculated COP fell below `3.8`.

## Task 3 – Log File Anomaly Parser & Alert Formatter (JavaScript / Node.js)
**Requirements**: Implement a utility function `parseTunnelLogs(rawLogString)` that processes multi-line raw sensor log strings using regular expressions, extracts critical warnings (`[ERROR]` or `[WARN]`), deduplicates repeated consecutive alerts from the same sensor node, and formats them into a clean summary report.  
**Inputs**: Multi-line string with lines formatted as `YYYY-MM-DD HH:MM:SS [LEVEL] NODE_ID: Message`  
**Outputs**: Array of structured alert objects: `[{ timestamp, level, nodeId, message, occurrences }]`  
**Acceptance Criteria**:  
- Ignores `[INFO]` and `[DEBUG]` log lines completely.  
- Collapses consecutive identical warnings from the same `NODE_ID` into a single object with an incremented `occurrences` counter.  
- Handles empty strings or malformed lines gracefully without throwing runtime exceptions.

## Task 4 – Debounced Live Sensor Search Filter Component (JavaScript / Frontend)
**Requirements**: Create a clean, self-contained JavaScript module `createSensorFilter(nodes, delayMs)` that filters a list of station sensor nodes by station name or status while debouncing rapid user keystrokes to prevent redundant DOM re-renders.  
**Inputs**: Array of node objects `[{ id, station, line, status }]`, debounce delay in milliseconds (`int`), and search query string.  
**Outputs**: Promise or callback execution returning the filtered array of matching node objects.  
**Acceptance Criteria**:  
- Performs case-insensitive partial matching against both `station` and `line` fields.  
- Ensures the filter callback executes only once after the user stops typing for `delayMs` milliseconds.  
- Returns the full unfiltered list when the search query is empty or whitespace-only.
