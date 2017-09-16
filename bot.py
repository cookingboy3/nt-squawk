import logging
import discord
import asyncio

"""
heyo boys

nt-squawk discord bot
v1.0.0 - last edit dated 9/14/17

bot intent:
 1. push out administrator issued messages, following a standard format.
   1-1. authenticate users
   1-2. allow users to interact with the bot
   1-3. assemble a message out of user input
"""
token = "MzU4MTE4NTEwNjQxMDIwOTI5.DJzzZg.20DF-LfBy-nj2sKNGFz0FXi8Tyo"


# set up logging to file - will dump logs to nt-squawk.log in the same folder as bot.py
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)  # debug is far too much info for one man to handle.
handler = logging.FileHandler(filename='nt-squawk.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# start bot code
client = discord.Client()


class TestClass:
    admindeclared = False
    the_admin = None


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!suicide'):
        await client.send_message(message.channel, 'night')
        logger.info(f"heya, {message.author} told the bot to kill itself.")
        await client.logout()
    elif message.content.startswith('!undeadmin'):
        if not TestClass.admindeclared:
            TestClass.the_admin = message.author
            TestClass.admindeclared = True
            await client.send_message(message.channel, f'added admin: {TestClass.the_admin}')
            await client.send_message(message.channel, 'proud of you')
        elif message.author == TestClass.the_admin:
            await client.send_message(message.channel, 'you\'re already the admin buddy')
        else:
            await client.send_message(message.channel, 'not gonna happen punk')
    elif message.content.startswith('!tard'):
        await client.send_message(message.channel, '!undeadmin')

client.run(token)
