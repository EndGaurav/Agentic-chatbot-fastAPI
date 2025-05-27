from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent
import uvicorn
 
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool
    

ALLOWED_MODEL_PROVIDERS = ["llama-3.3-70b-versatile", "gemini-2.0-flash", "gpt-4o-mini"]

app = FastAPI(title="Langgraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in ALLOWED_MODEL_PROVIDERS:
        return {"error": f"Model name {request.model_name} not allowed."}
   
    response = get_response_from_ai_agent(
        llm_id=request.model_name,
        query=request.messages,
        allow_search=request.allow_search,
        system_prompt=request.system_prompt,
        provider=request.model_provider,
    )
    
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)