# Importing discord and asyncio for later use
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

# Initiating the client, so that discord knows its active
Client = discord.Client()
# Setting the prefix for the client
client = commands.Bot(command_prefix=".")

# When the bot is ready
@client.event
async def on_ready():
	# Set the presence of the bot to this, with the streaming status
    await client.change_presence(game=discord.Game(name="Sending messages via console", url="https://twitch.tv/streamer", type=1))
	# Ask for the server ID you want to talk in
    server=input('Server ID: ')
	# Ask for the channel ID you want to talk in
    ch=input('Channel ID: ')
	# Once we have both, confirm it
    print('Enjoy sending messages!')
    print('-----------------------')
    while True:
	# Wait for a message to send
        msg=input()
	# Get the server
        server = client.get_server(server)
        try:
		# Try and send the message specified to the server and then channel
            await client.send_message(client.get_channel(ch), msg)
		# If there's an error, stop trying to send message and pass
        except Exception:
            pass
		
client.run("PASTE YOUR TOKEN HERE")
