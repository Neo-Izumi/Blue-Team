import nextcord

from os import getenv, listdir
from dotenv import load_dotenv
from nextcord import Activity, ActivityType, DiscordException, Intents, Interaction
from nextcord.ext.commands import Bot, when_mentioned_or
from nextcord.ext.commands.errors import MissingPermissions


load_dotenv()
TOKEN = getenv('DISCORD_TOKEN_MAIN')
GUILD = getenv('DISCORD_GUILD')

intents = nextcord.Intents.all()
intents.members = True

bot = Bot(
        command_prefix = when_mentioned_or('!'),
        activity = Activity(
            type = ActivityType.listening,
            name = f"{'!'}help",
        ),
        intents = intents,
        strip_after_prefix = True,
    )

@bot.event
async def on_ready():
    guild = nextcord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@bot.check
async def no_dm(ctx):
    return ctx.guild or await bot.is_owner(ctx.author)

@bot.check
async def no_self_response(ctx):
    return ctx.author != bot.user

@bot.event
async def on_application_command_error(ctx, e: DiscordException):
    if isinstance(e, MissingPermissions):
        await ctx.response.send_message(
            content = e,
            ephemeral = True,
            delete_after = 10,
        )
   
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}. How old are you? {member.name}'
    )
    
@bot.command(name = 'hello', description = 'Greetings')
async def hello(ctx):
    await ctx.send('hello i\'m a bot!')
    
ID = 1035593393381838888
    
extensions = []

for filename in listdir('./cogs'):
    if filename.endswith('.py'):
        extensions.append('cogs.' + filename[:-3])

if __name__ == '__main__':
    for ex in extensions:
        bot.load_extension(ex)


bot.run(TOKEN)






#test slash_command
# @bot.slash_command(name = 'wtf', description = 'Run the test slash_command', guild_ids = [ID],)
# async def wtf(interaction: Interaction, message):
#     await interaction.response.send_message(f'you\'ve just said what? {message} ha!')
    
# @bot.slash_command(name = 'dm', description = 'Run the test slash_command', guild_ids = [ID],)
# async def dm(interaction: Interaction, message):
#     await interaction.response.send_message(f'Ok {message}!')
    
# @bot.slash_command(name = 'haha', description = 'hahahahahaha', guild_ids = [ID])
# async def haha(interaction: Interaction):
#     await interaction.response.send_message(f'Yooo what\'s up')




# shutdown bot command:
# @commands.is_owner()
# async def shutdown(ctx):
#     await ctx.bot.logout()




# action to normal messages
# @bot.event
# async def on_message(message):
#     if message.author == bot.user: 
#         return 
#     if '!' not in message.content:
#         await message.channel.send(f'You can type \'!\' to see sugesstions.')  