import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from engine.physics_ml import MissionGuard
from engine.ui import render_footer

st.set_page_config(layout="wide")
render_footer() # Apply Signature

st.title("🧠 Physics-Informed ML Kernel")

guard = MissionGuard()
c1, c2 = st.columns([1, 2])

with c1:
    st.markdown("### Digital Twin Controls")
    p = st.slider("Pressure (PSI)", 0, 7000, 3500)
    v = st.slider("Vibration (G)", 0.0, 3.0, 0.5)
    t = st.slider("Temperature (K)", 200, 1000, 450)
    
    risk = guard.pipeline.predict(pd.DataFrame({'psi':[p], 'vib':[v], 'temp':[t]}))[0]
    st.info(f"Predicted Risk: **{risk:.4f}**")

with c2:
    st.markdown("### Deterministic Decision Boundary")
    x = np.linspace(0, 7000, 100)
    batch = pd.DataFrame({'psi': x, 'vib': np.full(100, v), 'temp': np.full(100, t)})
    y = guard.pipeline.predict(batch)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x, y, color='purple', linewidth=2)
    ax.set_title(f"Risk Sensitivity (Vib={v}G)")
    ax.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig)