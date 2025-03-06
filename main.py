import discord
from discord.ext import commands

# Set your bot's prefix here
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True
intents.message_content = True  # Required for reading message content

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    """Responds with a hello message."""
    await ctx.send(f'Hello {ctx.author.mention}!')

@bot.command()
async def ping(ctx):
    """Responds with bot latency."""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Latency is {latency}ms.')

@bot.command()
async def say(ctx, *, message):
    """Repeats the message sent by the user."""
    await ctx.send(message)

# Run the bot
bot.run('MTMyODIwMjExOTA3Mjg0MTc0OA.G_b73_.ZP7I0v43iH7CAEOhTsckBMdpFxz5cpM5KVNq48')  # Replace 'token_here' with your actual bot token
