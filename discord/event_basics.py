from email import message
import discord
intents = discord.Intents.all()
bot = discord.Client(intents = intents)

@bot.event
async def on_ready():
    print("Bot is Online")

@bot.event
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    else:
        if msg.content == "Hello":
            await msg.channel.send("Hello" + " " + username)
            
@bot.event
async def on_member_join(member):
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f"Welcome to {guildname}!")
    
@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    member = payload.member
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)
    
    if emoji == "🕸️" and message_id == 935044162041053184:
        role = discord.utils.get(guild.roles, name = "Marvel Fan")
        await member.add_roles(role)
        
    if emoji == "🦇" and message_id == 935044211407994920:
        role = discord.utils.get(guild.roles, name = "DC Fan")
        await member.add_roles(role)
        
@bot.event
async def on_raw_reaction_remove(payload):
    user_id = payload.user_id
    emoji = payload.emoji.name
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)
    member = guild.get_member(user_id)
    
    if emoji == "🕸️" and message_id == 935044162041053184:
        role = discord.utils.get(guild.roles, name = "Marvel Fan")
        await member.remove_roles(role)
        
    if emoji == "🦇" and message_id == 935044211407994920:
        role = discord.utils.get(guild.roles, name = "DC Fan")
        await member.remove_roles(role)

bot.run("TOKEN")