# Spaceport-Mission-Command

The repository holds a Streamlit application which operates in containers and provides high performance for two functions. Its first function monitors deterministic sensor telemetry while its second function handles mission-critical risk through Physics-Informed Machine Learning.

# Technical Stack

i. Frontend: Streamlit (v1.30.0+) 

ii. Data Science: Pandas, NumPy, Scikit-learn, Matplotlib 

iii. Database: PostgreSQL (3NF Schema) 

iv. Containerization: Docker with Multi-Stage builds 

Signature UI: Custom integrated footer "Invented by Pooja Kiran".
# Repository Structure
├── app/
│   └── dashboard/
│       ├── Home.py              # Main dashboard entry point
│       ├── engine/              # Core logic & backend
│       │   ├── agent.py         # AI Agent logic
│       │   ├── ledger.py        # SHA-256 block creation
│       │   ├── physics_ml.py    # ML Pipeline & physics simulation
│       │   └── ui.py            # Custom CSS & signature rendering
│       └── pages/               # Multi-page application modules
│           ├── 1_Live_Telemetry.py
│           ├── 2_Physics_ML.py
│           ├── 3_Audit_Ledger.py
│           └── 4_Mission_Control.py
├── .env                         # Database configuration
├── Dockerfile                   # Multi-stage optimized build
├── docker-compose.yml           # Service orchestration
├── requirements.txt             # Python dependencies
└── schema.sql                   # PostgreSQL 3NF & Audit schema


# Installation & Setup

1. Prerequisites:
                   python -m venv venv
   
                   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Local Requirements Installation
   
To install the necessary dependencies locally, use the provided requirements.txt:

                                                                                 pip install -r requirements.txt

# Build and Start:

                docker-compose up --build

                docker run -p 8501:8501 spaceport-dashboard

# Key Features - Project Architecture

i. Deterministic Physics Engine: Generates high-fidelity telemetry for pressure, vibration, and temperature using mathematical models.

ii. Mission Guard (ML Kernel): A RandomForestRegressor pipeline that predicts mission risk scores.

iii. Immutable Audit Ledger: A cryptographic logging system that secures telemetry data using SHA-256 hashing.

iv. Autonomous Mission Agent: A dual-protocol AI interface that handles official commands professionally while utilizing a "Personality Matrix" for manual overrides.


# Safety & Reliability
The MissionGuard kernel features a deterministic "warmup" phase to ensure telemetry starts in a safe (Nominal) state. Risk assessments are categorized into three levels:

NOMINAL: Safe operations.

WARNING: ML Risk > 0.4.

CRITICAL: ML Risk > 0.7.


![Dashboard3](https://github.com/user-attachments/assets/ab6cdc69-7eda-4c61-8e34-6a6ca6efad4e)

