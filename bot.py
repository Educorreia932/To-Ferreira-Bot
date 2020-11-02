import discord
import requests

from discord.ext import commands
from bs4 import BeautifulSoup

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
    URL = "https://sigarra.up.pt/sasup/pt/web_base.gera_pagina?P_pagina=265689"
    university = university.upper()

    canteens = {
        "FEUP": "Cantina de Engenharia",
        "FMUP": "Cantina de S. João"
    }

    # Retrieve menu's PDF link
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, features="lxml")

    menu_anchors = soup.select("div.mobile a")

    for anchor in menu_anchors:
        canteen_name = anchor.next

        if canteen_name == canteens[university]:
            pdf_url = "https://sigarra.up.pt/sasup/pt/" + anchor["href"]

    await ctx.send(canteens[university])

bot.run(TOKEN)
