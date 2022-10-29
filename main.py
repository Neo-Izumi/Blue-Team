from os import getenv

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents = intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
   
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}. How old are you? {member.name}'
    )
    
@client.command(name = 'hello', description = 'Greetings')
async def hello(ctx):
    await ctx.send('hello i\'m a bot!')

# @client.event
# async def on_message(message):
#     if message.author == client.user: 
#         return 
#     if '!' not in message.content:
#         await message.channel.send(f'You can type \'!\' to see sugesstions.')  

@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

client.run(TOKEN)