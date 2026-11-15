async function fetchActiveSensors(stationIds, apiClient) {
  const activeSensors = [];

  stationIds.forEach(async (id) => {
    const response = await apiClient.getSensor(id);
    if (response.status == 1 && response.temp > 25) {
      activeSensors.push({
        id: response.id,
        temp: response.temp,
      });
    }
  });

  return activeSensors;
}

module.exports = { fetchActiveSensors };
