function getTopTemperatures(readings, limit) {
  if (!Array.isArray(readings) || limit <= 0) {
    return [];
  }

  // Clone array before sorting numerically in descending order
  const sorted = [...readings].sort((a, b) => b - a);

  // Slice strictly to limit items
  return sorted.slice(0, limit);
}

const tunnelTemps = [9.5, 28.1, 102.4, 31.0, 24.8, 19.2];
console.log("Top 3 temperatures:", getTopTemperatures(tunnelTemps, 3));
console.log("Original array preserved:", tunnelTemps);

module.exports = { getTopTemperatures };
