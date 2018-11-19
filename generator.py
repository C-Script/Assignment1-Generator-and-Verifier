# The generator / sender function


# 1-Taking the Input

print("Generator")
F = open("generator_input.txt", "r")
input = F.readlines()

message = input[0].rstrip()
generator = input[1]

print("Message is "+message)
print("Generator is "+generator)


# Output
file = open("generator_output.txt", "w")

file.write("I am the generator output")
