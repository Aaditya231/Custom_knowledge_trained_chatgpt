# Custom_knowledge_trained_chatgpt

I am using in-context learning in order to train chatgpt on custom data that can be anything related to your organization or any text data in general
I used gpt-3.5-turbo model which is the same model chatgpt is trained on
Since openai have released a limited amount of tokens so the response will not be the same as chatgpt but it will be more than enough.

# To train it on your data:
* Add all data in form of txt extension in textdata folder. You can add any number of files and can also paste codes in txt files.
* Run train.py and it will generate an index.json file
* The model then uses this index file along with its previous knowledge to generate response

# To host it on web

