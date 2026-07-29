#the libraries
import asyncio
import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import random

#this is to use the .env file that has the discord token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#this loads the discord default permissions
intents = discord.Intents.default()
#this makes it so the bot can read messages
intents.message_content = True
#this makes it so the bot can read the users of the members
intents.members = True

bot = commands.Bot(command_prefix="", intents=intents)

#this executes the code when the bot is ready
@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Snas's bot is ready.")

#this executes the code when a new member joins
@bot.event
async def on_member_join(member): #this function welcomes new members
    channel_name = "welcomes-bienvenidas"

    channel = discord.utils.get(member.guild.text_channels, name=channel_name)

    if channel:
        await channel.send(f"sup {member.mention}. welcome to the server / Buenas {member.mention}. bienvenido al server")

#these are the commands
@bot.tree.command(name="are_you_working", description="asks Snas if he is working well")
async def are_you_working(interaction: discord.Interaction): #this function prints a little fact, nothing interesting
    """asks Snas if he is working well"""
    await interaction.response.send_message("I'm working i think e e e ee eeee")

@bot.tree.command(name="estas_funcionando", description="asks Snas if he is working well")
async def estas_funcionando(interaction: discord.Interaction): #this function prints a little fact too
    """preguntarle a Snas si funciona bien"""
    await interaction.response.send_message("creo que estoy funcionando si te estoy respondiendo e e e ee eeee")

@bot.tree.command(name="bluey", description="gives Snas's opinion on Bluey")
async def bluey(interaction: discord.Interaction): #this function prints a little fact x3
    """gives Snas's opinion on Bluey"""
    await interaction.response.send_message("Bluey's the goat")

@bot.tree.command(name="how_is_your_day", description="asks Snas about his day")
async def how_is_your_day(interaction: discord.Interaction): #this function prints a little fact x4
    """asks Snas about his day"""
    await interaction.response.send_message("my day for now is SANSacional")

@bot.tree.command(name="como_va_tu_dia", description="le pregunta a Snas como va su día")
async def como_va_tu_dia(interaction: discord.Interaction): #this function prints a little fact x5
    """le pregunta a Snas como va su día"""
    await interaction.response.send_message("por ahora mi día es SANSacional")

@bot.tree.command(name="tell_me_a_joke", description="Snas tells you a joke")
async def tell_me_a_joke(interaction: discord.Interaction): #this function prints a random joke from 3 available
    """Snas tells you a joke"""
    await interaction.response.defer() #this makes discord wait for the responses of the bot
    random_joke = random.randint(1, 3)
    if random_joke == 1:
        await interaction.followup.send("knock knock")
        await asyncio.sleep(2)
        await interaction.followup.send("'who's there'")
        await asyncio.sleep(2)
        await interaction.followup.send("mustache")
        await asyncio.sleep(2)
        await interaction.followup.send("'mustache who?'")
        await asyncio.sleep(2)
        await interaction.followup.send("i mustache you a question, but i'll shave it for later")
    elif random_joke == 2:
        await interaction.followup.send("come on i've gotten a ton of work done today. a skele-ton")
    elif random_joke == 3:
        await interaction.followup.send("knock knock")
        await asyncio.sleep(2)
        await interaction.followup.send("'who's there'")
        await asyncio.sleep(2)
        await interaction.followup.send("dishes")
        await asyncio.sleep(2)
        await interaction.followup.send("'dishes who?'")
        await asyncio.sleep(2)
        await interaction.followup.send("dishes a very bad joke")

@bot.tree.command(name="cuentame_un_chiste", description="Snas te cuenta un chiste (en español)")
async def cuentame_un_chiste(interaction: discord.Interaction): #this function prints a random joke from 3 available but in Spanish
    await interaction.response.defer()
    random_joke = random.randint(1, 3)
    if random_joke == 1:
        await interaction.followup.send("knock knock")
        await asyncio.sleep(2)
        await interaction.followup.send("'Quien es?'")
        await asyncio.sleep(2)
        await interaction.followup.send("Calcio")
        await asyncio.sleep(2)
        await interaction.followup.send("'Calcio que?'")
        await asyncio.sleep(2)
        await interaction.followup.send("Calcioualidad que justo te encontré por aquí")

    elif random_joke == 2:
        await interaction.followup.send("todos me preguntan cuál es el trabajo ideal para un esqueleto flojo")
        await asyncio.sleep(2)
        await interaction.followup.send("ser modelo de radiografías, te pagan por quedarte quieto y no tienes ni que peinarte.")

    elif random_joke == 3:
        await interaction.followup.send("'cuanto es 2+2'")
        await asyncio.sleep(2)
        await interaction.followup.send("no se")
        await asyncio.sleep(2)
        await interaction.followup.send("'como no sabes?'")
        await asyncio.sleep(2)
        await interaction.followup.send("esque soy un cabeza hueca")

@bot.tree.command(name="how_many_genders_exist", description="asks Snas how many genders exist")
async def how_many_genders_exist(interaction: discord.Interaction): #this function prints a little fact x6
    await interaction.response.send_message("I'm pretty sure that there are only 2 genders, male and female")

@bot.tree.command(name="cuantos_generos_hay", description="le pregunta a Snas cuantos generos existen")
async def cuantos_generos_hay(interaction: discord.Interaction): #this function prints a little fact x7
    await interaction.response.send_message("por lo que se solo hay 2 generos, hombre y mujer")

@bot.tree.command(name="recomendar_juego", description="sirve para recomendar un juego")
@app_commands.describe(
    title="nombre del juego",
    description="descripción del juego",
    url="url del juego",
    image="imagen del juego"
)
async def recomendar_juego( #this command creates an embed (something like a post) where you can put a title, a description, an url and an image to recommend a game to other people
        interaction: discord.Interaction,
        title:str,
        description:str,
        url:str,
        image:discord.Attachment):

    embed = discord.Embed(title=title, description=description, color=discord.Color.green())
    embed.add_field(name="url", value=url, inline=False)
    if image:
       
        if image.content_type and image.content_type.startswith("image/"): #if the image is an image then
            embed.set_image(url=image)
        else:
            await interaction.response.send_message(
                "archivo invalido",
                ephemeral=True #this is to make the message private
            )
            return
    await interaction.response.send_message(embed=embed)

#this runs the bot if it is executed in this file
if __name__ == "__main__":
    bot.run(TOKEN)