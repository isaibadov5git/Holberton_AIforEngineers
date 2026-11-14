import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from thermal_analyzer import ThermalAnalyzer


class TestCase04CorruptedFiltering(unittest.TestCase):
    def test_corrupted_and_insufficient_window(self) -> None:
        analyzer = ThermalAnalyzer(window_size=3)
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:00:00Z", "temperature": 25.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:01:00Z", "temperature": None, "status": "ERROR"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:02:00Z", "temperature": 25.1, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:03:00Z", "temperature": 24.9, "status": "CALIBRATING"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:04:00Z", "temperature": 35.0, "status": "OK"},
        ]
        result = analyzer.analyze(readings)
        self.assertEqual(result["total_valid_readings"], 3)
        self.assertEqual(result["anomalies"], [])


if __name__ == "__main__":
    unittest.main()
