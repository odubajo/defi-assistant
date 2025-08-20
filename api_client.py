import os
import requests
from dotenv import load_dotenv
from typing import List, Dict
from tavily import TavilyClient 

load_dotenv()

def get_web_context(query: str) -> str:
    try:
        tavily_api_key = os.getenv("TAVILY_API_KEY")
        if not tavily_api_key:
            return "Search is not configured."
            
        tavily = TavilyClient(api_key=tavily_api_key)
        response = tavily.search(query=query, search_depth="basic", max_results=5)
        
        context = "\n".join([f"- {res['content']}" for res in response['results']])
        return context
    except Exception as e:
        print(f"Error during web search: {e}")
        return f"Error fetching web context: {str(e)}"

class DobbyAPI:
    def __init__(self):
        self.api_url = "https://api.fireworks.ai/inference/v1/chat/completions"
        self.api_key = os.getenv("FIREWORKS_API_KEY")
        if not self.api_key:
            raise ValueError("FIREWORKS_API_KEY not found. Please set it in your .env file.")

    def chat(self, prompt: str, model: str = "accounts/sentientfoundation/models/dobby-unhinged-llama-3-3-70b-new", conversation_history: List[Dict] = None, perform_search: bool = False) -> str:
        """Sends a request to the Dobby API, with an optional web search."""
        try:
            final_prompt = prompt
            
            if perform_search:
                print("Performing web search for up-to-date context...")
                web_context = get_web_context(prompt)
                
                final_prompt = f"""Based on the following current web search results, provide a comprehensive answer to the user's request. Synthesize the information from the context and also use your own knowledge.

[Web Search Context from {current_date}]:
{web_context}

[User's Original Request]:
{prompt}
"""
                print("Augmented prompt created.")

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            messages = list(conversation_history) if conversation_history else []
            messages.append({"role": "user", "content": final_prompt})

            payload = {
                "model": model,
                "messages": messages,
                "max_tokens": 2000,  
                "temperature": 0.5 
            }

            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()

            return response.json()["choices"][0]["message"]["content"]

        except Exception as e:
            return f"Error connecting to Dobby: {str(e)}"


from datetime import datetime
current_date = datetime.now().strftime("%B %d, %Y")

dobby_client = DobbyAPI()