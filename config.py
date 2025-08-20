import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="The DeFi Lens",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

CUSTOM_CSS = """
<style>
    /* CSS Custom Properties for consistent theming */
    :root {
        --primary-bg: #0A1628;
        --secondary-bg: #1E3A5F;
        --dark-bg: #0D0D0D;
        --accent-cyan: #00D4FF;
        --accent-green: #00FF88;
        --text-primary: #FFFFFF;
        --text-secondary: #00D4FF;
        --glow-cyan: 0 0 10px #00D4FF, 0 0 20px #00D4FF, 0 0 30px #00D4FF;
        --glow-green: 0 0 10px #00FF88, 0 0 20px #00FF88, 0 0 30px #00FF88;
        --border-gradient: linear-gradient(45deg, #00D4FF, #00FF88, #00D4FF);
    }

    /* Keyframe Animations */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes slideInLeft {
        0% { transform: translateX(-50px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }

    /* Main app styling */
    .stApp {
        background: linear-gradient(135deg, var(--dark-bg) 0%, var(--primary-bg) 50%, var(--secondary-bg) 100%);
        background-size: 300% 300%;
        animation: gradientShift 15s ease infinite;
        color: var(--text-primary);
    }

    /* --- STYLING FOR STREAMLIT COMPONENTS --- */
    
    /* Main chat messages */
    [data-testid="stChatMessage"] {
        padding: 1.5rem 2rem;
        border-radius: 20px;
        margin-bottom: 1.5rem;
        animation: slideInLeft 0.5s ease-out;
        backdrop-filter: blur(5px);
        border-width: 1px;
        border-style: solid;
    }

    /* User message styling */
    [data-testid="stChatMessage"]:has(div[data-testid="stChatMessageContent"][class*="user"]) {
        background: linear-gradient(135deg, rgba(30, 58, 95, 0.5), rgba(10, 22, 40, 0.5));
        margin-left: 2rem;
        border-image: linear-gradient(to right, var(--accent-cyan), transparent) 1;
        box-shadow: 0 4px 20px rgba(0, 212, 255, 0.1);
    }
    
    /* Assistant message styling */
    [data-testid="stChatMessage"]:has(div[data-testid="stChatMessageContent"][class*="assistant"]) {
        background: linear-gradient(135deg, rgba(13, 13, 13, 0.4), rgba(30, 58, 95, 0.4));
        margin-right: 2rem;
        border-image: linear-gradient(to left, var(--accent-green), transparent) 1;
        box-shadow: 0 4px 20px rgba(0, 255, 136, 0.1);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-bg), var(--secondary-bg));
        color: var(--text-primary);
        border: 2px solid var(--accent-cyan);
        border-radius: 12px;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, var(--accent-cyan), var(--accent-green));
        color: var(--dark-bg);
        transform: translateY(-3px);
        box-shadow: var(--glow-cyan);
        border-color: var(--accent-green);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--dark-bg), var(--primary-bg));
        border-right: 1px solid rgba(0, 212, 255, 0.3);
    }

    /* Text input styling */
    .stTextInput > div > div > input {
        background: var(--primary-bg);
        color: var(--text-primary);
        border: 2px solid rgba(0, 212, 255, 0.3);
        border-radius: 12px;
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--accent-cyan);
        box-shadow: var(--glow-cyan);
    }

    /* Headers */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: var(--text-primary);
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
    }

    /* --- STYLING FOR CUSTOM HTML CLASSES --- */
    
    /* Custom main header on the homepage */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        margin: -1rem -1rem 2rem -1rem;
    }

    .main-header h1 {
        text-shadow: var(--glow-cyan);
        font-size: 2.5rem;
    }

    .main-header p {
        color: var(--accent-green);
        font-size: 1.1rem;
    }

    /* Conversation preview messages in the sidebar */
    .conversation-message {
        padding: 0.6rem;
        margin: 0.3rem 0;
        border-radius: 8px;
        font-size: 0.85rem;
        background: rgba(30, 58, 95, 0.3);
    }
    .user-message {
        border-left: 3px solid var(--accent-cyan);
    }
    .assistant-message {
        border-left: 3px solid var(--accent-green);
    }

</style>
"""