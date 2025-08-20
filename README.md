# 🎯 web3 Clarity Assistant

> Powered by Dobby AI - Your crypto-native guide to understanding DeFi protocols, news, and strategies.

web3 Clarity Assistant is a comprehensive Streamlit application that helps users navigate the complex world of Decentralized Finance (DeFi) through AI-powered explanations, document analysis, and strategic guidance.

## ✨ Features

### 🔧 Core Tools

- **📚 DeFi Protocol Explainer**: Get detailed explanations of any DeFi protocol with web-based research
- **📄 Document Analyzer**: Upload and analyze PDFs, DOCX, or text files (whitepapers, documentation)
- **✅ DeFi Strategy Validator**: Receive feedback on your DeFi investment strategies
- **📰 Crypto News Simplifier**: Break down complex crypto articles into understandable insights
- **📖 Crypto Terms Translator**: Explain DeFi terminology and concepts

### 🎨 User Experience

- **Conversational Interface**: Maintains context across questions within each tool
- **Modern UI**: Dark theme with cyberpunk-inspired design and smooth animations
- **Session Management**: Track conversation history and statistics
- **Multi-format Support**: Handle various document types (PDF, DOCX, TXT, MD)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- API keys for:
  - [Fireworks AI](https://fireworks.ai/) (for Dobby AI model)
  - [Tavily](https://tavily.com/) (for web search functionality)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd defi-clarity-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   FIREWORKS_API_KEY=your_fireworks_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the app**
   
   Open your browser to `http://localhost:8501`

## 📁 Project Structure

```
defi-clarity-assistant/
├── app.py                 # Main Streamlit application
├── config.py             # App configuration and CSS styling
├── session_manager.py    # Session state management
├── api_client.py         # API integrations (Fireworks AI, Tavily)
├── requirements.txt      # Python dependencies
├── ui/
│   ├── components.py     # Reusable UI components
│   └── pages.py          # Page-specific functionality
└── .env                  # Environment variables (create this)
```

## 🔧 Configuration

### API Keys Setup

1. **Fireworks AI API Key**
   - Sign up at [Fireworks AI](https://fireworks.ai/)
   - Get your API key from the dashboard
   - Add to `.env` as `FIREWORKS_API_KEY`

2. **Tavily API Key** (for web search)
   - Sign up at [Tavily](https://tavily.com/)
   - Get your API key
   - Add to `.env` as `TAVILY_API_KEY`

### Customization

- **Styling**: Modify `CUSTOM_CSS` in `config.py` to customize the appearance
- **AI Model**: Change the model parameter in `api_client.py` to use different Fireworks AI models
- **Search Settings**: Adjust search parameters in the `get_web_context` function

## 🎯 Usage Guide

### 1. Protocol Explanation
- Enter any DeFi protocol name (e.g., "Uniswap", "AAVE", "Curve")
- Get comprehensive explanations with current web research
- Ask follow-up questions to dive deeper

### 2. Document Analysis
- Upload PDF, DOCX, TXT, or MD files
- Choose analysis focus (General, Technical, Risk Assessment, etc.)
- Select audience level (Beginner to Expert)
- Continue the conversation with follow-up questions

### 3. Strategy Validation
- Describe your DeFi strategy or investment plan
- Provide context about experience level and risk tolerance
- Receive honest feedback and alternative suggestions

### 4. News Simplification
- Paste article URLs or full article text
- Get clear breakdowns of complex crypto news
- Understand implications for decentralization and users

### 5. Terms Translation
- Ask about any crypto or DeFi terminology
- Get clear definitions with context and examples
- Learn about common misconceptions

## 🛠️ Technical Details

### Dependencies

- **Streamlit**: Web application framework
- **Requests**: HTTP library for API calls
- **PyPDF2**: PDF text extraction
- **python-docx**: DOCX document processing
- **tavily-python**: Web search integration
- **python-dotenv**: Environment variable management

### Architecture

- **Modular Design**: Separate files for configuration, session management, and UI components
- **State Management**: Persistent conversation history and context
- **API Integration**: Fireworks AI for LLM capabilities, Tavily for web search
- **Document Processing**: Support for multiple file formats with error handling

## 🔒 Privacy & Security

- **Local Processing**: Document content is processed locally before sending to AI
- **API Security**: API keys stored in environment variables
- **Session Isolation**: Each user session is independent
- **No Data Persistence**: Conversations are cleared when sessions end


### Common Issues

1. **API Key Errors**
   - Ensure `.env` file exists with correct API keys
   - Check API key format and permissions

2. **Document Upload Issues**
   - Verify file format is supported (PDF, DOCX, TXT, MD)
   - Check file size limitations
   - Ensure file is not corrupted

3. **Slow Response Times**
   - Web search functionality may take longer
   - Large documents are truncated to improve performance
   - Check internet connection for API calls

4. **Styling Issues**
   - Clear browser cache
   - Try refreshing the page
   - Check browser compatibility

### Getting Help

- Check the console logs for error messages
- Review the `.env` file setup
- Ensure all dependencies are installed
- Try restarting the Streamlit server

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py
```


**Built with ❤️ for the DeFi community**

*Powered by Dobby AI - Bringing clarity to the decentralized world*
