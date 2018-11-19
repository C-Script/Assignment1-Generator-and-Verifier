### The verifier / receiver function ###

from XOR import XOR


def verifier(transmitted_message, g):

    # 1-Doing XOR between transmitted message and generator
    r = XOR(transmitted_message, g)

    if(int(r) > 0):
        verification = "Message is transmitted incorrectly, there is an error."
    else:
        verification = "Message is transmitted correctly."

    return verification
