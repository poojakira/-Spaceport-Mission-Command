import streamlit as st
from engine.physics_ml import MissionGuard
from engine.ui import render_footer

st.set_page_config(layout="wide")
render_footer() # Apply Signature

st.title("📡 Live Sensor Telemetry")

guard = MissionGuard()
df = guard.get_telemetry_stream(200)

c1, c2 = st.columns(2)
with c1:
    st.subheader("Pressure (PSI)")
    st.area_chart(df.set_index("Timestamp")["Pressure_PSI"], color="#E91E63")
with c2:
    st.subheader("Vibration (G)")
    st.line_chart(df.set_index("Timestamp")["Vibration_G"], color="#2196F3")

st.subheader("ML Risk Analysis")
st.area_chart(df.set_index("Timestamp")["ML_Risk"], color="#F44336")