import discord
import os
from discord.ext.commands import Bot
from checks import is_int
from discord.ext import commands

roles = []
guild = None
members = []
bot = Bot(command_prefix="#")


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

    all = bot.get_all_members()
    for member in all:
        if member.top_role.is_default():
            if member.dm_channel is None:
                await member.create_dm()
                dmchannel = member.dm_channel
                print(member.name)
                await dmchannel.send("Hey Warrior, It seems no roles is assigned to you!")
                await dmchannel.send("Type #add_role 'Your passout year' to get your role! :)")


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
        id = auth.id
        auth = guild.get_member(id)
        if len(auth.roles)>1:
            await ctx.trigger_typing()
            await ctx.send("You already have a role assigned to you!, If you want to change it contact an admin :)")
            
                
        else:
            args = []
            args.append(roles[i])
            await auth.add_roles(*args)
            await ctx.send("Role added!")
    else :
        await ctx.trigger_typing()
        await ctx.send("Oops there are no such roles now, Please contact any admin for assistance")


@bot.event
async def on_member_join(member):
    await member.create_dm()

    dmchannel = member.dm_channel

    await dmchannel.trigger_typing()
    await dmchannel.send("Welcome warrior!, Welcome to KeyGEnCoders Server!")
    await dmchannel.send("Type #add_role 'Your passout year' to get started :)")



bot.run(os.getenv('TOKEN'))
