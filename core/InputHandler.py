from posixpath import split


class Input:
    isValidCommand = False
    command = ""
    caseSensitiveCommand = ""
    args = []

    def __init__(self, message: str):
        if len(message) > 0 and message[0] != '!':
            return
        self.isValidCommand = True
        self.args = message.split()
        self.caseSensitiveCommand = self.args.pop()
        self.command = self.caseSensitiveCommand.lower()
