import json
from messages import Message, MessageBody, MessageHeader


class CommandMeta(type):
    pass


class CommandHeader(MessageHeader):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, messagePurpose="commandRequest")


class CommandBody(MessageBody):
    def __init__(self, message, *args, overload='default', **kwargs):
        super().__init__(message, *args, name=type(message).__name__.lower(),
                         overload=overload, version=1, input=kwargs)


class Command(Message, metaclass=CommandMeta):
    header_class = CommandHeader
    body_class = CommandBody

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Fill(Command):
    def __init__(self,  x1, y1, z1, x2, y2, z2, tileName="air", tileData=0, oldBlockHandling="replace", replaceTileName="", replaceDataValue="", **kwargs):
        super().__init__(x1=x1,
                         y1=y1,
                         z1=z1,
                         x2=x2,
                         y2=y2,
                         z2=z2,
                         tileName=tileName,
                         tileData=tileData,
                         oldBlockHandling=oldBlockHandling,
                         replaceTileName=replaceTileName,
                         replaceDataValue=replaceDataValue,
                         **kwargs)


BLOCK_LIMIT = 65000


def ability():
    raise NotImplementedError()


def clear():
    raise NotImplementedError()


def clone():
    raise NotImplementedError()


def deop():
    raise NotImplementedError()


def difficulty():
    raise NotImplementedError()


def effect():
    raise NotImplementedError()


def enchant():
    raise NotImplementedError()


def execute():
    raise NotImplementedError()


def experience():
    raise NotImplementedError()


def gamemode():
    raise NotImplementedError()


def gamerule():
    raise NotImplementedError()


def give():
    raise NotImplementedError()


def help():
    raise NotImplementedError()


def kill():
    raise NotImplementedError()


def list():
    raise NotImplementedError()


def locate():
    raise NotImplementedError()


def me():
    raise NotImplementedError()


def mixer():
    raise NotImplementedError()


def msg():
    raise NotImplementedError()


def op():
    raise NotImplementedError()


def playsound():
    raise NotImplementedError()


def replaceitem():
    raise NotImplementedError()


def say():
    raise NotImplementedError()


def setblock():
    raise NotImplementedError()


def setmaxplayers():
    raise NotImplementedError()


def setworldspawn():
    raise NotImplementedError()


def setspawnpoint():
    raise NotImplementedError()


def spreadplayers():
    raise NotImplementedError()


def stopsound():
    raise NotImplementedError()


def summon():
    raise NotImplementedError()


def teleport():
    raise NotImplementedError()


def tell():
    raise NotImplementedError()


def testfor():
    raise NotImplementedError()


def testforblock():
    raise NotImplementedError()


def testforblocks():
    raise NotImplementedError()


def tickingarea():
    raise NotImplementedError()


def time():
    raise NotImplementedError()


def title():
    raise NotImplementedError()


def toggledownfall():
    raise NotImplementedError()


def tp():
    raise NotImplementedError()


def transferserver():
    raise NotImplementedError()


def w():
    raise NotImplementedError()


def weather():
    raise NotImplementedError()


def xp():
    raise NotImplementedError()


if __name__ == "__main__":
    cmd = Fill(0, 0, 0, 1, 1, 1)
    print(cmd)
