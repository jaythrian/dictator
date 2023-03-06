import discord
import random

client = discord.Client()
dictaterPath = 'data/dictater.png'

@client.event
async def on_ready():
    print("I am logged in as DicTater")


@client.event
async def on_message(message):
    send = [1,2,3]
    flatter = [
        'Thank you for your praise, you have served this server well',
        'You peasant, you are too weak to be considered a memeber of this server, to the gulag with you',
    ]
    rant = [
        'Eleminate the Middle Class',
        'I shall rule forever',
        'I am the highest power in the world and everyone will learn their place beneath me',
        'The courts have no authority over me!',
    ]

    if message.author == client.user:
        return

    if message.content.startswith('$flatter'):
        await message.channel.send(random.choice(flatter))

    if message.content.startswith('$propoganda'):
        for x in send:
            await message.channel.send(file=discord.File(data))

    if message.content.startswith('$rant'):
        await message.channel.send(random.choice(rant))

    



































client.run('NjE5MzUxOTgwNjg2NDQyNTE3.Xr8kuA.ynhktOkYGsnl_Z1WLbkenyx_ZE0')
