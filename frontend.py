import streamlit as st
import requests

st.set_page_config( page_title="LanggGraph Agent UI", page_icon="🤖")
st.title("AI Chatbot Agents")
st.write("Welcome to the AI Chatbot Agents!")

system_prompt = st.text_area("Define your ai agents: ", height=100, placeholder="Type your system prompt here...")
provider = st.radio("Select an provider:", ["Gemini", "Groq"]) 


if provider == "Groq":
    selected_model = st.selectbox("Select Groq model: ", ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"])
elif provider == "Gemini":
    selected_model = st.selectbox("Select Gemini model: ", ["gemini-2.0-flash", "Gemini 2.5 Flash Preview 05-20"])

web_search = st.checkbox("Allow web search")

user_query = st.text_area("Define your query: ", height=100, placeholder="Type your query here...")

API_URL = "https://chat-with-agent.onrender.com/chat"

if st.button("Ask Agent"):
    if user_query.strip():
        messages = [user_query]
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": messages,
            "allow_search": web_search
        }
        response = requests.post(API_URL, json=payload)
        print(f"Response line 34 at frontend.py: {response}")
        if response.status_code == 200:
            response_data = response.json()
            print(f"Response data line 37 at frontend.py: {response_data}")
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                # st.markdown(f"**Final Response:** {response_data['final_response']}")
                st.markdown(f"**Final Response:** {response_data}")