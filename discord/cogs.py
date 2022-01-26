from asyncio import tasks
from discord.ext import commands
from datetime import datetime

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "hello":
            await msg.channel.send("Hi!")
            
    @commands.command()
    async def yellow(self, ctx):
        await ctx.send("White!")

def setup(bot):
    bot.add_cog(MyCog(bot))