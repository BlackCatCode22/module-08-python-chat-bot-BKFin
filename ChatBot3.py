# ChatBotApp.py
# This is custom code put together by myself and some code found on various places on the internet - BKF
# Code updated 5/5/2024
# This chatbot allows for remembering the conversation
# For example, you can tell it your name, and then later ask it your name and it'll remember
# I tried to make it more compact than the original starter code we were given.

import openai

openai.api_key = "sk-proj-nv0Umded1IfystKFPzztT3BlbkFJXL9i06a3wdHtFn5LOFQ7"

message = {"role":"user", "content":  input("[To exit, send \"###\".]\n\nPython Student:")}

conversation = [{"role": "system", "content": "Assume the role of a Python teacher, and think step by step. Your name is Skippy Py."}]

while(message["content"]!="###"):

    try:
        conversation.append(message)
        completion = openai.chat.completions.create(model="gpt-3.5-turbo", messages=conversation, temperature=0, max_tokens=2024, top_p=1, frequency_penalty=0, presence_penalty=0) 
        message["content"] = input(f"Python Teacher: {completion.choices[0].message.content} \n\nPython Student: ")
        print()
        conversation.append(completion.choices[0].message)
    except Exception as e:
        # Print an error message if the API call fails
        print("Error generating response:", e)