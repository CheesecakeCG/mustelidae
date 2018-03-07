import discord
import asyncio
import os
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

soul = json.load(open('cfg/soul.json'))
clientid = json.load(open('cfg/clientid.json'))

client = discord.Client()

def create_reply(m):
	output = "My database does not contain a reply for that. Sorry!"
	choices = []
	for c in soul["responses"]:
		if fuzz.ratio(c[0], m) > 50:
			choices.append(c)

	ext = process.extractOne(m, choices)
	if ext[1] > 80:
		print( "Choices: ", choices)
		print( "ext: ", ext )
		output = ext[0][1]
	
	return output
	
@client.event
async def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print("------")
	has_followed = False

@client.event
async def on_message(message):
	print( message.content )
	if message.content.startswith("<@367815240328413184>"):
		await client.send_message(message.channel, create_reply(message.content.replace("<@367815240328413184>", "")))
	else:
		if message.content.startswith("Otters be gone!"):
			await client.send_message(message.channel, "Later! OwO")
			quit()
	   

#f = open("clientid","r")
#print(f.read())


client.run(clientid["id"])
