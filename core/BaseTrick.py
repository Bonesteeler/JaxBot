from abc import ABC, abstractmethod, abstractproperty
import abc


class BaseTrick(ABC):

    @abc.abstractproperty
    def tricks(self):
        return []

    @abc.abstractproperty
    def caseSensitiveTricks(self):
        return []

    @abc.abstractproperty
    def help(self):
        return []

    @abc.abstractmethod
    def onReady(self):
        pass
