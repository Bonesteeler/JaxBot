from PIL import Image
import sys
import os


def fixNames():
    imgPath = sys.path[0] + '\serotonin'
    for path, subdirs, files, in os.walk(imgPath):
        index = 0
        namePadding = '0' * len(str(len(files)))
        for name in files:
            indexStrLength = len(str(index))

            expectedName = ""
            if indexStrLength < len(namePadding):
                expectedName = namePadding[indexStrLength:]
            expectedName = expectedName + str(index) + '.' + name.split('.')[1]

            im = Image.open(imgPath + '\\' + name)

            if expectedName != name:
                print(f'{name} is {expectedName}')
                im.save(imgPath + '\\' + expectedName)
                os.remove(imgPath + '\\' + name)

            index = index + 1


if __name__ == "__main__":
    fixNames()
