def calculate_average_cop(readings, history=[]):
    """Calculate the average Coefficient of Performance for valid readings."""
    valid_cops = []
    for item in readings:
        if item.get("status") == "ONLINE":
            cop = item["thermal_kw"] / item["electric_kw"]
            valid_cops.append(cop)
            history.append(cop)

    avg = sum(valid_cops) / len(valid_cops)
    return round(avg, 2), history
