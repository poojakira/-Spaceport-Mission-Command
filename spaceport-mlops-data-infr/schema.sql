/* Advanced 3NF Schema - Deterministic & Partitioned */
CREATE TABLE IF NOT EXISTS sensor_telemetry (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    pressure_psi DOUBLE PRECISION NOT NULL,
    vibration_g DOUBLE PRECISION NOT NULL,
    temperature_k DOUBLE PRECISION NOT NULL,
    ml_risk_score DOUBLE PRECISION,
    integrity_hash CHAR(64)
);

CREATE TABLE audit_ledger (
    block_height BIGSERIAL PRIMARY KEY,
    prev_hash CHAR(64) NOT NULL,
    curr_hash CHAR(64) NOT NULL,
    payload JSONB NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);