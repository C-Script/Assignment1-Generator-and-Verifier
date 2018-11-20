
from generator import generator
from verifier import verifier

# 1-Taking the Input

inputFile = open("generator_input.txt", "r")
input = inputFile.readlines()

message = input[0].rstrip()
g = input[1]
alter = False
alterBit = 2


# 2- Getting transmitted message from generator
print("Calling Generator")

transmitted_message = generator(message, g)
print("Generator output: " + transmitted_message)

# 3- Altering
## if (alter option is chosen for a bit): alter this bit ##
if(alter):
    transmitted_message = list(transmitted_message)
    if(transmitted_message[alterBit] == "0"):
        transmitted_message[alterBit] = "1"
    else:
        transmitted_message[alterBit] = "0"

    transmitted_message = "".join(transmitted_message)

    print("Message after altering: " + transmitted_message)

# 4- Verifying the message through verifier
print("Calling Verifier")

verification = verifier(transmitted_message, g)
print("Verifier output: " + verification)


# 5- Putting the output
outputFile = open("generator_output.txt", "w")

outputFile.write("Transmitted Message: " + transmitted_message +
                 "\n" + "Verifier Output: " + verification)
