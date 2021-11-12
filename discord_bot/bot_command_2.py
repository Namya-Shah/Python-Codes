import discord
from discord import user

client = discord.Client()

@client.event
async def on_message(message):
    if str(message.channel) == "general" and message.content != "":
        await message.channel.purge(limit=1)

client.run('OTA3NTYyMTIyODg2NjcyMzk3.YYo_Fw.pKeeoRBp0fjjE1EcgFLw-g_QsXg')