### The generator / sender function ###


# 1-Taking the Input

print("Generator")
F = open("generator_input.txt", "r")

input = F.readlines()

message = input[0].rstrip()
generator = input[1]


# 2-Adding necessary zeros to the message

generatorLength = len(generator)
appendedZerosLength = generatorLength-1

for x in range(appendedZerosLength):
    message = message+"0"

print("Message is "+message)
print("Generator is "+generator)


# 3-Doing XOR between message and generator
## calling XOR function ##


# 4-Printing the output
file = open("generator_output.txt", "w")

file.write("I am the generator output")
