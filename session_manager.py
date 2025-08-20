import streamlit as st
from typing import List, Dict

class SessionManager:    
    @staticmethod
    def initialize():
        if 'page' not in st.session_state:
            st.session_state.page = "home"
        if 'conversation_history' not in st.session_state:
            st.session_state.conversation_history = []

    @staticmethod
    def add_to_conversation(user_message: str, assistant_response: str):
        st.session_state.conversation_history.extend([
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": assistant_response}
        ])

    @staticmethod
    def get_conversation_history() -> List[Dict]:
        return st.session_state.conversation_history

    @staticmethod
    def clear_conversation():
        st.session_state.conversation_history = []
    
    @staticmethod
    def get_conversation_stats() -> Dict:
        history = st.session_state.conversation_history
        total_messages = len(history)
        user_messages = len([msg for msg in history if msg["role"] == "user"])
        return {
            "total_messages": total_messages,
            "user_messages": user_messages,
            "assistant_messages": total_messages - user_messages
        }