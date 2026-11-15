# Data Model - AstemLab Urban Grid Analytics MVP

## Entity Relationship Overview

---

## Entity 1: `TransitStation`
Represents a monitored subway station ventilation shaft (capped at 10 active stations in the MVP).

| Field Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `station_id` | `STRING (UUID)` | Primary Key, Not Null | Unique identifier for the transit ventilation shaft. |
| `station_name` | `STRING(100)` | Not Null, Unique | Human-readable hub name (e.g., `"28 May"`, `"20 Yanvar"`, `"Gənclik"`). |
| `transit_line` | `STRING(50)` | Not Null | Subway line identifier (e.g., `"Red Line"`, `"Green Line"`). |
| `shaft_cross_section_m2` | `FLOAT` | Not Null, `> 0` | Ventilation shaft cross-sectional area used to compute mass airflow rate. |
| `status` | `ENUM` | Default: `"ONLINE"` | Operational status (`"ONLINE"`, `"OFFLINE"`, `"MAINTENANCE"`). |

---

## Entity 2: `TelemetryReading`
Represents a single time-stamped environmental and energy-harvesting packet collected from a station's self-powered TEG node.

| Field Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `reading_id` | `STRING (UUID)` | Primary Key, Not Null | Unique identifier for the telemetry record. |
| `station_id` | `STRING (UUID)` | Foreign Key (`TransitStation`), Not Null | Reference to the originating transit shaft. |
| `recorded_at` | `DATETIME (ISO-8601)` | Not Null | UTC timestamp when the sensor reading was captured. |
| `ambient_temp_c` | `FLOAT` | Not Null, `-20.0` to `100.0` | Measured tunnel exhaust air temperature in degrees Celsius. |
| `airflow_velocity_mps` | `FLOAT` | Not Null, `>= 0.0` | Measured tunnel airflow speed in meters per second. |
| `teg_voltage_mv` | `FLOAT` | Not Null, `>= 0.0` | Harvested thermoelectric generator output voltage in millivolts. |
| `recoverable_thermal_kw` | `FLOAT` | Not Null, `>= 0.0` | Calculated recoverable waste heat potential in kilowatts. |
| `estimated_cop` | `FLOAT` | Not Null, `>= 1.0` | Projected heat pump Coefficient of Performance at target grid output. |

---

## Entity 3: `AlertEvent`
Represents an automated anomaly or threshold breach detected on a specific transit shaft.

| Field Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `alert_id` | `STRING (UUID)` | Primary Key, Not Null | Unique identifier for the alert event. |
| `station_id` | `STRING (UUID)` | Foreign Key (`TransitStation`), Not Null | Reference to the affected transit station. |
| `reading_id` | `STRING (UUID)` | Foreign Key (`TelemetryReading`), Not Null | Reference to the specific reading that triggered the alert. |
| `severity` | `ENUM` | Not Null | Alert severity level (`"LOW"`, `"MEDIUM"`, `"HIGH"`). |
| `metric_type` | `STRING(50)` | Not Null | Metric that breached threshold (`"TEMPERATURE"`, `"AIRFLOW"`, `"TEG_VOLTAGE"`). |
| `message` | `TEXT` | Not Null | Human-readable summary of the anomaly. |
| `acknowledged` | `BOOLEAN` | Default: `FALSE` | Indicates whether an operator has acknowledged the alert. |
| `created_at` | `DATETIME (ISO-8601)` | Not Null | UTC timestamp when the alert was generated. |

---

## Entity 4: `AlertThresholdConfig`
Stores configurable safety and efficiency thresholds per station.

| Field Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `config_id` | `STRING (UUID)` | Primary Key, Not Null | Unique identifier for the threshold configuration. |
| `station_id` | `STRING (UUID)` | Foreign Key (`TransitStation`), Unique | Station associated with these threshold limits. |
| `max_temp_c` | `FLOAT` | Default: `38.0` | Upper temperature limit (°C) before triggering a thermal spike alert. |
| `min_airflow_mps` | `FLOAT` | Default: `1.5` | Minimum acceptable airflow velocity (m/s) before flagging a blockage. |
| `min_teg_voltage_mv` | `FLOAT` | Default: `250.0` | Minimum TEG output voltage (mV) required for autonomous node operation. |
