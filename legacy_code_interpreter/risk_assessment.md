# Risk Assessment - Legacy Municipal SCADA & Telemetry Logger

| Risk | Severity | Notes |
| :--- | :--- | :--- |
| **SQL Injection Vulnerabilities** | High | Raw string interpolation (`%s`) used to construct `INSERT` and `UPDATE` queries in `TelemetryWriter::flush_batch_to_db()`. |
| **Hardcoded Database & SMTP Credentials** | High | Plaintext PostgreSQL passwords and mail server credentials stored directly in source files (`scada_config.py`). |
| **End-of-Life Python 2.7 & Dependency Usage** | High | Runs on unsupported Python 2.7.15 and Twisted 15.5.0 with unpatched security vulnerabilities and incompatible libraries. |
| **Silent Exception Swallowing** | High | Bare `except Exception: pass` blocks in `SerialPoller` hide serial hardware dropouts and drop critical thermal alarm packets without notice. |
| **Zero Automated Test Coverage** | Medium | No unit or integration tests exist; refactoring thermodynamic math or database logic carries a high risk of silent regressions. |
| **Tight Coupling & Monolithic Modules** | Medium | Hardware polling, enthalpy equations, and SQL persistence are mixed inside 1,500+ line files, making isolated updates difficult. |
| **Blocking Synchronous Alert Dispatching** | Medium | Main polling loop stalls for up to 15 seconds during slow `smtplib` network calls, delaying real-time sensor ingestion. |
| **Unstructured & Missing Diagnostic Logging** | Low | Relies on `print` statements to stdout rather than rotating structured logs, complicating post-incident root-cause analysis. |
