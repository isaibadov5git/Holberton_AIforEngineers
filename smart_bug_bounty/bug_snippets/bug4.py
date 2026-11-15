def filter_critical_alerts(alerts, default_config={"acknowledged": False}):
    """Remove acknowledged alerts and attach default metadata."""
    cleaned = []
    for alert in alerts:
        if alert["acknowledged"]:
            alerts.remove(alert)
        else:
            entry = default_config
            entry["id"] = alert["id"]
            entry["severity"] = alert["severity"]
            cleaned.append(entry)
    return cleaned
