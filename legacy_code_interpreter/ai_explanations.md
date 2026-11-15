# AI Code Explanations - Legacy Municipal SCADA & Telemetry Logger

## Section 1 – SerialPoller::read_modbus_frame()
- **Plain English**: Opens a raw RS-485 serial connection, reads a 16-byte binary packet from an underground thermal sensor, verifies the trailing 2-byte CRC checksum, and unpacks the raw bytes into floating-point temperature and airflow values.
- **Pattern**: Imperative byte-level bit-shifting loop paired with manual buffer slicing (`struct.unpack('>HHf', buf[3:11])`) and blocking `time.sleep()` retries.
- **Issues**: Uses a bare `except Exception: pass` block that silently drops corrupted packets without incrementing error counters, and hardcodes serial port `/dev/ttyS0` at `9600` baud directly inside the method.
- **Improvements**: Replace bare exception handlers with structured error logging, extract hardware port parameters into environment configuration, and adopt `pymodbus` with explicit timeout handling and unit tests using mock byte streams.

## Section 2 – ThermalCalibrator::compute_enthalpy_delta()
- **Plain English**: Calculates the net thermal energy transfer across a transit shaft heat exchanger using polynomial curve-fitting coefficients for moist air density, specific heat capacity, and inlet/outlet temperature differentials.
- **Pattern**: Deeply nested conditional branches (`if/elif/else` 5 levels deep) selecting hardcoded empirical constants based on humidity ranges and seasonal flags.
- **Issues**: Magic numbers (`1.006`, `2501.3`, `0.001293`) appear throughout the equations with zero inline documentation or units, making it impossible to distinguish physical constants from empirical sensor offsets.
- **Improvements**: Refactor nested conditionals into guard clauses and a lookup table, define named physical constants with explicit SI units in docstrings, and validate calculations against reference thermodynamic tables.

## Section 3 – TelemetryWriter::flush_batch_to_db()
- **Plain English**: Iterates over an in-memory queue of validated sensor readings and writes them into the PostgreSQL `telemetry_logs` table while updating each station's `last_seen` timestamp.
- **Pattern**: Row-by-row synchronous `INSERT` and `UPDATE` queries constructed via string concatenation (`"INSERT INTO telemetry_logs VALUES ('%s', %f)" % (...)`) inside a manual autocommit loop.
- **Issues**: Vulnerable to SQL injection on string station identifiers, causes severe N+1 database round-trip latency during peak polling intervals, and lacks transaction atomicity (partial batches remain committed if a connection drops mid-loop).
- **Improvements**: Switch to parameterized batch inserts (`psycopg2.extras.execute_values`), wrap the batch write and station status update inside a single atomic database transaction (`with conn:`), and add connection pooling.

## Section 4 – AlertDispatcher::evaluate_thresholds()
- **Plain English**: Checks incoming temperature and groundwater moisture readings against station-specific alarm limits and triggers email or SMS notifications if a sensor breaches safety thresholds.
- **Pattern**: Stateful global dictionary (`LAST_ALERT_SENT = {}`) tracking cooldown timestamps alongside synchronous `smtplib` network calls executed directly on the main polling thread.
- **Issues**: Blocking SMTP calls stall the entire sensor polling loop for up to 15 seconds whenever the mail server is slow, and global mutable state causes race conditions and lost cooldown tracking upon process restart.
- **Improvements**: Decouple alert dispatching onto an asynchronous background worker queue, persist alert cooldown states in PostgreSQL or Redis, and isolate threshold evaluation logic into pure, testable functions.
