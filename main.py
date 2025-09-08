import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot online as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("👋 Hello! Welcome to the server.")

bot.run(os.getenv("TOKEN"))
