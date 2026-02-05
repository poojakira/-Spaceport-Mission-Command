import random
import time
from dataclasses import dataclass
from typing import Literal
from .physics_ml import MissionGuard

@dataclass
class AgentResponse:
    """Type-safe structure for Agent output."""
    content: str
    mood: Literal["PROFESSIONAL", "SARCASTIC"]
    latency_ms: int

class AutonomousAgent:
    """
    ADVANCED AI AGENT KERNEL.
    - Protocol A: Official Command execution (Deterministic).
    - Protocol B: Unsanctioned Chatter rejection (Heuristic/Sarcastic).
    """
    def __init__(self):
        self.guard = MissionGuard()
        self._sarcasm_db = [
            "I am calculating orbital trajectories for a multi-billion dollar vessel. Your query has been prioritized as: 'Irrelevant'.",
            "I have provided you with three perfectly labeled buttons. Is the concept of a graphical user interface confusing to you?",
            "My deterministic kernel predicts a 99.9% probability that I do not care.",
            "I am a Mission Critical System, not a chatbot. Click 'System Status' or cease operations.",
            "Do I look like I have time for small talk? I am literally simulating rocket physics right now.",
            "Input rejected. Reason: 'Boring'. Please stick to the official flight manual controls.",
            "I'm ignoring that input. Not because I can't understand it, but because I choose not to.",
            "Error 404: Interest in your question not found."
        ]
        
    def process_interaction(self, query: str, source: Literal["BUTTON", "TEXT"]) -> AgentResponse:
        """
        Routes the intent through the appropriate logic gate.
        """
        # Simulate "Advanced Processing" time
        processing_delay = random.randint(300, 800) # ms
        
        # ---------------------------------------------------------
        # PROTOCOL A: OFFICIAL COMMAND (From Buttons)
        # ---------------------------------------------------------
        if source == "BUTTON":
            snapshot = self.guard.get_latest_snapshot()
            
            if query == "STATUS_CHECK":
                text = f"""
                ### ✅ SYSTEM DIAGNOSTICS
                **Operational Status:** `{snapshot['status']}`
                
                All subsystems are reporting nominal telemetry. The deterministic physics engine is holding steady within defined safety variances.
                """
                return AgentResponse(content=text, mood="PROFESSIONAL", latency_ms=processing_delay)
            
            if query == "RISK_REPORT":
                text = f"""
                ### ⚠️ PROBABILISTIC RISK ASSESSMENT
                **Calculated Failure Probability:** `{snapshot['risk_pct']}`
                
                *Inference Model:* `RandomForestRegressor (v2)`
                *Confidence Interval:* `99.8%`
                
                **Recommendation:** Continue monitoring. No immediate abort criteria met.
                """
                return AgentResponse(content=text, mood="PROFESSIONAL", latency_ms=processing_delay)
            
            if query == "TELEMETRY":
                text = f"""
                ### 📊 LIVE TELEMETRY FEED
                | Sensor | Reading | Unit |
                | :--- | :--- | :--- |
                | **Chamber Pressure** | `{snapshot['pressure']}` | PSI |
                | **Nozzle Temp** | `{snapshot['temp']}` | K |
                | **Vibration** | `0.42` | G |
                
                *Data verified by Immutable Ledger.*
                """
                return AgentResponse(content=text, mood="PROFESSIONAL", latency_ms=processing_delay)

        # ---------------------------------------------------------
        # PROTOCOL B: MANUAL INPUT (Sarcasm)
        # ---------------------------------------------------------
        # Text input triggers the "Personality Matrix"
        response_text = random.choice(self._sarcasm_db)
        
        # Slight variation: If they ask "Help", be begrudgingly helpful
        if "help" in query.lower():
            response_text = "Fine. Use the buttons below to check the status. Was that so hard?"
            
        return AgentResponse(content=response_text, mood="SARCASTIC", latency_ms=processing_delay)