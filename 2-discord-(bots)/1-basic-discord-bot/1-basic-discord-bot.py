#the libraries
import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random

#this is to use the .env file that has the discord token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#this loads the discord default permissions
intents = discord.Intents.default()
#this makes it so the bot can read messages
intents.message_content = True

#this enables the bot to use the permissions and makes it so you can use commands with "!"
bot = commands.Bot(command_prefix="!", intents=intents)

#this executes the code when the bot is ready
@bot.event
async def on_ready():
    print("Snas's bot is ready.")

#these are the commands
@bot.command()
async def are_you_working(ctx):
    """asks Snas if he is working well"""
    await ctx.send("I'm working i think e e e ee eeee")
@bot.command()
async def bluey(ctx):
    """gives Snas's opinion on Bluey"""
    await ctx.send("Bluey's the goat")
@bot.command()
async def how_is_your_day(ctx):
    """asks Snas about his day"""
    await ctx.send("my day for now is SANSacional")
@bot.command()
async def tell_me_a_joke(ctx):
    """Snas tells you a joke"""
    random_joke = random.randint(1, 3)
    if random_joke == 1:
        await ctx.send("knock knock")
        await asyncio.sleep(2)
        await ctx.send("'who's there'")
        await asyncio.sleep(2)
        await ctx.send("mustache")
        await asyncio.sleep(2)
        await ctx.send("'mustache who?'")
        await asyncio.sleep(2)
        await ctx.send("i mustache you a question, but i'll shave it for later")
    elif random_joke == 2:
        await ctx.send("come on i've gotten a ton of work done today. a skele-ton")
    elif random_joke == 3:
        await ctx.send("knock knock")
        await asyncio.sleep(2)
        await ctx.send("'who's there'")
        await asyncio.sleep(2)
        await ctx.send("dishes")
        await asyncio.sleep(2)
        await ctx.send("'dishes who?'")
        await asyncio.sleep(2)
        await ctx.send("dishes a very bad joke")

#this runs the bot if it is executed in this file
if __name__ == "__main__":
    bot.run(TOKEN)