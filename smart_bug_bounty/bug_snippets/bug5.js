function getTopTemperatures(readings, limit) {
  if (!Array.isArray(readings) || limit <= 0) {
    return [];
  }

  // Bug 1: mutates caller array in place
  // Bug 2: default .sort() sorts numbers lexicographically as strings
  const sorted = readings.sort();

  // Bug 3: off-by-one slice returns limit + 1 items instead of limit
  return sorted.slice(0, limit + 1);
}

const tunnelTemps = [9.5, 28.1, 102.4, 31.0, 24.8, 19.2];
console.log("Top 3 temperatures:", getTopTemperatures(tunnelTemps, 3));
console.log("Original array:", tunnelTemps);

module.exports = { getTopTemperatures };
