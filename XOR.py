### The function that is called in the generator and the verifier files ###


######################### Helper Functions #########################

def mainXOR(s1, s2):
    result = ""
    if(len(s1) != len(s2)):
        return 0
    else:
        for i in range(len(s1)):
            if((s1[i] == "1" and s2[i] == "1") or (s1[i] == "0" and s2[i] == "0")):
                result += "0"
            else:
                result += "1"

    return result


def elimnating_left_zeros(s):
    result = s
    for i in range(len(s)):
        if(s[i] == "0"):
            result = s[i+1:]
        else:
            return result

    return ""


######################### Primary Function #########################

def XOR(message, G):

    i = 0
    message_slice = ""
    lengthOfMessage_slice = 0
    flag = 0

    while(1):
        if(((i+len(G)) - lengthOfMessage_slice) <= len(message)):
            message_slice = message_slice + \
                message[i:((i+len(G)) - lengthOfMessage_slice)]
        else:
            message_slice = message_slice + message[i:]
            flag = 1
        i = ((i + len(G)) - lengthOfMessage_slice)

        if(len(message_slice) < len(G)):
            break
        # message after XOR
        message_slice = mainXOR(message_slice, G)

        # message after elimnating left zeros
        message_slice = elimnating_left_zeros(message_slice)

        lengthOfMessage_slice = len(message_slice)
        if (flag == 1):
                break
    while(len(message_slice) < len(G)-1):
        message_slice = "0"+message_slice

    return message_slice
