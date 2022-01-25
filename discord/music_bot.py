from aiohttp import client
from discord.ext import commands
import discord, youtube_dl, os, asyncio
bot = commands.Bot(command_prefix = "!")
queuelist = []
filestodelete = []
 
@bot.command()
@commands.has_role("DJ")
async def join(ctx):
    user = ctx.message.author
    vc = user.voice.channel

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild) # This allows for more functionality with voice channels

    if voice == None: # None being the default value if the bot isnt in a channel (which is why the is_connected() is returning errors)
        await vc.connect()
        await ctx.send(f"Joined **{vc}**")
    else:
        await ctx.send("I'm already connected!")
 
@bot.command()
@commands.has_role("DJ")
async def leave(ctx, help = "leaves the Voice Channel"):
    await ctx.voice_client.disconnect()
 
@bot.command()
@commands.has_role("DJ")
async def play(ctx, *, searchword):
    ydl_opts = {}
    voice = ctx.voice_client
 
    #Get the Title
    if searchword[0:4] == "http" or searchword[0:3] == "www":
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(searchword, download = False)
            title = info["title"]
            url = searchword
 
    if searchword[0:4] != "http" and searchword[0:3] != "www":
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{searchword}", download = False)["entries"][0]
            title = info["title"]
            url = info["webpage_url"]
 
    ydl_opts = {
        'format' : 'bestaudio/best',
        "outtmpl" : f"{title}.mp3",
        "postprocessors": 
        [{"key" : "FFmpegExtractAudio", "preferredcodec" : "mp3", "preferredquality" : "192"}],   
    }
 
    #Downloads the Audio File with the Title, it is run in a different thread so that the bot can communicate to the discord server while downloading
    def download(url):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, download, url)
 
    #Playing and Queueing Audio
    if voice.is_playing():
        queuelist.append(title)
        await ctx.send(f"Added to Queue: ** {title} **")
    else:
        voice.play(discord.FFmpegPCMAudio(f"{title}.mp3"), after = lambda e : check_queue())
        await ctx.send(f"Playing ** {title} ** :musical_note:")
        filestodelete.append(title)
        await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = title))
 
    #the after function that gets called after the first song ends, then it checks whether a song is in the queuelist
    #if there is a song in the queuelist, it plays that song 
    #if there is no song in the queuelist, it deletes all the files in filestodelete
    def check_queue():
        try:
            if queuelist[0] != None:
                voice.play(discord.FFmpegPCMAudio(f"{queuelist[0]}.mp3"), after = lambda e : check_queue())
                coro = bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = queuelist[0]))
                fut = asyncio.run_coroutine_threadsafe(coro,bot.loop)
                fut.result()
                filestodelete.append(queuelist[0])
                queuelist.pop(0)
        except IndexError:
            for file in filestodelete:
                os.remove(f"{file}.mp3")
            filestodelete.clear()   
 
#Stop, Resume and Pause
@bot.command()
@commands.has_role("DJ")
async def pause(ctx):
    voice = ctx.voice_client
    if voice.is_playing() == True:
        voice.pause()
    else:
        await ctx.send("Bot is not playing Audio!")
 
@bot.command(aliases = ["skip"])
@commands.has_role("DJ")
async def stop(ctx):
    voice = ctx.voice_client
    if voice.is_playing() == True:
        voice.stop()
    else:
        await ctx.send("Bot is not playing Audio!")
 
@bot.command()
@commands.has_role("DJ")
async def resume(ctx):
    voice = ctx.voice_client
    if voice.is_playing() == True:
        await ctx.send("Bot is playing Audio!")
    else:
        voice.resume()
 
#function that displays the current queue
@bot.command()
async def viewqueue(ctx):
    await ctx.send(f"Queue:  ** {str(queuelist)} ** ")
 
#Error Handlers
@join.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("You have to be connected to a Voice Channel to use this command.")
    if isinstance(error, commands.errors.MissingRole):
        await ctx.send("You have to have the DJ Role to use this bot.")
 
@leave.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("Bot is not connected to a Voice Channel.")
    if isinstance(error, commands.errors.MissingRole):
        await ctx.send("You have to have the DJ Role to use this bot.")
 
@play.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("Music can't be played.")
    if isinstance(error, commands.errors.MissingRole):
        await ctx.send("You have to have the DJ Role to use this bot.")
 
@stop.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("Bot is not connected to a Voice Channel.")
    if isinstance(error, commands.errors.MissingRole):
        await ctx.send("You have to have the DJ Role to use this bot.")
 
@resume.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("Bot is not connected to a Voice Channel.")
    if isinstance(error, commands.errors.MissingRole):
        await ctx.send("You have to have the DJ Role to use this bot.")
 
@pause.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("Bot is not connected to a Voice Channel.")
    if isinstance(error, commands.errors.MissingRole):
        await ctx.send("You have to have the DJ Role to use this bot.")
 
bot.run("OTM1MDI2ODQ5OTU5MDE0NDcx.Ye4pnA.ju77dc_WeA5jYdE8tR8ufdj-j9A")