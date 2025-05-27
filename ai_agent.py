import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


SYSTEM_PROMPT = """
Act as an AI chatbot who is smart, friendly, and helpful. 
You are an AI agent that helps users find information on the internet. 
"""

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    print(llm_id, query, allow_search, system_prompt, provider)
    if provider == "Gemini":
        llm = ChatOpenAI(model=llm_id, api_key=GEMINI_API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
    elif provider == "Groq":
        llm = ChatGroq(model=llm_id, api_key=GROQ_API_KEY)
   
    tools = [TavilySearch(max_results=2)] if allow_search else []
  
  
    agent = create_react_agent(model=llm, tools=tools, prompt=system_prompt) 


    state = {"messages": query}

    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]

    print("ai_agent line 57: ", ai_messages)
    return ai_messages[-1]