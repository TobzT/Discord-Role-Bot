import discord
from discord.ext.commands import Bot
import os
import sys
import dotenv
intents = discord.Intents.default()
intents.message_content = True
bot = Bot(intents=intents, command_prefix="ab!")

def formatEmoji(emoji):
    if("<" in str(emoji)):
        emoji = str(emoji)
        start = int(emoji.find(":"))
        end = int(emoji.find(':', start + 1)) + 1
        # print(f"start: {start}, end: {end}")
        return emoji[start:end]
    return emoji

def formatOptions(ctx, list):
    output = []
    for emoji in list:
        print(emoji)
        if(":" not in emoji):
            output.append(emoji)
        else:
            # format :owenPog: to <:owenPog:1052257596549111879> and add to output
            emoji = discord.utils.get(ctx.guild.emojis, name=emoji[1:-1])
            output.append(str(emoji))

    return output

@bot.event
async def on_ready():
    # SERVER_NAME = os.getenv("SERVER_NAME")
    # for guild in bot.guilds:
    #     if(guild.name == SERVER_NAME):
    #         print(f"- {guild.id} (name: {guild.name})")
    #         break;
    
    CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

    # print(CHANNEL_ID)

    channel = bot.get_channel(CHANNEL_ID)

    await channel.send("test")

@bot.command()
async def roles(ctx):

    ROLES = os.getenv("ROLES")
    dictionary = dict((x.strip(), y.strip())
             for x, y in (element.split('-')
             for element in ROLES.split(', ')))
    print(dictionary)

    def check(reaction, user):
        emoji = reaction.emoji
        emoji = formatEmoji(str(emoji))
        return user == user and emoji in dictionary.keys()

    possible_roles = formatOptions(ctx, dictionary.keys())
    string = ""
    MESSAGE = os.getenv("MESSAGE")
    await ctx.send(f"{MESSAGE} \n Possible roles: {string}{string.join(possible_roles)}")  # Message to react to
    while True:
        reaction = await bot.wait_for("reaction_add", check=check)  # Wait for a reaction
        if reaction:
            emoji = str(reaction[0])
            emoji = formatEmoji(emoji)
            roleName = dictionary[emoji]
            await assign_role(ctx, reaction, roleName)
    

@discord.ext.commands.has_role("OG")
async def assign_role(ctx, reaction, roleName):
    member = reaction[1]
    print(f"member: {member}")
    role = discord.utils.get(ctx.guild.roles, name=roleName)
    print(f"role: {role}")
    await member.add_roles(role)
    

dotenv.load_dotenv(os.getcwd() + "/config.env")
TOKEN = os.getenv('BOT_TOKEN')
bot.run(TOKEN)