## Lilly: ChatGPT bot for Twitch

### Intro
This is my personal project to build an integrated AI chat bot into twitch. Right now, it is based off ChatGPT. However, in the future I plan to implement my own chatbot. 

![Chatbot screenshot](https://github.com/drozhevskii/chatGPT_bot_twitch/blob/main/twitch_bot_active.png)

### Description
The lilly_bot file contains the code to connect to ChatGPT API and send requests. This file is responsible for communicating between Twitch chat and ChatGPT. The initial prompt variable in the code sends the initial prompt that will set up some kind of personality for your bot. It has a voice function that uses internal Windows voice to give voice to your bot's responses in Twitch chat.

The twitch_bot file contains code to connect to your channel Twitch chat and read the chat. It uses functions from lilly_bot to communicate with ChatGPT by sending all the incoming messages to ChatGPT. You have to turn this python file into .exe format and run it. After running it, it will connect to your Twitch chat and will start responding to every message in Twitch chat.

[This GitHub page](https://github.com/TwitchIO/TwitchIO) explains in more detail how to get your Twitch API keys.

You can find your OpenAI key on the official [OpenAI website](https://openai.com/api/) after creating an account.

### ChatGPT Bot: Initialization and Functions
First, we create a script with all the functions our bot will use to make API calls:

### Required libraries:
```
import os # for importing env vars for the bot to use
import openai
import pyttsx3
from gtts import gTTS
import playsound
from twitchio.ext import commands
```

Put starting prompt to initialize a "personality" for your channel bot (could be your channel description).
The bot will use this information to answer relevant questions.
```
prompt = "Your channel description and/or any other personality traits you want your chatbot to have"
chat_log = prompt
```

Create the start and end sequences to keep a chat record.
```
start_sequence = "\nChatGPT"
restart_sequence = "\nChat: "
```

Write a function to make an API request to OpenAI with the question (or rather Twitch chat message).
In the first part, we configure ChatGPT 3.5 version we want to use (text-davinci-003) and set other settings however you want (you can experiment).
More about various GPT 3.5 models [here](https://platform.openai.com/docs/models/gpt-3-5).
Finally, in the second part, we want to save the answer we receive from the ChatGPT.
```
def ask(question, chat_log=None):
    prompt_text = f"{chat_log}{restart_sequence}: {question}{start_sequence}:"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt_text,
    temperature=0.98,
    max_tokens=218,
    top_p=1,
    frequency_penalty=0.47,
    presence_penalty=0.6,
    stop=['\n'],
    )
    
    answer = response['choices'][0]['text']
    return str(answer)
```

Write a function to keep track of the conversation and output it in the application later:
```
def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: 
        chat_log = prompt 

        return f"{chat_log}{restart_sequence} {question}{start_sequence}{answer}"
```







