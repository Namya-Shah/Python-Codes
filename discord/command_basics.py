from dis import disco
import discord
import random
from discord.ext import commands
import datetime
from datetime import datetime
import asyncio

bot = commands.Bot(command_prefix="!", help_command=None)

def is_me(ctx):
    return ctx.author.id == 664753095074512908

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
    
@bot.command()
async def coinflip(ctx):
    num = random.randint(1, 2)
    
    if num == 1:
        await ctx.send("Heads!")
    else:
        await ctx.send("Tails!")

@bot.command()
async def rps(ctx, hand):
    hands = ["✌️", "✋", "👊"]
    bothand = random.choice(hands)
    await ctx.send(bothand)
    if hand == bothand:
        await ctx.send("It's a Draw!")
    elif hand == "✌️":
        if bothand == "👊":
            await ctx.send("Bot Won!")
        if bothand == "✋":
            await ctx.send("You Won!")
    elif hand == "✋":
        if bothand == "👊":
            await ctx.send("You Won!")
        if bothand == "✌️":
            await ctx.send("Bot Won!")
    elif hand == "👊":
        if bothand == "✋":
            await ctx.send("Bot Won!")
        if bothand == "✌️":
            await ctx.send("You Won!")

@bot.command(aliases = ["about"])
async def help(ctx):
    MyEmbed = discord.Embed(title = "Commands", description = "These are the commands that you can use for this bot!", color = discord.Colour.dark_purple())
    MyEmbed.set_thumbnail(url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flogos-world.net%2Fwp-content%2Fuploads%2F2021%2F05%2FDiscord-New-Logo.png&f=1&nofb=1")
    MyEmbed.add_field(name = "!ping", value = "This Command replies with Pong whenever you write !ping", inline=None)
    MyEmbed.add_field(name = "!coinflip", value = "This Command lets you flip a coing", inline=None)
    MyEmbed.add_field(name = "!rps", value = "This Command allows you to play the game with the bot", inline=None)
    await ctx.send(embed = MyEmbed)

@bot.group()
async def edit(ctx):
    pass

@edit.command()
async def servername(ctx,*,servername):
    await ctx.guild.edit(name = servername)

@edit.command()
async def region(ctx,*,servername):
    await ctx.guild.edit(region = servername)
    
@region.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Please enter a valid region name!")
    
    
@edit.command()
async def createtextchannel(ctx,*,servername):
    await ctx.guild.create_text_channel(name = servername)

@edit.command()
async def createvoicechannel(ctx,*,servername):
    await ctx.guild.create_voice_channel(name = servername)
    
@edit.command()
async def createrole(ctx,*,servername):
    await ctx.guild.create_role(name = servername)

@bot.command()
@commands.has_role("Administrator")
async def kick(ctx, member: discord.Member,*, reason = None):
    await ctx.guild.kick(member, reason=reason)
    
@kick.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have necessary roles for this command!")

@bot.command()
@commands.has_role("Administrator")
async def ban(ctx, member: discord.Member,*, reason = None):
    await ctx.guild.ban(member, reason=reason)
    
@ban.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have necessary roles for this command!")


@bot.command()
@commands.has_role("Administrator")
async def unban(ctx, *, input):
    name, discriminator = input.split("#")
    banned_members = await ctx.guild.bans()
    for bannedmember in banned_members:
        username = bannedmember.user.name
        disc = bannedmember.user.discriminator
        if name == username and discriminator == disc:
            await ctx.guild.unban(bannedmember.user)
            
@unban.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have necessary roles for this command!")

@bot.command()
@commands.check(is_me)
async def purge(ctx, amount, day : int = None, month : int = None, year : int = datetime.now().year):
    if amount == "/":
        if day == None or month == None:
            return
        else:
            await ctx.channel.purge(after = datetime(year, month, day))
    else:
        await ctx.channel.purge(limit = int(amount) + 1)
        
@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to specify a number or a date.")
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("You can type / or a number or a date.")
        
#mute
@bot.command()
async def mute(ctx, user: discord.Member):
    await user.edit(mute = True)

#unmute
@bot.command()
async def unmute(ctx, user: discord.Member):
    await user.edit(mute = False)

#deafen
@bot.command()
async def deafen(ctx, user: discord.Member):
    await user.edit(deafen = True)

#undeafen
@bot.command()
async def undeafen(ctx, user: discord.Member):
    await user.edit(deafen = False)

#voicekick
@bot.command()
async def voicekick(ctx, user: discord.Member):
    await user.edit(voice_channel = False)

@bot.command()
async def reload(ctx):
    bot.reload_extension("cogs")

bot.load_extension("cogs")

bot.run("OTM1MDI2ODQ5OTU5MDE0NDcx.Ye4pnA.ju77dc_WeA5jYdE8tR8ufdj-j9A")