# Agri Chatbot LLM 🌾

Agri Chatbot LLM is a simple AI-powered chatbot that answers agriculture-related questions using a Large Language Model.  
It helps users get information about crops, farming practices, pests, fertilizers, and general agriculture topics.



## Features
- 🤖 Conversational chatbot for agriculture-related questions  
- 🌱 Answers on crops, pests, diseases, fertilizers, irrigation, and weather impact  
- 🧠 Uses LLM (OpenAI GPT) for natural language understanding  
- 🔒 Secure API key handling using environment variables  
- 💬 Maintains conversation context (memory)  
- 🧪 Easy to extend with RAG (PDFs, research papers, ICAR data) 

## 🏗️ Architecture Overview
User Question  
↓  
Prompt + Conversation History  
↓  
LLM (OpenAI GPT Model)  
↓  
Agricultural Answer  



## Tech Stack
- Python
- Streamlit
- OpenAI API


## Project Structure
```text
agri-chatbot-llm/
│── app.py               # Main chatbot application
│── requirements.txt     # Project dependencies
│── .env.example         # Environment variable template
│── .gitignore           # Prevents secrets from being pushed
│── README.md            # Project documentation
```

## Environment Setup (Important)
Create a .env file in the root directory:
```
OPENAI_API_KEY=your_api_key_here
```
⚠️ Never push .env or API keys to GitHub

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```
## Sample Questions
- "What are early signs of thrips infestation in onion crops?"
- "Which fertilizer is best for banana plantation?"
- "How does rainfall affect pest incidence?"
- "Best practices to control red spot thrips?"
- "Ideal temperature for wheat cultivation?"

