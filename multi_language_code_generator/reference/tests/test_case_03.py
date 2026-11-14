import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from thermal_analyzer import ThermalAnalyzer


class TestCase03ZeroVariance(unittest.TestCase):
    def test_zero_variance_baseline_with_spike(self) -> None:
        analyzer = ThermalAnalyzer(window_size=3)
        readings = [
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:00:00Z", "temperature": 22.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:01:00Z", "temperature": 22.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:02:00Z", "temperature": 22.0, "status": "OK"},
            {"sensor_id": "S1", "timestamp": "2026-11-14T10:03:00Z", "temperature": 23.6, "status": "OK"},
        ]
        result = analyzer.analyze(readings)
        self.assertEqual(len(result["anomalies"]), 1)
        self.assertEqual(result["anomalies"][0]["deviation"], 1.6)


if __name__ == "__main__":
    unittest.main()
