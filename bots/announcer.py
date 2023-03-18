#CONFIG (Main)


channelid = 12345678910 #Channel it sends the announcement to
bottoken = "bot token here" #token to run the bot
prefix = "." #prefix for the bot (example if it was . the command would be .announce)
embedcolor = 0x1f67cf #default color for announcements

#CODE

import nextcord
from nextcord import Intents, Activity, Embed
from nextcord.ext import commands

from colorama import Fore


intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=prefix, intents=intents, status=nextcord.Status.dnd)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print(f"Invite For Your Bot: {Fore.BLUE}https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=51200&scope=bot%20applications.commands{Fore.WHITE}")

@client.command()
async def announce(ctx, title, msg):
    try:
        embed = nextcord.Embed(title=title,description=msg, color=embedcolor)
        channel = await ctx.guild.fetch_channel(channelid)
        await channel.send(embed=embed)
        await ctx.send("Message Sent!")
    except:
        print('Failed To Send Message (lack of permissions)')
        return
        
@client.slash_command()
async def announce(ctx, title, msg):
    try:
        embed = nextcord.Embed(title=title,description=msg, color=embedcolor)
        channel = await ctx.guild.fetch_channel(channelid)
        await channel.send(embed=embed)
        await ctx.send("Message Sent!",ephemeral=True)
    except:
        print('Failed To Send Message (lack of permissions)')
    

client.run(bottoken)
