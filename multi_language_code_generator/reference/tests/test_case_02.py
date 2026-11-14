import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from thermal_analyzer import ThermalAnalyzer


class TestCase02EmptyStream(unittest.TestCase):
    def test_empty_telemetry_stream(self) -> None:
        analyzer = ThermalAnalyzer(window_size=3)
        result = analyzer.analyze([])
        self.assertEqual(result["total_valid_readings"], 0)
        self.assertEqual(result["unique_sensors"], 0)
        self.assertIsNone(result["global_mean_temp"])
        self.assertEqual(result["anomalies"], [])


if __name__ == "__main__":
    unittest.main()
