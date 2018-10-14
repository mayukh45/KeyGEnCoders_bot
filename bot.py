import discord
import os
import json

from discord.ext.commands import Bot
from checks import is_year
from discord.ext import commands

colours = []
roles = []
guild = None
members = []
desc = '''A bot made by server admins to manage KeyGEnCoders discussion Server'''
bot = Bot(command_prefix=["!"],description=desc)


def get_colours():
    f = open("colour.json",'r')
    c = json.loads(f.read())
    for i in range(1,6):
        h,s,v = tuple(c[str(i)])
        colours.append(discord.Colour.from_hsv(h,s,v))

get_colours()
@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.event
async def on_ready():

    global roles
    global guild
    guild = bot.guilds

    guild = guild[0]
    roles = guild.roles
    
    #for role in roles:
      #  if is_year(role.name) and rol:
      #      colours.append(role.colour)

    game = discord.Game(name="Judgement Day")
    await bot.change_presence(status=discord.Status.idle,activity=game)
    all = bot.get_all_members()
    for member in all:
        if member.top_role.is_default():
            if member.dm_channel is None:
                await member.create_dm()
                dmchannel = member.dm_channel
                print(member.name)
                await dmchannel.send("Hey Warrior, It seems no roles is assigned to you!")
                await dmchannel.send("Type !setyear 'Your passout year' to get your role! :)")


@bot.command()
async def setyear(ctx, arg):
    """ Sets your passout year as a role """
    global guilds
    global roles
    f = False
   #get_colours()

    auth = ctx.message.author
    id = auth.id
    auth = guild.get_member(id)

    if is_year(arg):
        for i in range(len(roles)):
            if roles[i].name == arg:
                f = True
                break

        year_added = any(is_year(role.name) for role in auth.roles)
        if f:


            if year_added:

                await ctx.send(" You already have a role assigned to you! If you want to change it contact an admin :)")


            else:
                args = []
                args.append(roles[i])
                await auth.add_roles(*args)
                await ctx.send(" Year added!")
        else:

            await ctx.send(" Oops there are no such roles now, Please contact any admin for assistance")

    else:
        await ctx.send("The correct format is !setyear YYYY ")


@bot.command()
async def setcurr(ctx,arg):
    """ Yearly update of colour (Only for admins)"""
    global colours
    print(colours)
    if is_year(arg):
        arg = int(arg)
    else:
        await ctx.send("The correct format is !setcurr YYYY ")

    auth = ctx.message.author
    id = auth.id
    auth = guild.get_member(id)
    if auth.top_role.name!="admin":
        await ctx.send("You dont have permissions to use this command")
    else:
        for role in roles:
            if is_year(role.name):
                if int(role.name) < arg:
                    await role.edit(colour=colours[4])

                else:
                    await role.edit(colour=colours[3-arg-int(role.name)])


@bot.event
async def on_member_join(member):
    await member.create_dm()

    dmchannel = member.dm_channel


    await dmchannel.send("Welcome {0.mention}!, Welcome to KeyGEnCoders Server!".format(member))
    await dmchannel.send("Type !setyear 'Your passout year' to get started :)")



bot.run(os.getenv('TOKEN'))
