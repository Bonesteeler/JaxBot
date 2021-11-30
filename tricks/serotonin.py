import os
import random
import sys
import discord
from core.BaseTrick import BaseTrick


class Serotonin(BaseTrick):
    serotoninPath = ""
    serotoninPictures = []
    serotoninQueue = []

    def __init__(self):
        return

    def caseSensitiveTricks(self):
        return {"!SEROTONIN": self.sendLotsSerotonin}

    def tricks(self):
        return {"!serotonin": self.sendSerotonin, "!brain": self.addImage}

    def help(self):
        return {"!serotonin": "Child picture", "!brain": "Adds attached images to serotonin"}

    def onReady(self):
        self.serotoninPath = sys.path[0] + '\pictures\serotonin'
        for path, subdirs, files, in os.walk(self.serotoninPath):
            for name in files:
                self.serotoninPictures.append(name)
        print(f'Got {len(self.serotoninPictures)} serotonin pictures')

    def randomizeImages(self):
        print("Reshuffling pictures")
        imageIndices = list(range(0, len(self.serotoninPictures)))
        random.shuffle(imageIndices)
        for index in imageIndices:
            self.serotoninQueue.append(self.serotoninPictures[index])

    async def sendSerotonin(self, message: discord.message, amt=1):
        for i in range(0, amt):
            if(len(self.serotoninQueue) == 0):
                self.randomizeImages()
            pictureName = self.serotoninQueue.pop(0)
            await message.channel.send(file=discord.File(self.serotoninPath + '\\' + pictureName))

    async def sendLotsSerotonin(self, message: discord.message):
        await self.sendSerotonin(message, 2)

    async def addImage(self, message: discord.message):
        if len(message.attachments) == 0:
            await message.channel.send("No images given")
            return
        addedImages: int = 0
        for attachment in message.attachments:
            ext = attachment.filename.split('.')[-1].lower()
            if ext in {"jpg", "png"}:
                savePath = self.serotoninPath + '\\' + \
                    str(len(self.serotoninPictures)) + '.' + ext
                self.serotoninPictures.append(savePath)
                self.serotoninQueue.append(savePath)
                print(f'Saving image at {savePath}')
                await attachment.save(savePath)
                addedImages = addedImages + 1

        await message.channel.send("Added " + str(addedImages) + (" picture" if addedImages == 1 else " pictures"))

    pass
