import streamlit as st
import io
import PyPDF2
import docx2txt
from session_manager import SessionManager
from api_client import dobby_client
from ui.components import show_back_button

def render_continuous_chat():
    st.markdown("---")
    st.markdown("### Conversation")

    history = SessionManager.get_conversation_history()
    if not history:
        st.info("Your conversation with Dobby will appear here.")
    else:
        for message in history:
            role = "🙋 You" if message["role"] == "user" else "🤖 Dobby"
            st.markdown(f'**{role}:** {message["content"]}')

    user_input = st.chat_input("Ask a follow-up question...")

    if user_input:
        with st.spinner("Dobby is thinking..."):
            perform_search = False
            final_prompt = user_input

            if 'search_context' in st.session_state and st.session_state.search_context.get("type") == "document":
                perform_search = True
                doc_name = st.session_state.search_context.get("name", "the previously analyzed document")
                final_prompt = f"In the context of the document '{doc_name}' that we just discussed, the user has a follow-up question: '{user_input}'"

            response = dobby_client.chat(
                final_prompt, 
                conversation_history=history,
                perform_search=perform_search
            )

            SessionManager.add_to_conversation(user_input, response)
            st.rerun()

def extract_text_from_file(uploaded_file):
    try:
        if uploaded_file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.getvalue()))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            return docx2txt.process(io.BytesIO(uploaded_file.getvalue()))
        else: 
            return str(uploaded_file.read(), "utf-8")
    except Exception as e:
        st.error(f"Error reading or processing file: {e}")
        return None

def show_homepage():
    st.markdown('<div class="main-header"><h1>🎯 Web3 Navigator</h1><p>Powered by Dobby AI</p></div>', unsafe_allow_html=True)

    st.markdown("### Choose what you need help with:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📚 Explain DeFi Protocol", key="explain_btn", help="Learn how any DeFi protocol works"):
            st.session_state.page = "explain"
            st.rerun()

        if st.button("📄 Analyze Documents", key="docs_btn", help="Upload and analyze whitepapers, docs, PDFs"):
            st.session_state.page = "docs"
            st.rerun()

        if st.button("✅ Validate DeFi Strategy", key="strategy_btn", help="Get feedback on your DeFi plans"):
            st.session_state.page = "strategy"
            st.rerun()

    with col2:
        if st.button("📰 Simplify Crypto News", key="news_btn", help="Break down complex articles"):
            st.session_state.page = "news"
            st.rerun()

        if st.button("📖 Translate Crypto Terms", key="terms_btn", help="Explain DeFi terminology"):
            st.session_state.page = "terms"
            st.rerun()

    st.markdown("---")
    st.markdown("""
    **About DeFi Clarity Assistant:**
    This tool leverages Dobby AI's crypto-native intelligence to help you understand DeFi better.
    Dobby brings a decentralization-focused perspective to every explanation and analysis.
    - 🎯 **Focused**: Each tool handles one specific task well
    - 🧠 **Smart**: Powered by Dobby's crypto expertise
    - 📄 **Document Analysis**: Upload PDFs, DOCX, and text files for explanation
    - 💬 **Conversational**: Maintains context across your questions on each page
    """)

def explain_protocol_page():
    show_back_button()

    st.markdown("# 📚 DeFi Protocol Explainer")
    st.markdown("Get Dobby's take on how any DeFi protocol works")

    protocol_name = st.text_input(
        "Enter protocol name:",
        placeholder="e.g., Uniswap, AAVE, Curve, Compound...",
        help="Type the name of any DeFi protocol you want to understand"
    )

    if st.button("Explain Protocol", type="primary"):
        if protocol_name:
            with st.spinner(f"Dobby is searching the web and analyzing {protocol_name}..."):
                prompt = f"""You're Dobby, an AI with strong convictions about decentralization and crypto freedom.

Explain {protocol_name} to someone who's new to DeFi. Cover its purpose, benefits, risks, and importance for decentralization.

Use your crypto-native personality and keep it engaging but informative."""

                SessionManager.clear_conversation()
                if 'search_context' in st.session_state: del st.session_state['search_context'] # Clear context
                
                response = dobby_client.chat(prompt, perform_search=True) 
                
                SessionManager.add_to_conversation(f"Explain the protocol: {protocol_name}", response)
                st.rerun() 
        else:
            st.warning("Please enter a protocol name")

    render_continuous_chat()

def news_simplifier_page():
    show_back_button()

    st.markdown("# 📰 Crypto News Simplifier")
    st.markdown("Let Dobby break down complex crypto articles for you")

    news_input = st.text_area(
        "Paste article URL or full text:",
        height=200,
        placeholder="Paste a crypto news article URL or the full article text here...",
        help="Dobby will analyze the content and explain what it means"
    )

    if st.button("Simplify Article", type="primary"):
        if news_input:
            with st.spinner("Dobby is analyzing the article..."):
                prompt = f"""You're Dobby, a crypto-native AI. Someone just shared this crypto news with you:

{news_input}

Break this down in simple terms. Explain:
1. What actually happened (cut through the jargon)
2. Why it matters for regular crypto users
3. What the implications are for decentralization
4. Your honest take on whether this is good or bad news

Keep it clear and use your personality - don't just summarize, actually explain what people should understand."""
                SessionManager.clear_conversation()
                if 'search_context' in st.session_state: del st.session_state['search_context'] # Clear context
                response = dobby_client.chat(prompt)
                SessionManager.add_to_conversation(f"Simplify the news: {news_input[:100]}...", response)
                st.rerun()
        else:
            st.warning("Please paste an article URL or text")

    render_continuous_chat()

