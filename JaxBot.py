#!/usr/bin/env python
import json
import random
import sys
import os

import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

commandUsage = dict()
serotoninPictures = []


def getSerotonin():
    global serotoninPath
    for path, subdirs, files, in os.walk(serotoninPath):
        for name in files:
            serotoninPictures.append(name)
    print(f'Got {len(serotoninPictures)} serotonin pictures')


async def sendSerotonin(message, amt=1):
    picturePath = random.choice(serotoninPictures)
    await message.channel.send(file=discord.File(serotoninPath + '\\' + picturePath))


async def addImage(message):
    addedImages = 0
    for attachment in message.attachments:
        ext = attachment.filename.split('.')[-1].lower()
        if ext in {"jpg", "png"}:
            savePath = serotoninPath + '\\' + \
                str(len(serotoninPictures)) + '.' + ext
            print(f'Saving image at {savePath}')
            await attachment.save(savePath)
            addedImages = addedImages + 1
    await message.channel.send("Added " + str(addedImages) + " picture" if addedImages == 1 else " pictures")


@client.event
async def on_ready():
    sysPath = sys.path[0]
    global serotoninPath
    serotoninPath = sysPath + '\serotonin'
    getSerotonin()
    print(f'bork')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    potentialCommand = message.content.split()[0]
    if(potentialCommand[0] == "!"):
        if(potentialCommand not in commandUsage):
            commandUsage[potentialCommand] = 0
        commandUsage[potentialCommand] = commandUsage[potentialCommand] + 1
    else:
        return

    async with message.channel.typing():
        if "!SEROTONIN" == potentialCommand:
            await sendSerotonin(message, 2)

        command = potentialCommand.lower()

        if "!speak" == command:
            await message.channel.send("Bork")

        if "!serotonin" == command:
            await sendSerotonin(message)

        if "!brain" == command:
            if len(message.attachments) > 0:
                await addImage(message)
            else:
                await message.channel.send("No images given")

        if "!help" == command:
            await message.channel.send("!speak: Bork\n!serotonin: Child picture\n!brain: Adds attached images to serotonin\n!sleep: Stops Jax")

        if "!sleep" == command:
            await message.channel.send("zzz")
            print(commandUsage)
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
