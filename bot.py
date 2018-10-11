import discord
import os
from checks import is_int
roles


bot = Bot(command_prefix="#")
print(discord.version_info)



@bot.event
async def on_message(message):

    if message.content.size == 4 and is_int(message.content):
        #Have to add roles
        
        await message.channel.send("Your role is added!")

    #print(type(bot.messages))



@bot.event
async def on_ready():
    global roles
    guild = bot.guilds
    print(guild)
    guild = guild[0]
    roles = guild.roles

    all = bot.get_all_members()
    for member in all:
        if member.top_role.is_default():
            if member.dm_channel == None:
                await member.create_dm()
                dmchannel = member.dm_channel
                print(member.name)
                await dmchannel.send("Hey Warrior, It seems no roles is assigned to you!")
                await dmchannel.send("Can you please provide your passout year?")


@bot.event
async def on_member_join(member):
    await member.create_dm()
    dmchannel = member.dm_channel
    await dmchannel.send("Welcome warrior!, Can you please provide your passout year?")






bot.run(os.getenv('TOKEN'))
