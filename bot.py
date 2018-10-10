import discord
import os
test_id = 499296940358369280


client = discord.Client()
print(discord.version_info)



@client.event
async def on_message(message):
    print(":>")

    await client.send_message(message.channel, 'Why')

    print(type(client.messages))



@client.event
async def on_ready():

    print('Logged in as')
    print(client.guilds)
    users =  list(client.users)
    for users in users:
        print(users.name)
    print(client.get_channel(test_id))


client.run(os.getenv('TOKEN'))
