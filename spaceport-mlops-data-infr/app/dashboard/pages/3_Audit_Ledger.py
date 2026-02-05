import streamlit as st
import pandas as pd
from engine.ledger import ImmutableLedger
from engine.physics_ml import MissionGuard
from engine.ui import render_footer

st.set_page_config(layout="wide")
render_footer() # Apply Signature

st.title("🔐 Immutable Audit Ledger")

guard = MissionGuard()
ledger = ImmutableLedger()
stream = guard.get_telemetry_stream(10)

chain = []
prev_hash = "00000000000000000000000000000000"

for _, row in stream.iterrows():
    block = ledger.create_block(
        asset_id="THRUSTER_A",
        action="LOG",
        payload={"psi": row['Pressure_PSI']},
        prev_hash=prev_hash
    )
    chain.append({
        "Hash": block['hash'],
        "Prev_Hash": block['content']['prev_hash_ref'],
        "Timestamp": block['timestamp']
    })
    prev_hash = block['hash']

st.dataframe(pd.DataFrame(chain), use_container_width=True)