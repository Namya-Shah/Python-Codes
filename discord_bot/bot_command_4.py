import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.command()
async def server(ctx):
    name = ctx.guild.name
    description = ctx.guild.description
    
    owner = ctx.guild.owner
    id = ctx.guild.id
    region = ctx.guild.region
    memberCount = ctx.guild.member_count
    
    icon = ctx.guild.icon_url
    
    embed = discord.Embed(
        title=name + "Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    
    await ctx.send(embed=embed)



client.run('OTA3NTYyMTIyODg2NjcyMzk3.YYo_Fw.pKeeoRBp0fjjE1EcgFLw-g_QsXg')