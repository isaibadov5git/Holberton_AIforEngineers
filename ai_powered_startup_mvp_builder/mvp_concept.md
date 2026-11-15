# MVP Concept - AstemLab Urban Grid Analytics

## Problem Statement
Municipal transit authorities and district heating operators lack real-time visibility into low-grade waste heat trapped inside underground subway tunnels and ventilation shafts, while installing wired environmental sensors underground requires costly electrical cabling and disruptive track closures.

## Target Users
- **Municipal Transit Infrastructure Engineers**: Need zero-wiring, low-maintenance airflow and thermal telemetry inside subway ventilation shafts.
- **District Heating & Utility Planners**: Need accurate, continuous thermal yield metrics to evaluate waste-heat recovery feasibility for local heating networks.
- **Urban Sustainability & Climate Officers**: Need verifiable energy recovery and carbon-offset projections to support municipal decarbonization initiatives.

## Core Features
- **Live Shaft Telemetry Dashboard**: Displays real-time airflow velocity (m/s), ambient tunnel temperature (°C), and thermoelectric generator (TEG) power output across active transit hubs (e.g., 28 May, 20 Yanvar, Gənclik).
- **Thermal Recovery & COP Estimator**: Calculates recoverable thermal energy (kW/MWh) and projected heat pump Coefficient of Performance (COP 3.8+) for upgrading 25°C–35°C tunnel exhaust into 60°C–90°C district heating water.
- **Automated Anomaly & Threshold Alerts**: Flags sudden temperature spikes, airflow drops, or groundwater moisture intrusions on the dashboard when readings breach configurable safety limits.
- **One-Click CSV & Summary Export**: Allows engineers and planners to export filtered station telemetry and estimated CO2e savings into clean CSV files for feasibility reporting.

## Constraints
- **Simulated / Historical Telemetry Stream**: MVP uses pre-loaded and simulated sensor JSON feeds rather than live hardware RS-485/LoRaWAN field gateways.
- **Single-Tenant Demo Mode**: No role-based authentication or multi-organization user management in v1; opens directly into the operator workspace.
- **Station Cap**: Limited to monitoring up to 10 transit ventilation shafts simultaneously with in-memory session storage.
