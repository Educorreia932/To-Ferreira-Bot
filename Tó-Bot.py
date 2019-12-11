import collections
import discord
import requests

from discord.ext import commands
from extract import excel

bot = commands.Bot(command_prefix='$')
token_file = "token.txt"

with open(token_file) as f:
        TOKEN = f.read()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

    # give info about you here
    embed.add_field(name = "Author", value = "Skelozard")

    # Shows the number of servers the bot is member of.
    embed.add_field(name = "Server count", value = f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name = "Invite", value = "[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed = embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "Tó Ferreira", description = "A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name = "$stats", value = "Gives stats about messages/emojis", inline = False)
    embed.add_field(name = "$info", value = "Gives a little info about the bot", inline=False)
    embed.add_field(name = "$help", value = "Gives this message", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def stats(ctx, mode):  
    print("Retrieving stats...")
    channel = bot.get_channel(615941696072450055)
    counter = 1
    
    msg = "Modo incorreto, vai para Campo Alegre rapaz."
    
    if mode == "messages":
        users = {}
        msg = "**Number of messages per author:**\n"
        
        async for message in channel.history(limit = 50000):
            if (message.author.name not in users):
                users[message.author.name] = 1
            
            else:
                users[message.author.name] += 1
            
        sorted_users = sorted(users.items(), key=lambda kv: kv[1], reverse = True)
        users = collections.OrderedDict(sorted_users)
            
        for user in users:
            msg += str(counter) + "º) " + user + ": " + str(users[user]) + "\n"
            counter += 1
            
    if mode == "emojis":
        emojis = {i : 0 for i in bot.emojis}
        emojis["👌"] = 0
        emojis["❤"] = 0
        emojis["🤔"] = 0
        emojis["💦"] = 0
        emojis["👍"] = 0
        
        msg = "**Number of times that each emoji was used\n**"
        
        async for message in channel.history(limit = 50000):
            for reaction in message.reactions:
                for n in range(reaction.count):
                    try:
                        emojis[reaction.emoji] += 1
                    except:
                        continue                        

        sorted_emojis = sorted(emojis.items(), key=lambda kv: kv[1], reverse = True)
        emojis = collections.OrderedDict(sorted_emojis)

        for emoji in emojis:    
            msg += str(counter) + "º) " + str(emoji) + " : " + str(emojis[emoji]) + "\n"
            counter += 1
            
    print("Stats completed!")
            
    await ctx.send(msg)
    
@bot.command()
async def ementa(ctx, school):
    print("Retrieving menu...")
    
    if school == "FMUP":
        url = "https://sigarra.up.pt/sasup/pt/web_gessi_docs.download_file?p_name=F-895735909/Plano%20Ementas_Cant%20S.%20Jo%E3o_%20DEZ%20[20112019].pdf"
    
    elif school == "FEUP":
        url = "https://sigarra.up.pt/sasup/pt/web_gessi_docs.download_file?p_name=F-249413138/Ementas%20de%2009-12%20a%2005-01-2020%20Engenharia_validada.pdf"
        
    else:
        await ctx.send("Modo incorreto, vai para Campo Alegre rapaz.")
    
    r = requests.get(url)
    open("output.pdf", 'wb').write(r.content)
        
    # await ctx.send(extract("output.pdf"))
    
    await ctx.send("```\n" + excel() + "\n```")
    
    print("Menu completed!")
    
bot.run(TOKEN)
