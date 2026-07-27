import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Snas's bot is ready.")

@bot.command()
async def are_you_working(ctx):
    await ctx.send("I'm working i think e e e ee eeee")

@bot.command()
async def bluey(ctx):
    await ctx.send("Bluey's the goat")

if __name__ == "__main__":
    bot.run(TOKEN)