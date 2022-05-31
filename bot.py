# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} has connected to Discord!')
    print(f'{client.user} is connected to: 'f'{guild.name}\n')
    print('(ID: 'f'{guild.id})')
    # members = '\n-'.join(member.name for member in guild.members)
    # count = guild.member_count
    # print('Member List:\n -' f'{members}' '\nA total of: ' f'{count}' '.')

@client.event
async def on_member_update(before, after):
    channel = client.get_channel(719574895805071450)
    reaction = f'{after.name}'' just turned 'f'{after.status}''.'
    await client.wait_until_ready()
    if before.status != after.status:
        await channel.send(reaction) 
 
@client.command()
async def ping(ctx):
    await ctx.send('PING PONG PENG PONG {0}'.format(round(client.latency, 3)))
    
@client.command()
async def monkey(ctx):
    await ctx.send("samuel gay")
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio("E:/bot/me/monkey.mp3"))
    await ctx.voice_client.disconnect()
    
@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
 
@client.event
async def on_message(message):
    if message.author != client.user:
        if 'pog' in message.content.lower():
            await message.channel.send(file=discord.File('E:/bot/me/pog.png'))
        if 'fisika' in message.content.lower():
            await message.channel.send(file=discord.File('E:/bot/me/geraldi.png'))
        if 'plis' in message.content.lower():
            await message.channel.send(file=discord.File('E:/bot/me/doa.png'))
        if 'hai' in message.content.lower():
            await message.channel.send(file=discord.File('E:/bot/me/hai.jpg'))
        if 'ga sengaja' in message.content.lower():
            await message.channel.send(file=discord.File('E:/bot/me/gs.jpg'))
        if message.content == 'raise-exception':
            raise discord.DiscordException
    choice = ['yes', 'no']
    choose = random.choice(choice)
    if message.author != client.user:
        if message.content.lower().startswith('should'):
            await message.channel.send(choose)
    await client.process_commands(message)
            
   

client.run(TOKEN)