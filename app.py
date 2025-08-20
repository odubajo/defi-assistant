import streamlit as st
from config import set_page_config, CUSTOM_CSS
from session_manager import SessionManager
from ui.components import render_sidebar
from ui.pages import show_homepage, explain_protocol_page, news_simplifier_page, document_analyzer_page, terms_translator_page, strategy_validator_page

def main():
    set_page_config()
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    SessionManager.initialize()

    render_sidebar()

    page = st.session_state.page

    if page == "home":
        show_homepage()
    elif page == "explain":
        explain_protocol_page()
    elif page == "news":
        news_simplifier_page()
    elif page == "docs":
        document_analyzer_page()
    elif page == "terms":
        terms_translator_page()
    elif page == "strategy":
        strategy_validator_page()

if __name__ == "__main__":
    main()