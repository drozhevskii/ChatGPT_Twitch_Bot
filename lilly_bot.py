import os # for importing env vars for the bot to use
#from twitchio.ext import commands
import openai
import pyttsx3
from gtts import gTTS
import playsound
from twitchio.ext import commands

oauth_token = "YOUR TWITCH TOKEN"
client_id = "YOUR TWITCH CLIENT ID"
bot_account = 'Lilly'
channel_name = 'YOUR CHANNEL NAME'

OPENAI_API_KEY = "YOUR OPEN AI key"
#openai.api_key = os.environ['OPENAI_API_KEY']
openai.api_key = OPENAI_API_KEY

start_sequence = "\nLilly"
restart_sequence = "\nChat: "

prompt = "YOUR INITAL PROMPT FOR BOT"
chat_log = prompt

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

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: 
        chat_log = prompt 

        return f"{chat_log}{restart_sequence} {question}{start_sequence}{answer}"

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 180)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def read_chat(text):
    speak(str(text))


def lilly(message):
    incoming_msg = message
    answer = ask(incoming_msg, chat_log)
    append_interaction_to_chat_log(incoming_msg, answer, chat_log)

    print(str(answer))
    speak(str(answer))

#lilly()
