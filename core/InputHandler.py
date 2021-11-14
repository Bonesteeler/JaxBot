from posixpath import split


class Input:
    isValidCommand = False
    command = ""
    args = []

    def __init__(self, message: str):
        if message[0] != '!':
            return
        self.isValidCommand = True
        self.args = message.split()
        self.command = self.args.pop()
