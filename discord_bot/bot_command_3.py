import discord
from discord import user
from discord.ext import commands

#client = discord.Client()
client = commands.Bot(command_prefix="!")

'''
@client.event
async def on_message(message):
    if str(message.channel) == "general" and message.content != "":
        await message.channel.purge(limit=1)
'''

@client.command()
async def hello(ctx, arg1, arg2):
    await ctx.send("This is arg1: " + arg1 + ", this is arg2: " + arg2)

        

client.run('OTA3NTYyMTIyODg2NjcyMzk3.YYo_Fw.pKeeoRBp0fjjE1EcgFLw-g_QsXg')