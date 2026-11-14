import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from thermal_analyzer import ThermalAnalyzer


class TestCase05MultiSensor(unittest.TestCase):
    def test_multi_sensor_interleaved_stream(self) -> None:
        analyzer = ThermalAnalyzer(window_size=2)
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:00:00Z", "temperature": 20.0, "status": "OK"},
            {"sensor_id": "S2", "timestamp": "2026-11-14T10:00:05Z", "temperature": 30.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:01:00Z", "temperature": 20.2, "status": "OK"},
            {"sensor_id": "S2", "timestamp": "2026-11-14T10:01:05Z", "temperature": 30.1, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:02:00Z", "temperature": 25.0, "status": "OK"},
            {"sensor_id": "S2", "timestamp": "2026-11-14T10:02:05Z", "temperature": 30.2, "status": "OK"},
        ]
        result = analyzer.analyze(readings)
        self.assertEqual(result["unique_sensors"], 2)
        self.assertEqual(len(result["anomalies"]), 1)
        self.assertEqual(result["anomalies"][0]["sensor_id"], "S1")


if __name__ == "__main__":
    unittest.main()
