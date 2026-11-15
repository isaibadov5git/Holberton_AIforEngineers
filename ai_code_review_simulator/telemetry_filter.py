import csv
import io
from datetime import datetime
from typing import Any, Dict, List, Optional


class TelemetryFilterError(ValueError):
    """Raised when invalid filter parameters are supplied."""


def _parse_iso_timestamp(value: str) -> datetime:
    """Parse an ISO-8601 timestamp string (supporting trailing 'Z')."""
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"
    return datetime.fromisoformat(normalized)


def filter_telemetry_readings(
    readings: List[Dict[str, Any]],
    station_name: Optional[str] = None,
    min_cop: Optional[float] = None,
    min_temp_c: Optional[float] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    only_online: bool = True,
) -> List[Dict[str, Any]]:
    """
    Filter transit shaft telemetry readings by station, COP efficiency,
    temperature threshold, operational status, and ISO-8601 time window.
    """
    if min_cop is not None and min_cop < 0:
        raise TelemetryFilterError("min_cop cannot be negative")

    parsed_start = _parse_iso_timestamp(start_time) if start_time else None
    parsed_end = _parse_iso_timestamp(end_time) if end_time else None

    if parsed_start and parsed_end and parsed_start > parsed_end:
        raise TelemetryFilterError("start_time cannot be later than end_time")

    target_station = station_name.strip().lower() if station_name else None
    filtered: List[Dict[str, Any]] = []

    for record in readings:
        if only_online and record.get("status") != "ONLINE":
            continue

        if target_station:
            rec_station = str(record.get("station_name", "")).strip().lower()
            if rec_station != target_station:
                continue

        if min_cop is not None:
            cop = record.get("estimated_cop")
            if cop is None or float(cop) < min_cop:
                continue

        if min_temp_c is not None:
            temp = record.get("ambient_temp_c")
            if temp is None or float(temp) < min_temp_c:
                continue

        if parsed_start or parsed_end:
            raw_ts = record.get("recorded_at")
            if not raw_ts:
                continue
            rec_dt = _parse_iso_timestamp(str(raw_ts))
            if parsed_start and rec_dt < parsed_start:
                continue
            if parsed_end and rec_dt > parsed_end:
                continue

        filtered.append(record)

    return filtered


def export_filtered_to_csv(readings: List[Dict[str, Any]]) -> str:
    """Serialize filtered telemetry readings into a standardized CSV string."""
    output = io.StringIO()
    fieldnames = [
        "station_name",
        "recorded_at",
        "ambient_temp_c",
        "airflow_velocity_mps",
        "estimated_cop",
        "status",
    ]
    writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    for row in readings:
        writer.writerow(row)
    return output.getvalue()
