# Codebase Overview - Legacy Municipal SCADA & Telemetry Logger

## Age
First released in 2011; last major feature update in 2017 (minor security patches through 2019).

## Size
~38,400 LOC across Python 2.7 (`~26,000 LOC`), legacy C serial drivers (`~8,200 LOC`), and raw SQL/XML configuration scripts (`~4,200 LOC`).

## Main Dependencies
- **Python 2.7.15** (End-of-Life runtime; relies on deprecated `urllib2`, `ConfigParser`, and old-style string formatting)
- **PostgreSQL 9.4** with `psycopg2==2.6.2` (lacks modern connection pooling and JSONB indexing)
- **Twisted 15.5.0** (legacy asynchronous networking engine for RS-485 / Modbus serial polling)
- **jQuery 1.11.3 & Bootstrap 3** (embedded static dashboard templates served via raw CGI scripts)

## Known Issues & Pain Points
- **No Automated Test Suite**: Zero unit or integration tests; all verification relies on manual staging scripts and live log inspection.
- **Monolithic Architecture & Tight Coupling**: Hardware polling loops, thermal calibration math, and direct SQL `INSERT` statements are mixed inside single 1,500+ line procedural modules.
- **Hardcoded Credentials & Magic Numbers**: Database connection strings, serial baud rates, and sensor alarm thresholds are scattered across source files instead of centralized environment configurations.
- **Silent Exception Swallowing**: Broad `except Exception: pass` blocks mask serial communication dropouts and corrupt sensor frames, causing silent gaps in historical telemetry logs.
- **Python 3 Incompatibility**: Heavy reliance on byte/string implicit conversions and legacy library APIs blocks migration to modern runtimes and security patches.
