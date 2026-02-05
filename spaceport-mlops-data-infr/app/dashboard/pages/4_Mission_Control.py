import streamlit as st
import time
from engine.agent import AutonomousAgent
from engine.ui import render_footer

# 1. Page Configuration
st.set_page_config(page_title="Mission Agent", page_icon="🤖")
render_footer()

st.title("🤖 Autonomous Mission Agent")
st.caption("v3.1.0 | Neural Link Established")

# 2. Session State Initialization
if "agent" not in st.session_state:
    st.session_state.agent = AutonomousAgent()

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant", 
        "content": "👋 **Greetings, Operator.**\n\nI am the Spaceport AI. My protocols are restricted to **Official Mission Business** only.\n\nPlease select a command below. Do not waste my cycles with idle chatter."
    }]

# 3. Helper: Chat Appender
def add_message(role, content):
    st.session_state.messages.append({"role": role, "content": content})

# 4. Interaction Handler (The Brain)
def handle_interaction(prompt, source):
    # Add User Message
    if source == "TEXT":
        add_message("user", prompt)
    else:
        add_message("user", f"🛠️ EXECUTE PROTOCOL: **{prompt}**")

    # Simulate AI "Thinking"
    with st.spinner("Processing Logic Gate..."):
        response_obj = st.session_state.agent.process_interaction(prompt, source)
        time.sleep(response_obj.latency_ms / 1000) # Simulate latency for realism
    
    # Format and Add AI Message
    if response_obj.mood == "SARCASTIC":
        # Sarcastic messages get a specific styling
        formatted_content = f"😒 {response_obj.content}"
    else:
        formatted_content = response_obj.content
        
    add_message("assistant", formatted_content)

# 5. Display Chat History (The View)
for msg in st.session_state.messages:
    # Set avatars based on role
    avatar = "🧑‍🚀" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# 6. INPUT AREA: Separation of Concerns

# --- ZONE A: Official Controls ---
st.markdown("---")
st.subheader("🎮 Mission Controls")
c1, c2, c3 = st.columns(3)

if c1.button("✅ System Status", use_container_width=True):
    handle_interaction("STATUS_CHECK", "BUTTON")
    st.rerun()

if c2.button("⚠️ Risk Analysis", use_container_width=True):
    handle_interaction("RISK_REPORT", "BUTTON")
    st.rerun()

if c3.button("📊 Telemetry Data", use_container_width=True):
    handle_interaction("TELEMETRY", "BUTTON")
    st.rerun()

# --- ZONE B: Manual Override (Sarcasm Trigger) ---
if prompt := st.chat_input("Manual Override (Not Recommended)..."):
    handle_interaction(prompt, "TEXT")
    st.rerun()