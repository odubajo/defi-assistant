import streamlit as st
from session_manager import SessionManager
from api_client import dobby_client

def render_sidebar():
    with st.sidebar:
        st.markdown("### 💬 Conversation Session")
        
        stats = SessionManager.get_conversation_stats()
        if stats["total_messages"] > 0:
            st.markdown(f"**Total Messages:** {stats['total_messages']}")
            st.markdown(f"**Your Questions:** {stats['user_messages']}")
            
            st.markdown("**Recent Context:**")
            for msg in SessionManager.get_conversation_history()[-6:]:
                role = "🙋 You" if msg["role"] == "user" else "🤖 Dobby"
                st.markdown(f'<div class="conversation-message {"user" if role == "🙋 You" else "assistant"}-message">{role}: {msg["content"][:60]}...</div>', unsafe_allow_html=True)
        else:
            st.markdown("*No conversation yet*")

        st.markdown("---")
        if st.button("🗑️ Clear History"):
            SessionManager.clear_conversation()
            if 'search_context' in st.session_state:
                del st.session_state['search_context']
            st.rerun()

def show_back_button():
    """Displays a button to navigate back to the homepage."""
    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()