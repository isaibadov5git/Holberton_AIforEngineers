# Cross-Language Specification – IoT Thermal Anomaly & Moving-Average Detector

## Algorithm Description
Implement a sliding-window anomaly detection and telemetry aggregation algorithm (`detect_thermal_anomalies`) designed to process time-ordered sensor readings from underground transit shafts. For a given stream of sensor readings and a configurable window size $W$:
1. Group readings chronologically by `sensor_id`.
2. For each reading at index $i$ (where $i \ge W$), compute the simple moving average ($\mu$) and sample standard deviation ($\sigma$) of the preceding $W$ valid temperature readings ($[i - W, i - 1]$).
3. Flag the current reading as a **thermal anomaly** if the absolute deviation exceeds $2.0$ standard deviations ($|T_i - \mu| > 2.0 \cdot \sigma$) AND the absolute difference is at least $1.5^\circ\text{C}$ ($|T_i - \mu| \ge 1.5$).
4. Compute global summary statistics across all valid readings: total valid readings processed, unique active sensors, overall mean temperature (rounded to 2 decimal places), and a list of detected anomaly events.

## Input Format
A JSON object (or language-native equivalent structure/dictionary) containing:
- `window_size` (integer, $W \ge 2$): Number of prior readings used to establish the baseline window.
- `readings` (array of objects): Chronologically ordered telemetry records, each containing:
  - `sensor_id` (string): Unique identifier for the IoT node (e.g., `"NODE_01"`).
  - `timestamp` (string): ISO-8601 UTC timestamp (e.g., `"2026-11-14T10:00:00Z"`).
  - `temperature` (float or null): Measured temperature in degrees Celsius.
  - `status` (string): Operational state (`"OK"`, `"CALIBRATING"`, or `"ERROR"`).

## Output Format
A JSON object (or structured dictionary/map) containing:
- `total_valid_readings` (integer): Count of readings where `status == "OK"` and `temperature` is a valid finite number.
- `unique_sensors` (integer): Count of distinct `sensor_id` values with at least one valid reading.
- `global_mean_temp` (float or null): Arithmetic mean of all valid temperatures rounded to 2 decimal places (`null` if `total_valid_readings == 0`).
- `anomalies` (array of objects): List of flagged anomaly records ordered by `timestamp` ascending, each containing:
  - `sensor_id` (string)
  - `timestamp` (string)
  - `temperature` (float)
  - `baseline_mean` (float, rounded to 2 decimal places)
  - `deviation` (float, rounded to 2 decimal places)

## Edge Cases
- **Empty Readings List (`readings: []`)**: Must return `0` valid readings, `0` unique sensors, `null` global mean, and an empty `anomalies` array without throwing division-by-zero errors.
- **Insufficient Window History**: If a sensor has fewer than or equal to $W$ valid readings, no anomalies can be evaluated for that sensor, though its readings still count toward `total_valid_readings` and `global_mean_temp`.
- **Zero Variance Window ($\sigma = 0$)**: If all $W$ preceding readings have the exact same temperature (e.g., `[25.0, 25.0, 25.0]`), $\sigma = 0$. Any sudden jump $\ge 1.5^\circ\text{C}$ (e.g., `27.0`) still satisfies $|T_i - \mu| > 2.0 \cdot 0$ and $|T_i - \mu| \ge 1.5$, so it must be flagged cleanly without `NaN` or division errors.
- **Corrupted / Non-OK Readings**: Entries with `status != "OK"` or `temperature == null` must be excluded from both the sliding window buffer and global statistics.
- **Interleaved Multi-Sensor Streams**: Readings from multiple sensors interleaved in the input array must maintain completely isolated sliding windows per `sensor_id`.

## Test Cases

### Test Case 1: Standard Anomaly Detection (Single Sensor)
- **Input**: `window_size = 3`, `readings` for `"S1"` with temperatures `[24.0, 24.2, 24.1, 29.5, 24.3]` (all `"OK"`).
- **Expected Output**:
  - `total_valid_readings`: `5`
  - `unique_sensors`: `1`
  - `global_mean_temp`: `25.22`
  - `anomalies`: 1 item for reading `29.5` (`baseline_mean`: `24.1`, `deviation`: `5.4`).

### Test Case 2: Empty Telemetry Stream
- **Input**: `window_size = 3`, `readings = []`.
- **Expected Output**:
  - `total_valid_readings`: `0`
  - `unique_sensors`: `0`
  - `global_mean_temp`: `null`
  - `anomalies`: `[]`

### Test Case 3: Zero-Variance Baseline with Sudden Spike
- **Input**: `window_size = 3`, `readings` for `"S1"` with temperatures `[22.0, 22.0, 22.0, 23.6]` (all `"OK"`).
- **Expected Output**:
  - `total_valid_readings`: `4`
  - `unique_sensors`: `1`
  - `global_mean_temp`: `22.4`
  - `anomalies`: 1 item for reading `23.6` (`baseline_mean`: `22.0`, `deviation`: `1.6`).

### Test Case 4: Corrupted Readings & Insufficient Window Filtering
- **Input**: `window_size = 3`, `readings` for `"S1"`: `[25.0 ("OK"), null ("ERROR"), 25.1 ("OK"), 24.9 ("CALIBRATING"), 35.0 ("OK")]`.
- **Expected Output**:
  - `total_valid_readings`: `3` (only the three `"OK"` entries count; since $3 \le W$, no window evaluation occurs).
  - `unique_sensors`: `1`
  - `global_mean_temp`: `28.37`
  - `anomalies`: `[]`

### Test Case 5: Multi-Sensor Interleaved Stream
- **Input**: `window_size = 2`, interleaved readings for `"S1"` `[20.0, 20.2, 25.0]` and `"S2"` `[30.0, 30.1, 30.2]` (all `"OK"`).
- **Expected Output**:
  - `total_valid_readings`: `6`
  - `unique_sensors`: `2`
  - `global_mean_temp`: `25.92`
  - `anomalies`: 1 item for `"S1"` at `25.0` (`baseline_mean`: `20.1`, `deviation`: `4.9`); `"S2"` produces `0` anomalies.
