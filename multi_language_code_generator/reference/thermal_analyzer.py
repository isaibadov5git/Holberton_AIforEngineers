import math
from collections import defaultdict
from typing import Any, Dict, List, Optional


class ThermalAnalyzer:
    """Sliding-window thermal anomaly detector and telemetry aggregator."""

    def __init__(self, window_size: int = 3) -> None:
        if window_size < 2:
            raise ValueError("window_size must be at least 2")
        self.window_size = window_size

    def _is_valid_reading(self, reading: Dict[str, Any]) -> bool:
        """Check whether a telemetry record has status 'OK' and a finite numeric temperature."""
        if reading.get("status") != "OK":
            return False
        temp = reading.get("temperature")
        if temp is None or isinstance(temp, bool) or not isinstance(temp, (int, float)):
            return False
        return math.isfinite(temp)

    def _compute_stats(self, window: List[float]) -> tuple[float, float]:
        """Return (mean, sample_std_dev) for a list of temperature values."""
        n = len(window)
        mean = sum(window) / n
        if n < 2:
            return mean, 0.0
        variance = sum((x - mean) ** 2 for x in window) / (n - 1)
        return mean, math.sqrt(variance)

    def analyze(self, readings: List[Dict[str, Any]], window_size: Optional[int] = None) -> Dict[str, Any]:
        """
        Process chronologically ordered sensor readings, compute global statistics,
        and detect thermal anomalies using a sliding window per sensor_id.
        """
        w = window_size if window_size is not None else self.window_size
        if w < 2:
            raise ValueError("window_size must be at least 2")

        sensor_buffers: Dict[str, List[float]] = defaultdict(list)
        all_valid_temps: List[float] = []
        anomalies: List[Dict[str, Any]] = []

        for reading in readings:
            if not self._is_valid_reading(reading):
                continue

            sensor_id = str(reading["sensor_id"])
            timestamp = str(reading["timestamp"])
            temp = float(reading["temperature"])

            all_valid_temps.append(temp)
            history = sensor_buffers[sensor_id]

            if len(history) >= w:
                window = history[-w:]
                mean, std_dev = self._compute_stats(window)
                diff = abs(temp - mean)

                if diff > (2.0 * std_dev) and diff >= 1.5:
                    anomalies.append({
                        "sensor_id": sensor_id,
                        "timestamp": timestamp,
                        "temperature": temp,
                        "baseline_mean": round(mean, 2),
                        "deviation": round(diff, 2),
                    })

            history.append(temp)

        total_valid = len(all_valid_temps)
        global_mean = round(sum(all_valid_temps) / total_valid, 2) if total_valid > 0 else None

        return {
            "total_valid_readings": total_valid,
            "unique_sensors": len(sensor_buffers),
            "global_mean_temp": global_mean,
            "anomalies": anomalies,
        }
