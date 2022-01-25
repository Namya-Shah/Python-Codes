import discord
from discord.ext import commands,tasks
 
bot = commands.Bot(command_prefix = "!")
 
class MyPoll(commands.Cog):
 
    def __init__(self,bot):
        self.bot = bot
        self.numbers = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
 
    @commands.command()
    async def poll(self,ctx, minutes : int, title, *options):
 
        if len(options) == 0:
            pollEmbed = discord.Embed(title = title, description = f"You have **{minutes}** minutes remaining!")
            msg = await ctx.send(embed = pollEmbed)
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")
 
        else:
            pollEmbed = discord.Embed(title = title, description = f"You have **{minutes}** minutes remaining!")
            for number,option in enumerate(options):
                pollEmbed.add_field(name = f"{self.numbers[number]}", value = f"**{option}**", inline = False)
            msg = await ctx.send(embed = pollEmbed)
            for x in range(len(pollEmbed.fields)):
                await msg.add_reaction(self.numbers[x])
        self.poll_loop.start(ctx, minutes, title, options, msg)
 
    @tasks.loop(minutes = 1)
    async def poll_loop(self, ctx, minutes, title, options, msg):
 
        count = self.poll_loop.current_loop
        remaining_time = minutes - count
 
        newEmbed = discord.Embed(title = title, description = f"You have **{remaining_time}** minutes remaining!")
        for number,option in enumerate(options):
                newEmbed.add_field(name = f"{self.numbers[number]}", value = f"**{option}**", inline = False)
        
        await msg.edit(embed = newEmbed)
        
        if remaining_time == 0:
            self.poll_loop.stop()
            counts = []
            msg = discord.utils.get(bot.cached_messages, id = msg.id)
            reactions = msg.reactions
 
            for reaction in reactions:
                counts.append(reaction.count)
            max_value = max(counts)
            i = 0
            for count in counts:
                if count == max_value:
                    i = i + 1
            if i > 1:
                await ctx.send("It's a Draw!")
 
            else:
                max_index = counts.index(max_value)
 
                if len(options) == 0:
                    winneremoji = reactions[max_index]
                    await ctx.send("Times up!")
                    if winneremoji.emoji == "👍":
                        await ctx.send("Looks like people think that way.")
                    if winneremoji.emoji == "👎":
                        await ctx.send("Looks like people dont think that way.")
                
                else:
                    winner = options[max_index]
                    winneremoji = reactions[max_index]
 
                    await ctx.send("Times Up!")
                    await ctx.send(f"{winneremoji.emoji} **{winner}** has won the Poll!")
 
            
 
bot.add_cog(MyPoll(bot))
bot.run("TOKEN")