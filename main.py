import os
import creds

import discord
from discord.ext import commands

# Initialize the bot with all intents and set the command prefix to "!"
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    """
    Event handler for when the bot is ready.
    Prints a message to the console and loads all extensions in the 'cogs' directory.
    """
    print("The bot is online")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_message(message):
    """
    Event handler for when a message is sent in the server.
    Responds to specific messages and processes commands.
    """
    if message.author == client.user:
        return

    # Respond to greetings
    if str(message.content).lower().startswith("witaj rpgobocie") or str(message.content).lower().startswith("cześć rpogbocie"):
        await message.channel.send('Cześć!')
        await message.add_reaction("\U0001F44B")

    # Respond to a specific question
    if str(message.content) == 'RPGobocie! Czy chciałbyś pograć w RPGi?':
        await message.channel.send('Oczywiście!')
        await message.add_reaction("\U0001F44D")

    # Process commands if any
    await client.process_commands(message)

# Run the bot with the provided token
client.run(creds.discord_bot_key)
