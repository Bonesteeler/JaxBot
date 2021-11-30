#!/usr/bin/env python
from collections import OrderedDict
from core.InputHandler import *
import json

import discord

from tricks.serotonin import Serotonin

intents = discord.Intents.all()
client = discord.Client(intents=intents)

commandUsage = dict()
commands = dict()
caseSensitiveCommands = dict()
helpCommand = dict()
helpString = ""
tricks = []


@client.event
async def on_ready():
    print(f'bork')


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    input = Input(message.content)
    if not input.isValidCommand:
        return

    await message.channel.trigger_typing()

    if input.caseSensitiveCommand in caseSensitiveCommands:
        recordCommand(input.caseSensitiveCommand)
        await caseSensitiveCommands[input.caseSensitiveCommand](message)
    elif input.command in commands:
        recordCommand(input.command)
        await commands[input.command](message)

    command = input.command.lower()

    if "!speak" == command:
        await message.channel.send("Bork")

    if "!help" == command:

        await message.channel.send(helpString)

    if "!sleep" == command:
        await message.channel.send("zzz")
        print(commandUsage)
        exit()


def recordCommand(command):
    if(command not in commandUsage):
        commandUsage[command] = 0
    commandUsage[command] = commandUsage[command] + 1


def getSecrets():
    secretsFile = open('secrets.json',)
    secrets = json.load(secretsFile)
    global token
    token = secrets['token']
    secretsFile.close()


if __name__ == "__main__":
    global token
    getSecrets()
    tricks.append(Serotonin())
    for trick in tricks:
        commands.update(trick.tricks())
        caseSensitiveCommands.update(trick.caseSensitiveTricks())
        helpCommand.update(trick.help())
        trick.onReady()
    helpKeys = sorted(helpCommand.keys())
    for key in helpKeys:
        helpString = helpString + key + ":" + helpCommand[key] + "\n"
    client.run(token)
