# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
if openai.api_key == "":
    print(openai.api_key)
    print(" openai key is invalid")
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

while True:
    reqTxt = input("user :")
    new_message = {"role": "user", "content": reqTxt}
    messages.append(new_message)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    result = response['choices'][0]['message']['content']
    print("gpt :"+result)
    messages.append(response['choices'][0]['message'])
