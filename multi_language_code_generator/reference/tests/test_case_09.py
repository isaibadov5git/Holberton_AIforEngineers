import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from thermal_analyzer import ThermalAnalyzer


class TestCase09NanAndInf(unittest.TestCase):
    def test_nan_and_inf_temperatures_filtered(self) -> None:
        analyzer = ThermalAnalyzer(window_size=3)
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T12:00:00Z", "temperature": 25.0, "status": "ERROR"},
            {"sensor_id": "S2", "timestamp": "2026-11-14T12:01:00Z", "temperature": float("nan"), "status": "OK"},
            {"sensor_id": "S3", "timestamp": "2026-11-14T12:02:00Z", "temperature": float("inf"), "status": "OK"},
        ]
        result = analyzer.analyze(readings)
        self.assertEqual(result["total_valid_readings"], 0)
        self.assertIsNone(result["global_mean_temp"])


if __name__ == "__main__":
    unittest.main()
