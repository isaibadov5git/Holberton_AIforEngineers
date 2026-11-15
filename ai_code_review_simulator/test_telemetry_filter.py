import unittest
from telemetry_filter import (
    TelemetryFilterError,
    export_filtered_to_csv,
    filter_telemetry_readings,
)


class TestTelemetryFilter(unittest.TestCase):
    def setUp(self) -> None:
        self.sample_readings = [
            {
                "station_name": "28 May",
                "recorded_at": "2026-11-15T08:00:00Z",
                "ambient_temp_c": 31.5,
                "airflow_velocity_mps": 4.2,
                "estimated_cop": 4.1,
                "status": "ONLINE",
            },
            {
                "station_name": "20 Yanvar",
                "recorded_at": "2026-11-15T09:00:00Z",
                "ambient_temp_c": 27.0,
                "airflow_velocity_mps": 3.5,
                "estimated_cop": 3.6,
                "status": "ONLINE",
            },
            {
                "station_name": "28 May",
                "recorded_at": "2026-11-15T10:00:00Z",
                "ambient_temp_c": 33.0,
                "airflow_velocity_mps": 4.5,
                "estimated_cop": 4.3,
                "status": "OFFLINE",
            },
        ]

    def test_filter_by_station_and_online_status(self) -> None:
        results = filter_telemetry_readings(self.sample_readings, station_name="28 May")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["recorded_at"], "2026-11-15T08:00:00Z")

    def test_filter_by_min_cop(self) -> None:
        results = filter_telemetry_readings(
            self.sample_readings, min_cop=3.8, only_online=False
        )
        self.assertEqual(len(results), 2)

    def test_filter_by_time_window(self) -> None:
        results = filter_telemetry_readings(
            self.sample_readings,
            start_time="2026-11-15T08:30:00Z",
            end_time="2026-11-15T09:30:00Z",
        )
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["station_name"], "20 Yanvar")

    def test_invalid_filter_bounds_raise_error(self) -> None:
        with self.assertRaises(TelemetryFilterError):
            filter_telemetry_readings(self.sample_readings, min_cop=-1.0)
        with self.assertRaises(TelemetryFilterError):
            filter_telemetry_readings(
                self.sample_readings,
                start_time="2026-11-15T11:00:00Z",
                end_time="2026-11-15T08:00:00Z",
            )

    def test_export_filtered_to_csv(self) -> None:
        results = filter_telemetry_readings(self.sample_readings, station_name="28 May")
        csv_output = export_filtered_to_csv(results)
        lines = csv_output.strip().splitlines()
        self.assertEqual(len(lines), 2)
        self.assertIn("28 May,2026-11-15T08:00:00Z,31.5,4.2,4.1,ONLINE", lines[1])


if __name__ == "__main__":
    unittest.main()
