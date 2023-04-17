from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import gradio as gr
import os
from fastapi import FastAPI
import json
from IPython.display import display, Markdown
os.environ["OPENAI_API_KEY"] = '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'


# def construct_index(directory_path):
#     max_input_size = 4096
#     num_outputs = 256
#     max_chunk_overlap = 20
#     chunk_size_limit = 600

#     llm_predictor = LLMPredictor(llm=ChatOpenAI(
#         temperature=0, model_name="gpt-3.5-turbo", max_tokens=num_outputs))
#     prompt_helper = PromptHelper(
#         max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
#     documents = SimpleDirectoryReader(directory_path).load_data()

#     index = GPTSimpleVectorIndex(
#         documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
#     )

#     index.save_to_disk('index1.json')

#     return index


def ask_me(question):
    prompt = "Below is the conversation you just had so answer accordingly\n"
    prompt = prompt + 'ques:'+ question
    prompt = prompt + '\n'
    query =prompt+ question 
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(query, response_mode="compact")
    prompt = prompt + 'your reply:'+ response.response
    prompt = prompt + '\n'
    return response.response
iface   =   gr . Interface ( fn = ask_me ,
                            inputs = gr.inputs.Textbox(lines=7,label="Enter text here"),
                            outputs = gr.outputs.Textbox(label="Chatbot's response") ,
                            title="Custom-trained AI chatbot")



# construct_index('textdata')
# An endless while loop is generated so that you can keep asking questions and not have to run it each time
# The prompt provides it with previous questions to get the best response

count = 0
while count < 5:
    iface.launch(share=True)
    
     
        
           