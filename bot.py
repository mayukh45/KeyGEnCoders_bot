import discord
import os
from checks import is_int
from discord.ext.commands import Bot
from discord.ext import commands


roles = []
guilds = []


bot = Bot(command_prefix="#")
#print(discord.version_info)



@bot.event
async def on_message(message):
    #bot.get_command(beep)
    await bot.process_commands(message)
    #print(type(bot.messages))



@bot.event
async def on_ready():
    global roles
    guild = bot.guilds

    guild = guild[0]
    roles = guild.roles

    all = bot.get_all_members()
    for member in all:
        if member.top_role.is_default():
            if type(member.dm_channel) == None:
                await member.create_dm()
                dmchannel = member.dm_channel
                print(member.name)
               # await dmchannel.send("Hey Warrior, It seems no roles is assigned to you!")
               # await dmchannel.send("Can you please provide your passout year?")


@bot.command()
async def add_role(ctx, arg):
    global guilds
    global roles
    f = False
    for i in range (len(roles)):
        if roles[i].name == arg:
            f = True
            break

    if f:
        auth = ctx.message.author
        print("lol")
        print(roles[i])
        args = []
        args.append(roles[i])
        await auth.add_roles(*args)
        await ctx.send("Role added!")
    else :
        await ctx.send("Oops there are no such roles now, Please contact any admin for assistance")



@bot.event
async def on_member_join(member):
    await member.create_dm()

    dmchannel = member.dm_channel
    await dmchannel.send("Welcome warrior!, Welcome to KeyGEnCoders Server!")
    await dmchannel.send("Type #add_role 'Your passout year' to get started :)")



bot.run(os.getenv('TOKEN'))
