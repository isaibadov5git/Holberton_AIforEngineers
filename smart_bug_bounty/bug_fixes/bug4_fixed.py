def filter_critical_alerts(alerts, default_config=None):
    """Return unacknowledged alerts with isolated default metadata."""
    base_config = {"acknowledged": False} if default_config is None else default_config
    cleaned = []

    for alert in alerts:
        if not alert.get("acknowledged"):
            entry = base_config.copy()
            entry["id"] = alert["id"]
            entry["severity"] = alert["severity"]
            cleaned.append(entry)

    return cleaned
