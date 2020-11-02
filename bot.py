from menu import * 

import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='$', description='Tó Ferreira Bot')

TOKEN_LOCATION = "token.txt"

with open(TOKEN_LOCATION) as token_file:
    TOKEN = token_file.read()

@bot.event
async def on_ready():
    print(f"\nDiscord.py Version: {discord.__version__}")
    print(f"Logged in as: {bot.user.name} - {bot.user.id}")

@bot.command()
async def menu(ctx, university):
    retrieve_menu_pdf(university)
    retrieve_menu_image(university)

    await ctx.send(file=discord.File("out.jpg"))

bot.run(TOKEN)
