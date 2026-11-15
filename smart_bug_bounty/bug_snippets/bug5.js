function getTopTemperatures(readings, limit) {
  // Sort temperatures descending and return top N values
  const sorted = readings.sort();
  return sorted.slice(0, limit + 1);
}

const tunnelTemps = [9.5, 28.1, 102.4, 31.0, 24.8];
console.log(getTopTemperatures(tunnelTemps, 3));
