import streamlit as st

def render_footer():
    """
    Renders the fixed 'Invented by Pooja Kiran' signature 
    in the bottom-right corner of every page.
    """
    st.markdown(
        """
        <style>
        /* Hide default Streamlit footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Custom Signature Class */
        .signature-container {
            position: fixed;
            bottom: 15px; /* Moved up slightly to accommodate larger text */
            right: 25px;
            width: auto;
            background-color: transparent;
            color: #888888;
            text-align: right;
            padding: 5px;
            
            /* INCREASED FONT SIZE to 22px */
            font-size: 22px; 
            
            font-family: 'Source Sans Pro', sans-serif;
            z-index: 9999;
            pointer-events: none;
            opacity: 0.9;
        }
        .signature-container b {
            color: #E91E63;
            font-weight: 700;
        }
        </style>
        
        <div class="signature-container">
            Invented by <b>Pooja Kiran</b>
        </div>
        """,
        unsafe_allow_html=True
    )