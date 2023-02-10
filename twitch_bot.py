from twitchio.ext import commands
import os

from lilly_bot import lilly, read_chat

oauth_token = 'cz2vt1mcdmayc102p2astx05aag6d7'
client_id = 'gp762nuuoqcoxypju8c569th9wz7q5'


bot_account = 'Lilly'
channel_name = 'permatoxxic'

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
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        #self.incoming_msg = message.content
        print('Chat: ', message.content)
        read_chat(message.content)
        print(lilly(message.content))
        #print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        #await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')

bot = Bot()
bot.run()
    