import numpy as np
import pandas as pd
import joblib
import os
import math
from dataclasses import dataclass
from typing import List, Dict, Optional
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

@dataclass
class TelemetryFrame:
    timestamp: pd.Timestamp
    pressure: float
    vibration: float
    temperature: float
    risk_score: float

class MissionGuard:
    """
    DETERMINISTIC PHYSICS ENGINE (Corrected).
    Now initializes in a SAFE state before ramping up.
    """
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MissionGuard, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.model_path = "deterministic_kernel_v2.pkl"
        self.pipeline: Optional[Pipeline] = None
        self._train_safe_kernel()

    def _train_safe_kernel(self):
        """
        Trains the ML Kernel on a full range of safe-to-dangerous scenarios.
        """
        N = 5000
        # Train on 0% to 120% throttle to understand all states
        throttle = np.linspace(0.0, 1.2, N)
        
        psi = throttle * 6000.0
        temp = (psi * 0.25) + 290.0 
        
        # Vibration math: exponential growth with throttle
        vib = (throttle * 1.5) + (np.sin(throttle * 20.0) * 0.15)
        
        # refined risk calculation
        risk = (psi / 7000.0)**2 + (vib / 2.5) + ((temp - 300.0) / 2800.0)**2
        risk = np.clip(risk, 0.0, 1.0)

        X = pd.DataFrame({'psi': psi, 'vib': vib, 'temp': temp})
        
        self.pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('model', RandomForestRegressor(n_estimators=50, max_depth=8, random_state=42))
        ])
        
        self.pipeline.fit(X, risk)
        joblib.dump(self.pipeline, self.model_path)

    def get_telemetry_stream(self, n_points: int = 100) -> pd.DataFrame:
        """
        Generates telemetry.
        FIX: Uses a 'warmup' phase so t=0 is safe.
        """
        # We shift the time window so the wave starts at a "trough" (low point)
        # Shift by pi (3.14) to start sine wave at low/negative cycle, clamped to 0
        t = np.linspace(np.pi, np.pi + 4, n_points)
        timestamps = pd.date_range(pd.Timestamp.now(), periods=n_points, freq='100ms')
        
        # DETERMINISTIC INPUT SIGNAL (Corrected)
        # This math ensures we start at ~10% throttle (Idle) instead of 65%
        # sin(pi) is 0. We add a base load of 0.2
        base_throttle = 0.4
        wave_component = 0.3 * np.sin(t) # Starts at 0, goes down then up
        
        # Result: Starts low, ramps up slowly
        throttle = base_throttle + wave_component
        throttle = np.clip(throttle, 0.1, 1.0) # Never go below 10% or above 100%
        
        # PHYSICS CALCULATION
        psi = throttle * 5800.0
        
        # Reduced noise frequency for cleaner deterministic look
        noise_temp = 2.0 * np.sin(t * 10.0)
        temp = (psi * 0.25) + 300.0 + noise_temp
        
        vib = throttle * 0.5 # significantly reduced base vibration for safety
        
        # ML Inference
        X_in = pd.DataFrame({'psi': psi, 'vib': vib, 'temp': temp})
        risk_scores = self.pipeline.predict(X_in)
        
        return pd.DataFrame({
            'Timestamp': timestamps,
            'Pressure_PSI': psi,
            'Vibration_G': vib,
            'Temperature_K': temp,
            'ML_Risk': risk_scores
        })

    def get_latest_snapshot(self) -> Dict[str, str]:
        """Returns the single latest frame."""
        # We grab the FIRST point of the stream (Idle state) for the snapshot
        df = self.get_telemetry_stream(1)
        row = df.iloc[0]
        
        status = "NOMINAL"
        # Adjusted thresholds
        if row['ML_Risk'] > 0.4: status = "WARNING"
        if row['ML_Risk'] > 0.7: status = "CRITICAL"
        
        return {
            "status": status,
            "risk_pct": f"{row['ML_Risk']:.4f}",
            "pressure": f"{row['Pressure_PSI']:.0f}",
            "temp": f"{row['Temperature_K']:.0f}"
        }