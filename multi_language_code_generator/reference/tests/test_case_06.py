import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from thermal_analyzer import ThermalAnalyzer


class TestCase06NegativeDrop(unittest.TestCase):
    def test_negative_temperature_drop_anomaly(self) -> None:
        analyzer = ThermalAnalyzer(window_size=3)
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:00:00Z", "temperature": 28.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:01:00Z", "temperature": 28.1, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:02:00Z", "temperature": 27.9, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:03:00Z", "temperature": 23.0, "status": "OK"},
        ]
        result = analyzer.analyze(readings)
        self.assertEqual(len(result["anomalies"]), 1)
        self.assertEqual(result["anomalies"][0]["deviation"], 5.0)


if __name__ == "__main__":
    unittest.main()
