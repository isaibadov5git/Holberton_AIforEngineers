# System Architecture - AstemLab Urban Grid Analytics MVP

## High-Level System Diagram

## Component Breakdown

### 1. Edge / Simulation Layer
- **Simulated TEG Sensor Feed**: Generates realistic time-series telemetry packets (temperature, airflow velocity, moisture index, and thermoelectric voltage) for up to 10 transit stations.

### 2. Backend Application Layer
- **Telemetry Ingestion & Validation API**: Validates incoming payloads, enforces sensor value bounds, and normalizes timestamps.
- **Thermodynamic & COP Engine**: Computes recoverable thermal energy ($Q = \dot{m} \cdot c_p \cdot \Delta T$), heat pump Coefficient of Performance (targeting COP 3.8+ for 60°C–90°C output), and CO2e offset metrics.
- **Anomaly & Alert Evaluator**: Compares incoming telemetry against configured station thresholds and generates active `AlertEvent` records upon breaches.
- **CSV Export Service**: Serializes filtered telemetry records and aggregated energy metrics into downloadable `.csv` files.

### 3. In-Memory Data Store (MVP)
- Stores active station profiles (capped at 10 stations), rolling telemetry history, and alert logs in lightweight session memory for rapid single-tenant demo execution without external database dependencies.

### 4. Frontend Presentation Layer
- **Responsive Operator Dashboard**: Built with modular UI components featuring station filtering, real-time KPI cards, an interactive target-temperature COP simulator, an active alerts banner, and a one-click CSV export trigger.
