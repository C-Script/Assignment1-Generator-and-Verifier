
from generator import generator

# 1-Taking the Input

print("Calling Generator")
inputFile = open("generator_input.txt", "r")

input = inputFile.readlines()

message = input[0].rstrip()
g = input[1]


# 2- Getting transmitted message from generator
transmitted_message = generator(message, g)

# 3- Altering
## if (alter option is chosen for a bit) alter this bit ##

# 4- Verifying the message through verifier
print("Calling Verifier")


# 5- Putting the output
outputFile = open("generator_output.txt", "w")

outputFile.write("transmitted message: " + transmitted_message)
