import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from thermal_analyzer import ThermalAnalyzer


class TestCase10InvalidWindowSize(unittest.TestCase):
    def test_invalid_window_size_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            ThermalAnalyzer(window_size=1)
        analyzer = ThermalAnalyzer(window_size=3)
        with self.assertRaises(ValueError):
            analyzer.analyze([], window_size=0)


if __name__ == "__main__":
    unittest.main()
