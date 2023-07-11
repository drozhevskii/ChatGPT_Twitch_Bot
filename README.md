## ChatGPT Bot for Twitch

### Intro
This is my personal project to build a simple integrated AI chatbot into Twitch. Right now, it is based on ChatGPT. However, in the future, I plan to improve to match the latest GPT model. 

![Chatbot screenshot](https://github.com/drozhevskii/chatGPT_bot_twitch/blob/main/twitch_bot_active.png)

### Description
The chatGPT_bot file contains the code to connect to ChatGPT API and send requests. This file is responsible for communicating between Twitch chat and ChatGPT. The initial prompt variable in the code sends the initial prompt that will set up some kind of personality for your bot. It has a voice function that uses internal Windows voice to give voice to your bot's responses in Twitch chat.

The twitch_bot file contains code to connect to your channel Twitch chat and read the chat. It uses functions from chatGPT_bot to communicate with ChatGPT by sending it all the incoming messages. You have to turn this python file into .exe format and run it. After running it, it will connect to your Twitch chat and will start responding to every message in the chat, while you are able to monitor the bot through the console (like in the [screenshot](twitch_bot_active.png) above).

[This GitHub page](https://github.com/TwitchIO/TwitchIO) explains in more detail how to get your Twitch API keys.

You can find your OpenAI key on the official [OpenAI website](https://openai.com/api/) after creating an account.



#### ChatGPT Bot: Initialization and Functions

First, we create a script with all the functions our bot will use to make API calls:

Required libraries:
```
import os # for importing env vars for the bot to use
import openai
import pyttsx3
from gtts import gTTS
import playsound
from twitchio.ext import commands
```

Conneect to OpenAI API to be able to make requests directly to ChatGPT:
```
OPENAI_API_KEY = 'Your OpenAI API key'
openai.api_key = OPENAI_API_KEY
```

Put starting prompt to initialize a "personality" for your channel bot (could be your channel description).
The bot will use this information to answer relevant questions.
```
prompt = "Your channel description and/or any other personality traits you want your chatbot to have"
chat_log = prompt
```

Create the start and end sequences to keep a chat record. 
```
start_sequence = "\nChatGPT:"
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

Write functions to get messages in the chat as input and read it with the internal TTS library.
In the first function, I configure my TTS function (you can experiment). The second function simply takes the answer as input and speaks it out.
I use these functions in the Twitch Bot script.
```
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 180)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def read_chat(text):
    speak(str(text))
```

Write the last function that activates the bot.
It takes the incoming response, appends it to the active conversation, and prints it out to the console.
```
def chatGPT(message):
    incoming_msg = message
    answer = ask(incoming_msg, chat_log)
    append_interaction_to_chat_log(incoming_msg, answer, chat_log)

    print(str(answer))
    speak(str(answer))
```


#### Twitch Bot: Uses created above functions and connect ChatGPT Bot to Twitch.

Here, we implement the functions above and connect the bot to the Twitch account you want it to appear on.

Get the necessary functions from the previous script (above):
```
from twitchio.ext import commands
import os

from chatGPT_bot import chatGPT, read_chat
```

Put the information such as API tokens and keys as variables:
```
oauth_token = 'Twitch API key'
client_id = 'Twitch Client ID'

bot_account = 'Your Bot Name' (in case you want to have multiple bots connected to your stream)
channel_name = 'Your channel name'
```

Write a Twitch Bot class with functions to connect, read, and answer chat messages:
```
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=oauth_token,
            client_id=client_id,
            nick=bot_account,
            prefix='!',
            initial_channels=[channel_name]
        )
    
    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot
        # For now we just want to ignore them
        if message.echo:
            return

        # Print the contents of our message to console
        print('Chat: ', message.content)
        read_chat(message.content)
        print(chatGPT(message.content))

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # We can also give our commands aliases (different names) to invoke with.

        await ctx.send(f'Hello {ctx.author.name}!')
```

Run the bot:
```
bot = Bot()
bot.run()
```

In order to turn this program into an executable, use the Pyinstaller library.
Pyinstaller allows you to quickly convert a Python file to an executable file from your terminal.

This code is a command line instruction that uses the PyInstaller library to create a standalone executable file for the Python script "validation.py".
The "--onefile" option specifies that the output should be a single executable file instead of a directory with multiple files.
When executed, this file will run the "validation.py" script without requiring the user to have Python or any dependencies installed.
```
pyinstaller --onefile twitch_bot.py
```



