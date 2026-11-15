async function fetchActiveSensors(stationIds, apiClient) {
  const responses = await Promise.all(
    stationIds.map((id) => apiClient.getSensor(id))
  );

  return responses
    .filter((response) => response && response.status === 1 && response.temp > 25)
    .map((response) => ({
      id: response.id,
      temp: response.temp,
    }));
}

module.exports = { fetchActiveSensors };
