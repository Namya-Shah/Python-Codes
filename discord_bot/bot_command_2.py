import token as t
import discord
from discord import user

client = discord.Client()

@client.event
async def on_message(message):
    if str(message.channel) == "general" and message.content != "":
        await message.channel.purge(limit=1)

client.run(t.token)