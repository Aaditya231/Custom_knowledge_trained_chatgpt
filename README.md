# Custom_knowledge_trained_chatgpt

I am using in-context learning in order to train chatgpt on custom data that can be anything related to your organization or any text data in general
I used gpt-3.5-turbo model which is the same model chatgpt is trained on.<p></p>
We can have our ChatGPT based chatbot, output the correct answers to user questions, even though the answers to these questions were not included in the chatbots/ChatGPT’s training data.

# To train it on your data:
* Get an api key from openai api site and replace your_api_key with that token
* Add all data in form of txt extension in textdata folder. You can add any number of files and can also paste codes in txt files.
* Run train.py and it will generate an index.json file
* The model then uses this index file along with its previous knowledge to generate response

## execute test.py to run it in terminal
This is a sample interface ,it can be modified according to your needs
<p align="center">
  <img src="images/img_1.png">
</p>
<p align="center">
  <img src="images/img_2.png">
</p>
To get an openai api key 
<p align="center">
  <img src="images/img_3.png">
</p>

## Main.py is used to run the model on local host
This is the fast api swagger ui
<p align="center">
  <img src="images/img_4.png">
</p>

## Scopes of use:
* You can easily create a question and answer bot
* It can be trained on any novel or book and then using prompt engineering it can behave like any character from that book
* With help of prompt engineering you can use for any purpose you want

Sources/inspirations:

https://beebom.com/how-train-ai-chatbot-custom-knowledge-base-chatgpt-api/ (For UI) <p></p>
https://blog.devgenius.io/creating-a-chatgpt-based-chatbot-using-in-context-learning-method-17c30ba72f3 (to know more about in-context learning)
