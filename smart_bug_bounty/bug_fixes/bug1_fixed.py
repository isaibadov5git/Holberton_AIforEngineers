def calculate_average_cop(readings, history=None):
    """Calculate the average Coefficient of Performance for valid readings."""
    if history is None:
        history = []

    valid_cops = []
    for item in readings:
        electric_kw = item.get("electric_kw", 0)
        thermal_kw = item.get("thermal_kw", 0)
        if item.get("status") == "ONLINE" and electric_kw > 0:
            cop = thermal_kw / electric_kw
            valid_cops.append(cop)
            history.append(round(cop, 2))

    if not valid_cops:
        return 0.0, history

    avg = sum(valid_cops) / len(valid_cops)
    return round(avg, 2), history
