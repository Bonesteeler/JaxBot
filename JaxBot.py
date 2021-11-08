#!/usr/bin/env python
import json
import random
import sys
import os

import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

serotoninPath = '\serotonin'

serotoninPictures = []

def getSerotonin():
    print(sys.path[0])
    for path, subdirs, files, in os.walk(sys.path[0] + serotoninPath):
        for name in files:
            serotoninPictures.append(name)
    print(f'Got {len(serotoninPictures)} serotonin pictures')

async def sendSerotonin(message, amt = 1):
    picturePath = random.choice(serotoninPictures)
    await message.channel.send(file=discord.File(sys.path[0] + serotoninPath + '\\' + picturePath))
    
@client.event
async def on_ready():
    getSerotonin()
    print(f'bork')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if "!SEROTONIN" in message.content:
        await sendSerotonin(message, 9)
        
    messageLower = message.content.lower()

    if "!speak" in messageLower:
        await message.channel.send("Bork")
        
    if "!serotonin" in messageLower:
        await sendSerotonin(message)
      
        
    if "!sleep" in messageLower:
        await message.channel.send("zzz")
        exit()
    
def getSecrets():
    secretsFile = open('secrets.json',)
    secrets = json.load(secretsFile)
    global token
    token = secrets['token']
    secretsFile.close()
    
if __name__ == "__main__":
    global token
    getSecrets()
    client.run(token)