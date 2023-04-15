from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import os
from pydantic import BaseModel
from fastapi import FastAPI
import json
os.environ["OPENAI_API_KEY"] = 'your_api_key'

app = FastAPI()

class ConversationHistory:
    def __init__(self):
        self.history = "Below is the conversation you just had so answer accordingly"
        self.history = self.history + '\n'

    def add_input(self, input_text):
        self.history = self.history +'ques: '+ input_text
        self.history = self.history + '\n'
    
    def add_ans(self,ans):
        self.history = self.history + ans
        self.history = self.history + '\n'
        
        
    def get_context(self):
        return self.history

def ask_me(question,prompt):
    query = question +prompt
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(query, response_mode="compact")
    return response.response

history = ConversationHistory()

# construct_index('textdata')
@app.post("/chatbot")
async def chatbot_handler(input_text: str):
    history.add_input(input_text)
    context = history.get_context()
    ans = ask_me(input_text,context)
    history.add_ans(ans)
    
    return ans
    


#python -m uvicorn main:app --reload