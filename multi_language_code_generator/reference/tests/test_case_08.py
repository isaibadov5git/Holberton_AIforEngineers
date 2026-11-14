import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from thermal_analyzer import ThermalAnalyzer


class TestCase08HighVariance(unittest.TestCase):
    def test_high_variance_suppresses_moderate_spike(self) -> None:
        analyzer = ThermalAnalyzer(window_size=3)
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:00:00Z", "temperature": 20.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:01:00Z", "temperature": 26.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:02:00Z", "temperature": 20.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T11:03:00Z", "temperature": 26.5, "status": "OK"},
        ]
        result = analyzer.analyze(readings)
        self.assertEqual(result["anomalies"], [])


if __name__ == "__main__":
    unittest.main()
