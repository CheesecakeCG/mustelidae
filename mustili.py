import discord
import asyncio
import os


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    has_followed = False

@client.event
async def on_message(message):
    if message.content.startswith('Hello'):
       await client.send_message(message.channel, 'What\'s up!')
    if message.content.startswith('It\'s alive!'):
       await client.send_message(message.channel, 'What?')
       await client.send_message(message.channel, 'I\'m not alive...')
    if message.content.startswith('Whos here?'):
       print( discord.get_all_messages() )
       await discord.send_message(message.channel, client.get_all_messages())

    if message.content.startswith('Otters be gone!'):
       await client.send_message(message.channel, 'Later! OwO')
       quit()


client.run('MzY3ODE1MjQwMzI4NDEzMTg0.DMA6tw.pV1-lbe9Hz3xU_YdtyVLde9j5kE')
