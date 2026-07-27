#the libraries
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

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
    await ctx.send("I'm working i think e e e ee eeee")
@bot.command()
async def bluey(ctx):
    await ctx.send("Bluey's the goat")

#this runs the bot if it is executed in this file
if __name__ == "__main__":
    bot.run(TOKEN)