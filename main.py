import nextcord

from os import getenv, listdir
from dotenv import load_dotenv
from discord_components import embed
from nextcord import Activity, ActivityType, DiscordException, Intents
from nextcord.ext.commands import Bot, when_mentioned_or, dm_only
from nextcord.ext.commands.errors import MissingPermissions, CommandNotFound, PrivateMessageOnly



load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')

intents = Intents.all()
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
async def no_self_response(ctx):
    return ctx.author != bot.user

@bot.event
async def on_command_error(ctx, e: DiscordException):
    if isinstance(e, MissingPermissions):
        await ctx.send(
            content = e,
            delete_after = 5,
        )
    elif isinstance(e, CommandNotFound):
        content = 'Please enter a proper command as the instruction!!!'
        error = embed.embed_error(content)
        await ctx.send(
            embed = error,
            delete_after = 5
        )
    elif isinstance(e, PrivateMessageOnly):
        await ctx.send(
            content = 'private message only',
            delete_after = 5
        )
    else: 
        raise e
    
@bot.command(name = 'hello', description = 'Greetings')
@dm_only()
async def hello(ctx):
    await ctx.send('hello i\'m a bot!')
    
extensions = []

for filename in listdir('./cogs'):
    if filename.endswith('.py'):
        extensions.append('cogs.' + filename[:-3])

if __name__ == '__main__':
    for ex in extensions:
        bot.load_extension(ex)

bot.run(TOKEN)

