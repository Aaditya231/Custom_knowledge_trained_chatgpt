from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import os
from fastapi import FastAPI
import json
from IPython.display import display, Markdown
os.environ["OPENAI_API_KEY"] = 'your_api_key'


def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 256
    max_chunk_overlap = 20
    chunk_size_limit = 600

    llm_predictor = LLMPredictor(llm=ChatOpenAI(
        temperature=0, model_name="gpt-3.5-turbo", max_tokens=num_outputs))
    prompt_helper = PromptHelper(
        max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )

    index.save_to_disk('index1.json')

    return index


def ask_me(question,prompt):
    query =prompt+ question 
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(query, response_mode="compact")
    return response.response



construct_index('textdata')

# prompt = "Below is the conversation you just had so answer accordingly\n"
# count = 0
# while count < 5:
    
#      ques = input()
#      ans = ask_me(ques,prompt)
#      prompt = prompt + 'ques:'+ ques
#      prompt = prompt + '\n'
#      prompt = prompt + 'your reply:'+ ans
#      prompt = prompt + '\n'
#      print(ans)
        
           