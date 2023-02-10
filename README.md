## Lilly: ChatGPT bot for Twitch

### Intro
This is my personal project to build an integrated AI chat bot into twitch. Right now, it is based off ChatGPT. However, in the future I plan to implement my own chatbot. 

### Files
The lilly_bot file contains the code to connect to ChatGPT api and send requests. This file is responsible for communicating between Twitch chat and ChatGPT. The initial prompt variable in the code send the initial prompt that will set up some kind of personality for your bot. It has a voice function that uses internal Windows voice to give voice to your bot's responses in twitch chat.

The twitch_bot file contains code to connect to your channel twitch chat and read the chat. It uses functions from lilly_bot to communicate with ChatGPT by sending all the incoming messages to ChatGPT. You have to turn this python file into .exe format and run it. After running it, it will connect to your twitch chat and will start responding to every message in twitch chat.

This Github is explaning in more detail how to get your twitch API keys:
https://github.com/TwitchIO/TwitchIO

You can find your OpenAI key on official OpenAI website after creating an account:
https://openai.com/api/
