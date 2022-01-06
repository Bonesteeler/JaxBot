from core.BaseTrick import BaseTrick


class ErrorTrick(BaseTrick):

    def __init__(self):
        return

    def caseSensitiveTricks(self):
        return {}

    def tricks(self):
        return {"!error": self.throwException}

    def help(self):
        return {}

    def onReady(self):
        return

    def throwException(self):
        raise Exception()
