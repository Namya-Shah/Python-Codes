import discord
from discord import user

client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        if str(message.author) == "ARGxHuLk#7154":
            await message.channel.send("Hello" + str(message.author) + "!")
        else:
            await message.channel.send("Hello, I am a test bot.")
            

client.run('OTA3NTYyMTIyODg2NjcyMzk3.YYo_Fw.pKeeoRBp0fjjE1EcgFLw-g_QsXg')