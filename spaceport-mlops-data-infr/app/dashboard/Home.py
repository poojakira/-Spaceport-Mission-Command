import streamlit as st
from engine.physics_ml import MissionGuard
from engine.ui import render_footer  # Import the new UI module

st.set_page_config(layout="wide", page_title="Spaceport Command")

# Apply Signature
render_footer()

def main():
    st.title("🚀 Spaceport Mission Command")
    st.markdown("#### Deterministic Physics MLOps Architecture")
    st.divider()

    guard = MissionGuard()
    metrics = guard.get_latest_snapshot()
    
    # KPI Grid
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Mission Status", metrics['status'])
    k2.metric("ML Risk Score", metrics['risk_pct'])
    k3.metric("Chamber Pressure", f"{metrics['pressure']} PSI")
    k4.metric("Nozzle Temp", f"{metrics['temp']} K")
    
    # Global Plots
    st.subheader("Global Sensor Array (Deterministic Signal)")
    df = guard.get_telemetry_stream(100)
    
    c1, c2 = st.columns([3, 1])
    with c1:
        st.line_chart(df.set_index("Timestamp")[["Pressure_PSI", "Temperature_K"]])
    with c2:
        st.dataframe(df[["Pressure_PSI", "ML_Risk"]].tail(5), use_container_width=True)

if __name__ == "__main__":
    main()