def document_analyzer_page():
    show_back_button()

    st.markdown("# 📄 Document Analyzer")
    st.markdown("Upload PDFs, DOCX, or plain text for Dobby to explain.")

    uploaded_file = st.file_uploader(
        "Choose a document to analyze:",
        type=['pdf', 'docx', 'txt', 'md'],
        help="Upload PDF, DOCX, text, or markdown files."
    )

    st.markdown("**Or paste document text directly:**")
    document_text = st.text_area(
        "Paste document content:",
        height=200,
        placeholder="Paste the document content here...",
    )

    col1, col2 = st.columns(2)
    with col1:
        analysis_focus = st.selectbox(
            "Analysis Focus:",
            ["General Summary", "Technical Deep Dive", "Risk Assessment", "Tokenomics", "Governance", "Use Cases"],
            key="doc_focus"
        )
    with col2:
        audience_level = st.selectbox(
            "Explanation Level:",
            ["Beginner-friendly", "Intermediate", "Technical", "Expert"],
            key="doc_audience"
        )

    if st.button("Analyze Document", type="primary"):
        document_content = ""
        doc_name = "Pasted Text"

        if uploaded_file is not None:
            document_content = extract_text_from_file(uploaded_file)
            doc_name = uploaded_file.name
        elif document_text.strip():
            document_content = document_text

        if document_content:
            if len(document_content) > 8000:
                document_content = document_content[:8000] + "\n\n[Document truncated...]"
                st.warning("⚠️ Document was truncated to fit processing limits.")

            with st.spinner("Dobby is analyzing the document..."):
                prompt = f"""You're Dobby, a crypto-native AI expert. Analyze the following document:

{document_content}

Analysis Focus: {analysis_focus}
Audience Level: {audience_level}

Provide a comprehensive analysis based on the focus and audience level. Cover key concepts, technology, decentralization aspects, risks, and your honest take."""
                SessionManager.clear_conversation()
                response = dobby_client.chat(prompt)
                SessionManager.add_to_conversation(f"Analyze the document: {doc_name} (Focus: {analysis_focus})", response)
                

                st.session_state.search_context = {
                    "type": "document",
                    "name": doc_name
                }
                
                st.rerun()
        else:
            st.warning("Please upload a file or paste document text to analyze")

    render_continuous_chat()

def terms_translator_page():
    """Crypto Terminology Translator page."""
    show_back_button()

    st.markdown("# 📖 Crypto Terminology Translator")
    st.markdown("Ask Dobby to explain any crypto or DeFi term")

    term_query = st.text_input(
        "Enter term or question:",
        placeholder="e.g., 'What is MEV?', 'impermanent loss', 'yield farming'...",
    )

    if st.button("Explain Term", type="primary"):
        if term_query:
            with st.spinner("Dobby is preparing the explanation..."):
                prompt = f"""You're Dobby, a crypto educator. Explain the term "{term_query}" clearly.

Cover:
1. Simple definition
2. Why it exists or is important
3. How it relates to decentralization
4. Common misconceptions."""
                SessionManager.clear_conversation()
                if 'search_context' in st.session_state: del st.session_state['search_context'] # Clear context
                response = dobby_client.chat(prompt)
                SessionManager.add_to_conversation(f"Explain the term: {term_query}", response)
                st.rerun()
        else:
            st.warning("Please enter a term or question")

    render_continuous_chat()

def strategy_validator_page():
    show_back_button()

    st.markdown("# ✅ DeFi Strategy Validator")
    st.markdown("Get Dobby's feedback on your DeFi plans")

    strategy_description = st.text_area(
        "Describe your DeFi strategy:",
        height=150,
        placeholder="e.g., 'I want to put $1000 into a Curve pool vs a Uniswap LP', 'Should I stake ETH on Lido or Rocket Pool?'...",
    )

    col1, col2 = st.columns(2)
    with col1:
        investment_amount = st.selectbox(
            "Investment size:",
            ["Under $500", "$500-$2000", "$2000-$10000", "$10000+", "Prefer not to say"],
        )
    with col2:
        experience_level = st.selectbox(
            "Your DeFi experience:",
            ["Complete beginner", "Some experience", "Intermediate", "Advanced"],
        )

    risk_tolerance = st.slider(
        "Risk tolerance (1=Conservative, 10=Aggressive):", 1, 10, 5
    )

    if st.button("Validate Strategy", type="primary"):
        if strategy_description:
            with st.spinner("Dobby is analyzing your strategy..."):
                prompt = f"""You're Dobby, a DeFi expert who cares about user safety and decentralization.

A user with '{experience_level}' experience shared their DeFi strategy: "{strategy_description}"

Additional context:
- Investment size: {investment_amount}
- Risk tolerance: {risk_tolerance}/10

Give them honest feedback covering potential risks, alignment with decentralization, and alternative approaches. Tailor your language to their experience level."""
                SessionManager.clear_conversation()
                if 'search_context' in st.session_state: del st.session_state['search_context'] # Clear context
                response = dobby_client.chat(prompt)
                SessionManager.add_to_conversation(f"Validate the strategy: {strategy_description[:50]}...", response)
                st.rerun()
        else:
            st.warning("Please describe your strategy")
            
    if SessionManager.get_conversation_history():
        st.info("💡 This is educational guidance, not financial advice. Always do your own research (DYOR).")
        
    render_continuous_chat()
