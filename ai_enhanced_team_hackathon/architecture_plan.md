# High-Level Architecture Plan - District Thermal Load & Waste-Heat Site Screener

## System Architecture Diagram

## Architectural Layers & Responsibilities

### 1. Client / Presentation Layer
- **Technology Stack**: Responsive HTML/CSS/JavaScript (or React + Tailwind CSS) single-page interface.
- **Responsibilities**:
  - Renders the candidate site submission form with client-side numeric range checks.
  - Displays a sortable, filterable comparison table of screened hubs with viability badges (`HIGH`, `MODERATE`, `LOW`).
  - Provides one-click preset loading for demo stations and triggers client-side `.csv` file downloads.

### 2. Application & API Gateway Layer
- **Technology Stack**: Python (FastAPI / Flask) REST backend.
- **Core Modules**:
  - **Input Validator & Sample Preset Loader**: Enforces physical constraints on exhaust temperature, airflow rate, and target supply temperature; serves pre-built municipal transit hub presets.
  - **Deterministic Thermodynamic Engine**: Computes exact thermal recovery potential ($Q = \rho \cdot \dot{V} \cdot c_p \cdot \Delta T$), practical heat pump COP using a 0.50 Lorenz/Carnot efficiency factor, annual MWh yield, and CO₂e savings before invoking the AI layer so numerical outputs remain 100% deterministic.
  - **AI Feasibility Prompt Engine**: Sends validated site metrics and deterministic thermodynamic results to an LLM API using a structured JSON system prompt to generate equipment recommendations, viability tiers, and site-specific engineering risk notes (with graceful fallback templates if the external LLM endpoint is offline).
  - **CSV Report Serializer**: Flattens `CandidateSite`, `ThermodynamicEvaluation`, and `AIFeasibilityReport` records into RFC-4180 compliant CSV rows.

### 3. Persistence / Session Store
- **Technology Stack**: Lightweight SQLite / in-memory JSON store for rapid hackathon deployment.
- **Responsibilities**: Stores active `ScreeningSession` records alongside linked `CandidateSite`, `ThermodynamicEvaluation`, and `AIFeasibilityReport` entities for instant sorting, filtering, and export during live demos.

## Key Engineering Trade-offs & Security Guardrails
- **Deterministic Math First, AI Second**: Thermodynamic equations are calculated in pure Python rather than delegated to an LLM to eliminate arithmetic hallucinations while leveraging the LLM for qualitative engineering synthesis.
- **Input Sanitization & CSV Escaping**: All text fields (`site_name`) are sanitized against leading formula characters (`=`, `+`, `-`, `@`) prior to CSV export.
