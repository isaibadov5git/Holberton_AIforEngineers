import os
import sys
import unittest

# Ensure parent /reference directory is on sys.path for direct test execution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from thermal_analyzer import ThermalAnalyzer


class TestThermalAnalyzer(unittest.TestCase):
    def setUp(self) -> None:
        self.analyzer = ThermalAnalyzer(window_size=3)

    def test_01_standard_single_sensor_anomaly(self) -> None:
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:00:00Z", "temperature": 24.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:01:00Z", "temperature": 24.2, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:02:00Z", "temperature": 24.1, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:03:00Z", "temperature": 29.5, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:04:00Z", "temperature": 24.3, "status": "OK"},
        ]
        result = self.analyzer.analyze(readings)
        self.assertEqual(result["total_valid_readings"], 5)
        self.assertEqual(result["unique_sensors"], 1)
        self.assertEqual(result["global_mean_temp"], 25.22)
        self.assertEqual(len(result["anomalies"]), 1)
        self.assertEqual(result["anomalies"][0]["temperature"], 29.5)
        self.assertEqual(result["anomalies"][0]["baseline_mean"], 24.1)
        self.assertEqual(result["anomalies"][0]["deviation"], 5.4)

    def test_02_empty_telemetry_stream(self) -> None:
        result = self.analyzer.analyze([])
        self.assertEqual(result["total_valid_readings"], 0)
        self.assertEqual(result["unique_sensors"], 0)
        self.assertIsNone(result["global_mean_temp"])
        self.assertEqual(result["anomalies"], [])

    def test_03_zero_variance_baseline_with_sudden_spike(self) -> None:
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:00:00Z", "temperature": 22.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:01:00Z", "temperature": 22.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:02:00Z", "temperature": 22.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:03:00Z", "temperature": 23.6, "status": "OK"},
        ]
        result = self.analyzer.analyze(readings)
        self.assertEqual(result["total_valid_readings"], 4)
        self.assertEqual(result["global_mean_temp"], 22.4)
        self.assertEqual(len(result["anomalies"]), 1)
        self.assertEqual(result["anomalies"][0]["baseline_mean"], 22.0)
        self.assertEqual(result["anomalies"][0]["deviation"], 1.6)

    def test_04_corrupted_readings_and_insufficient_window(self) -> None:
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:00:00Z", "temperature": 25.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:01:00Z", "temperature": None, "status": "ERROR"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:02:00Z", "temperature": 25.1, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:03:00Z", "temperature": 24.9, "status": "CALIBRATING"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:04:00Z", "temperature": 35.0, "status": "OK"},
        ]
        result = self.analyzer.analyze(readings)
        self.assertEqual(result["total_valid_readings"], 3)
        self.assertEqual(result["unique_sensors"], 1)
        self.assertEqual(result["global_mean_temp"], 28.37)
        self.assertEqual(result["anomalies"], [])

    def test_05_multi_sensor_interleaved_stream(self) -> None:
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:00:00Z", "temperature": 20.0, "status": "OK"},
            {"sensor_id": "S2", "timestamp": "2026-11-14T10:00:05Z", "temperature": 30.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:01:00Z", "temperature": 20.2, "status": "OK"},
            {"sensor_id": "S2", "timestamp": "2026-11-14T10:01:05Z", "temperature": 30.1, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:02:00Z", "temperature": 25.0, "status": "OK"},
            {"sensor_id": "S2", "timestamp": "2026-11-14T10:02:05Z", "temperature": 30.2, "status": "OK"},
        ]
        result = self.analyzer.analyze(readings, window_size=2)
        self.assertEqual(result["total_valid_readings"], 6)
        self.assertEqual(result["unique_sensors"], 2)
        self.assertEqual(result["global_mean_temp"], 25.92)
        self.assertEqual(len(result["anomalies"]), 1)
        self.assertEqual(result["anomalies"][0]["sensor_id"], "S1")
        self.assertEqual(result["anomalies"][0]["deviation"], 4.9)

    def test_06_negative_temperature_drop_anomaly(self) -> None:
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:00:00Z", "temperature": 28.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:01:00Z", "temperature": 28.1, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:02:00Z", "temperature": 27.9, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:03:00Z", "temperature": 23.0, "status": "OK"},
        ]
        result = self.analyzer.analyze(readings)
        self.assertEqual(len(result["anomalies"]), 1)
        self.assertEqual(result["anomalies"][0]["temperature"], 23.0)
        self.assertEqual(result["anomalies"][0]["deviation"], 5.0)

    def test_07_sub_threshold_jump_not_flagged(self) -> None:
        # Zero variance baseline at 20.0, jump to 21.4 (< 1.5°C minimum difference)
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:00:00Z", "temperature": 20.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:01:00Z", "temperature": 20.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:02:00Z", "temperature": 20.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:03:00Z", "temperature": 21.4, "status": "OK"},
        ]
        result = self.analyzer.analyze(readings)
        self.assertEqual(result["anomalies"], [])

    def test_08_high_variance_window_suppresses_moderate_spike(self) -> None:
        # Window [20.0, 26.0, 20.0] -> mean=22.0, std_dev=3.464 -> 2*std_dev=6.93
        # Reading 26.5 has diff=4.5 (< 6.93), so it should NOT be flagged
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:00:00Z", "temperature": 20.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:01:00Z", "temperature": 26.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:02:00Z", "temperature": 20.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:03:00Z", "temperature": 26.5, "status": "OK"},
        ]
        result = self.analyzer.analyze(readings)
        self.assertEqual(result["anomalies"], [])

    def test_09_all_corrupted_readings(self) -> None:
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T12:00:00Z", "temperature": 25.0, "status": "ERROR"},
            {"sensor_id": "S2", "timestamp": "2026-11-14T12:01:00Z", "temperature": float("nan"), "status": "OK"},
            {"sensor_id": "S3", "timestamp": "2026-11-14T12:02:00Z", "temperature": float("inf"), "status": "OK"},
        ]
        result = self.analyzer.analyze(readings)
        self.assertEqual(result["total_valid_readings"], 0)
        self.assertEqual(result["unique_sensors"], 0)
        self.assertIsNone(result["global_mean_temp"])

    def test_10_invalid_window_size_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            ThermalAnalyzer(window_size=1)
        with self.assertRaises(ValueError):
            self.analyzer.analyze([], window_size=0)


if __name__ == "__main__":
    unittest.main()
