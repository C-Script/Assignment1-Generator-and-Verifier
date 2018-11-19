### The function that is called in the generator and the verifier files ###

def XOR ( s1 , s2 ):
    result= ""
    if(len(s1) != len(s2)):
        return 0
    else:
        for i in range(len(s1)):
            if( (s1[i] == "1" and s2[i] == "1" ) or (s1[i] == "0" and s2[i] == "0") ):
                result+="0"
            else:
                result+="1"

    return result

def elimnating_Left_zeros(s):
    result = s
    for i in range(len(s)):
        if(s[i] == "0"):
            result = s[i+1:]
        else:
            return result

    return ""

def Adding_Left_zeros(s,len_G):
    while(1):

         if(len(s) < len_G - 1):
             s = "0" + s
         elif (len(s) == len_G - 1):
             return s




message = "101110000"      # str                  #7ot ya abdo al message bta3tk mkan de
G = "1001"                     # lentgh=4                #7ot ya abdo al G bta3tk mkan de
i = 0
message_slice = ""
lengthOfMessage_slice = 0
flag = 0
while(1):
    if(((i+len(G)) - lengthOfMessage_slice) < len(message)):
        message_slice = message_slice + message[i:((i+len(G)) - lengthOfMessage_slice)]
    else:
        message_slice = message_slice + message[i:]
        flag = 1
    i = ((i + len(G)) - lengthOfMessage_slice)
    #print(message_slice)
    if(len(message_slice) < len(G)):
        break
    message_slice = XOR(message_slice,G)                      # message after XOR
    #print(message_slice)
    message_slice = elimnating_Left_zeros(message_slice)      # message after elimnating left zeros
    #print(message_slice,"\n")
    lengthOfMessage_slice = len(elimnating_Left_zeros(message_slice))
    if (flag == 1):
        break


message_slice = Adding_Left_zeros(message_slice,len(G))
#print("#######" + message_slice + "#########")

file = open("generator_output.txt", "w")
file.write(message_slice)





