import collections
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

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
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name = "$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name = "$multiply X Y", value = "Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name = "$greet", value = "Gives a nice greet message", inline=False)
    embed.add_field(name = "$cat", value = "Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name = "$info", value = "Gives a little info about the bot", inline=False)
    embed.add_field(name = "$help", value = "Gives this message", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def stats(ctx):  
    print("stats incoming")
    channel = bot.get_channel(615941696072450055)
    users = {}
    msg = "**Number of messages per author:**\n"
    counter = 1
    
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
        
    await ctx.send(msg)
    
bot.run("")
