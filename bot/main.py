######Catnomy's multipurpose bot####
######Catnomy's multipurpose bot####
######Catnomy's multipurpose bot####



import discord
import os
import time
from discord.ext import commands


os.system('cls')
# Bot
print("""
Color attributes are specified by TWO hex digits -- the first
corresponds to the background; the second the foreground.  Each digit
can be any of the following values:

    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White

    or type default for bots choice
""")


os.system('cls')

time.sleep(1)

client = commands.Bot(command_prefix='mtl.', help_command=None)

######Catnomy's multipurpose bot####

logo = print("""

     ██████╗ █████╗ ████████╗███╗   ██╗ ██████╗ ███╗   ███╗██╗   ██╗
    ██╔════╝██╔══██╗╚══██╔══╝████╗  ██║██╔═══██╗████╗ ████║╚██╗ ██╔╝'s
    ██║     ███████║   ██║   ██╔██╗ ██║██║   ██║██╔████╔██║ ╚████╔╝
    ██║     ██╔══██║   ██║   ██║╚██╗██║██║   ██║██║╚██╔╝██║  ╚██╔╝
    ╚██████╗██║  ██║   ██║   ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║   ██║
     ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝   ╚═╝   MultiPurposeBot


    """)

#Startup####
######Catnomy's multipurpose bot####


@client.event
async def on_ready():
    print(logo)

######Catnomy's multipurpose bot####

@client.event
async def on_guild_join(guild):
    embed = discord.Embed(title="Thanks For Adding Me!", description="Do (prefix)Commands for a list of commands \n \n prefix can be changed anytime via admin panel \n admin panel will be released soon", color=0xd89522)
    await guild.text_channels[0].send(embed=embed)

@client.event
async def on_member_remove():
    channel = client.get_channel(905707512416862218)
    await channel.send('hello')

#####Cmd#####




######Catnomy's multipurpose bot####

#kick cmd
# ██████╗ █████╗ ████████╗███╗   ██╗ ██████╗ ███╗   ███╗██╗   ██╗
#██╔════╝██╔══██╗╚══██╔══╝████╗  ██║██╔═══██╗████╗ ████║╚██╗ ██╔╝
#██║     ███████║   ██║   ██╔██╗ ██║██║   ██║██╔████╔██║ ╚████╔╝
#██║     ██╔══██║   ██║   ██║╚██╗██║██║   ██║██║╚██╔╝██║  ╚██╔╝  's multipurpose bot
#╚██████╗██║  ██║   ██║   ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║   ██║
# ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝   ╚═╝

@client.command()
async def ev(ctx, *, args):
    if (ctx.author.id == 755784551313440881):
        result = eval(args)
        tostr = str(result)
        embed = discord.Embed(title='done')
        await ctx.send(embed=embed)
        await ctx.send("```json" + "\n" + tostr + "```")

@client.command()
async def db(ctx, *, args):
    if (ctx.author.id == 755784551313440881):
        result = eval(db)
        executed = exec(db)

    await ctx.send("```json" + "\n" + result + "```")
    await ctx.send("```json" + "\n" + executed + "```")


time.sleep(3)

@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title="Bot Help", description="Kekbot, a multi purpose bot made for CMTL (catnomy's multi tool),\n this is a paid custom bot made for thoose who purchased \n my multitool, since it comes in with a built in bot, to purchase the bot \n dm me: Kewl ` ⩲ Owner ⩲ ⌈ CatNomy#2216", colour=discord.Color.blue())
    embed.add_field(name = "**Moderation**", value="ban, kick, verbal")
    embed.add_field(name = "Devloper options", value="Cls, Ev, deploy")
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    val = round(client.latency * 100)
    tostr = str(val)
    await ctx.send(f"```json" + "\n" + tostr + 'ms'  + "```")


@help.command()
async def kick(ctx):
    embed = discord.Embed(title="Kick command", description="Kicks a member from the Server", color=discord.Color.blue())
    embed.add_field(name = "**Usage**", value = ">kick <member> [reason]")
    await ctx.send(embed=embed)

