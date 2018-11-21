### The generator / sender function ###
from XOR import XOR


def generator(message, g):

    # 1-Adding necessary zeros to the message
    original_message = message

    appendedZerosLength = len(g)-1

    for x in range(appendedZerosLength):
        message = message+"0"

    # 2-Doing XOR between message and generator
    r = XOR(message, g)

    print("Part appended to message before transmitting: " + r)

    transmittedMessage = original_message + r
    return {'transmitted_message':transmittedMessage, 'r':r}
