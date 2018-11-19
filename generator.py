### The generator / sender function ###
from XOR import XOR


def generator(message, g):

    # 1-Adding necessary zeros to the message
    generatorLength = len(g)
    appendedZerosLength = generatorLength-1

    for x in range(appendedZerosLength):
        message = message+"0"

    # 2-Doing XOR between message and generator
    r = XOR(message, g)

    transmittedMessage = message + r
    return transmittedMessage