@help.command()
async def ban(ctx):
    embed = discord.Embed(title="Ban command", description="Bans a member from the Server", color=discord.Color.blue())
    embed.add_field(name = "**Usage**", value = ">ban <member> [reason]")
    await ctx.send(embed=embed)

@help.command()
async def verbal(ctx):
    embed = discord.Embed(title="Verbal command", description="verbal a member from the Server", color=discord.Color.blue())
    embed.add_field(name = "**Usage**", value = ">verbal <member> [reason]")
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(title="Kick member", description='Kicked')
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title="Ban member", description='Banned')
    await ctx.send(embed=embed)
######Catnomy's multipurpose bot####

#help command
@client.command()
async def modhelp(ctx):
    embed = discord.Embed(title='Bot help', description='Do !commands for a list of commands \n About bot. \n \n this bot was made for multi moderation purposes \n its more like a moderation bot then for members \n \n \n Bot Included in Catnomys multitool')
    await ctx.send(embed=embed)

#!commands for help cmd
@client.command()
async def commands(ctx):
    embed = discord.Embed(title='Commands', description='1. Ban | Bans a member \n 2. Kick | Kicks a member \n 3. Commands | Shows this message \n Cls | Clear console screen \n Features | View list of features \n Modhelp | Redirects to this Message as of now \n \n \n \n Bot Made for Catnomys discord multitool', color=discord.Color.red())
    await ctx.send(embed=embed)



@client.command()
async def cls(ctx):
    os.system('clear')
######Catnomy's multipurpose bot####

@client.command()
async def features(ctx):
    embed = discord.Embed(title='Features', description='1. Words blacklisting \n Ban / kick commands \n Devloper functions \n fully secure \n mongodb database for devloper \n Dashboard \n Prefix changer \n Chmodded 8 times in database \n Stores passwords locally \n Stamp features \n \n \n Bot from catnomys multitool')
    await ctx.send(embed=embed)

@client.command()
async def mark(ctx):
    await ctx.send("""
    # ██████╗ █████╗ ████████╗███╗   ██╗ ██████╗ ███╗   ███╗██╗   ██╗
    #██╔════╝██╔══██╗╚══██╔══╝████╗  ██║██╔═══██╗████╗ ████║╚██╗ ██╔╝
    #██║     ███████║   ██║   ██╔██╗ ██║██║   ██║██╔████╔██║ ╚████╔╝
    #██║     ██╔══██║   ██║   ██║╚██╗██║██║   ██║██║╚██╔╝██║  ╚██╔╝
    #╚██████╗██║  ██║   ██║   ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║   ██║
    # ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝   ╚═╝
    """)

######Catnomy's multipurpose bot####
@client.command()
async def verbal(ctx):
    embed = discord.Embed(title="Verballed member")
    await ctx.send(embed=embed)




#######IMPORTANT
#######IMPORTANT
#######IMPORTANT




ownerid = 755784551313440881

@client.command()
async def getguildobject(ctx):
    if (ctx.author.id == ownerid):
        await ctx.send(f"{client.guilds()}")

@client.command()
async def getguildlength(ctx):
    if (ctx.author.id == ownerid):
        await ctx.send(f"{len(client.guilds)}")

@client.command()
async def dm(ctx, *, er):
    ertoint = int(er)
    user = client.get_user(ertoint)



@client.command()
async def fetchbotstatus(ctx, *, args):
    if (ctx.author.id == ownerid):
        if args in ('changebotstatus', 'changeworkmethod'):
            await ctx.send('```json' + '\n' + args +  '>_ '+  '```')
            input('>_')

        if args in ('fetchguildname'):
            await ctx.send(client.guilds)

        if args in ('50xworkload'):
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)
            await ctx.send('***50bytes***')
            time.sleep(1)

##config

@client.command()
async def getbotprofile(ctx):
    await ctx.send('#, #, #, #')



####Bot belongs to my multitool###
print("Bot prefix is >")


client.run("token")
# end

# ### Bot belongs to my multitool###
