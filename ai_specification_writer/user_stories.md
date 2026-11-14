# User Stories – AstemLab Urban Grid Analytics

### User Story 1
As a Municipal Transit Operator, I want to view real-time airflow velocity and temperature data from subway ventilation shafts so that I can monitor tunnel ventilation efficiency without manual inspections.
**Acceptance Criteria**:
- Dashboard updates airflow (m/s) and temperature (°C) telemetry at least once every 30 seconds.
- System displays the status (Online/Offline) of each installed thermoelectric IoT node.
- Historical data trends can be viewed over 24-hour, 7-day, and 30-day intervals.
**Priority**: MVP

### User Story 2
As a Municipal Transit Operator, I want to receive automated alerts when groundwater intrusion or abnormal thermal spikes are detected in a tunnel shaft so that maintenance teams can intervene before structural or electrical damage occurs.
**Acceptance Criteria**:
- Users can configure custom threshold values for moisture and temperature alerts per sensor node.
- System dispatches an email and dashboard notification within 60 seconds of a threshold breach.
- Alert logs record the timestamp, sensor ID, peak reading, and acknowledgment status.
**Priority**: MVP

### User Story 3
As a District Heating Provider, I want to monitor the live thermal output and Coefficient of Performance (COP) of connected heat pump units so that I can verify that recovered waste heat meets the 60°C–90°C district heating grid requirement.
**Acceptance Criteria**:
- Interface displays real-time input temperature (25°C–35°C), upgraded output temperature (60°C–90°C), and calculated COP.
- System flags any heat pump unit operating below a COP of 3.8 for more than 15 consecutive minutes.
- Daily thermal energy recovered (in MWh) is automatically aggregated per station.
**Priority**: MVP

### User Story 4
As a District Heating Provider, I want the AI control engine to automatically modulate heat pump transfer rates based on incoming tunnel airflow temperatures so that thermal energy conversion remains optimal during off-peak train hours.
**Acceptance Criteria**:
- AI controller adjusts compressor load automatically when tunnel inlet temperatures fluctuate by ±2°C or more.
- System maintains target output water temperature within ±1.5°C of the set point.
- Operators can toggle between "AI Autonomous Mode" and "Manual Override" with a single click.
**Priority**: High

### User Story 5
As a Field Maintenance Engineer, I want to view the self-powered energy harvesting voltage and capacitor charge level of each thermoelectric generator node so that I can confirm the sensors operate autonomously without grid power.
**Acceptance Criteria**:
- Each node card displays real-time voltage output (mV) from the thermoelectric generator and reserve charge percentage.
- System issues a "Low Thermal Gradient Warning" if reserve charge drops below 20%.
- Diagnostic logs show uptime percentages over the trailing 90 days.
**Priority**: High

### User Story 6
As an Urban Sustainability Planner, I want to export verified carbon emission reductions and total megawatt-hours recovered into standardized PDF and CSV reports so that I can submit accurate metrics for municipal climate audits and green funding.
**Acceptance Criteria**:
- Users can select a custom date range and click "Export Report" to download data in both CSV and PDF formats.
- Reports automatically calculate CO2 equivalent (CO2e) savings based on regional grid emission factors.
- Generated files download within 5 seconds for up to 12 months of aggregated data.
**Priority**: High

### User Story 7
As a System Administrator, I want to manage role-based access control (RBAC) for transit operators, utility engineers, and external auditors so that sensitive infrastructure controls are restricted to authorized personnel.
**Acceptance Criteria**:
- Admin can assign roles: "Admin", "Operator" (read/write controls), and "Viewer" (read-only analytics).
- Users with "Viewer" permissions cannot modify alert thresholds or heat pump control modes.
- All permission changes are recorded in an immutable security audit log.
**Priority**: Medium

### User Story 8
As a Field Maintenance Engineer, I want to register and calibrate new modular sensor nodes via a mobile-responsive web interface during tunnel installation so that new hardware integrates into the grid without disrupting train schedules.
**Acceptance Criteria**:
- Engineer can scan or enter a node's hardware ID to pair it with a specific transit station and shaft location.
- Interface runs a 30-second connection and calibration check before marking the node as "Active".
- Onboarding a single node takes less than 3 minutes from login to live telemetry display.
**Priority**: Medium

### User Story 9
As an Urban Sustainability Planner, I want to view a geospatial map overlay of all monitored transit stations color-coded by waste-heat recovery potential so that I can prioritize future retrofit expansions across the city.
**Acceptance Criteria**:
- Interactive map displays pins for every active and surveyed subway ventilation shaft.
- Clicking a station pin opens a summary popup showing average daily thermal output and current node count.
- Map supports filtering by transit line and thermal capacity tiers.
**Priority**: Medium

### User Story 10
As a District Heating Provider, I want to access a documented REST API to stream thermal telemetry directly into our existing municipal SCADA software so that operators can manage all energy assets from one central control room.
**Acceptance Criteria**:
- System provides authenticated API endpoints returning real-time node telemetry in JSON format.
- API enforces rate limiting and requires valid bearer tokens for all requests.
- Interactive API documentation (Swagger/OpenAPI) is accessible to authorized developer accounts.
**Priority**: Low
