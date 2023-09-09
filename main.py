import discord
from discord.ext.commands import Bot
import os
import sys
import dotenv
dotenv.load_dotenv(os.getcwd() + "/config.env", override=True)
intents = discord.Intents.default()
intents.message_content = True
PREFIX = os.getenv("PREFIX")
bot = Bot(intents=intents, command_prefix=PREFIX)

def formatEmoji(emoji):
    if("<" in str(emoji)):
        emoji = str(emoji)
        start = int(emoji.find(":"))
        end = int(emoji.find(':', start + 1)) + 1
        return emoji[start:end]
    return emoji

def formatOptions(ctx, dict):
    output = []
    for emoji in dict:
        name = dict[emoji]
        if(":" not in emoji):
            output.append(str(emoji) + " - " + name + "\n")
        else:
            # format :owenPog: to <:owenPog:1052257596549111879> and add to output
            emoji = discord.utils.get(ctx.guild.emojis, name=emoji[1:-1])
            output.append(str(emoji) + " - " + name + "\n")

    return output

@bot.event
async def on_ready():
    print("start")

@bot.command()
async def roles(ctx):
    await ctx.message.delete()
    ROLES = os.getenv("ROLES")
    dictionary = dict((x.strip(), y.strip())
             for x, y in (element.split('-')
             for element in ROLES.split(', ')))

    def check(reaction, user):
        emoji = reaction.emoji
        emoji = formatEmoji(str(emoji))
        return user == user and emoji in dictionary.keys()

    possible_roles = formatOptions(ctx, dictionary)
    string = ""
    MESSAGE = os.getenv("MESSAGE")
    
    await ctx.send(f"{MESSAGE} \n Possible roles: \n {string}{string.join(possible_roles)}")  # Message to react to
    
    while True:
        reaction = await bot.wait_for("reaction_add", check=check)  # Wait for a reaction
        if reaction:
            emoji = str(reaction[0])
            emoji = formatEmoji(emoji)
            roleName = dictionary[emoji]
            await assign_role(ctx, reaction, roleName)
            

@bot.command()
async def reloadenv(ctx):
    await ctx.message.delete()
    dotenv.load_dotenv(os.getcwd() + "/config.env", override=True)
    
BOT_ROLE = os.getenv("BOT_ROLE")
@discord.ext.commands.has_role(BOT_ROLE)
async def assign_role(ctx, reaction, roleName):
    member = reaction[1]
    role = discord.utils.get(ctx.guild.roles, name=roleName)
    await member.add_roles(role)
    


TOKEN = os.getenv('BOT_TOKEN')
bot.run(TOKEN)