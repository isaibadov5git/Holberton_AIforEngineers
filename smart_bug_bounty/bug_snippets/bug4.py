def filter_critical_alerts(alerts, default_config={"acknowledged": False}):
    """Remove acknowledged alerts and attach default metadata."""
    cleaned = []

    for alert in alerts:
        # Bug 1: mutating list while iterating skips the next element
        if alert.get("acknowledged"):
            alerts.remove(alert)
        else:
            # Bug 2: shallow reference reuse overwrites prior entries
            entry = default_config
            entry["id"] = alert["id"]
            entry["severity"] = alert["severity"]
            cleaned.append(entry)

    return cleaned
