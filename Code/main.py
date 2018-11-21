from generator import generator
from verifier import verifier
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
from tkinter import *


def main(window):

    # 0 If the user clicked again on select file clear all below

    for widget in window.grid_slaves():
        if int(widget.grid_info()["row"]) > 1:
            widget.grid_forget()

    # 1-Selecting the input file

    filename = askopenfilename(title="Select the generator input text file ")

    inputFile = open(filename, "r")

    input = inputFile.readlines()

    message = input[0].rstrip()

    g = input[1]

    # 2- Getting transmitted message and r from generator

    print("Calling Generator")
    # generator returns an object that consists of transmitted message and r
    generatorOutput = generator(message, g)
    transmitted_message = generatorOutput["transmitted_message"]
    appended_part = generatorOutput["r"]
    print("Generator output: " + transmitted_message)

    generatorOutputLabel = Label(text='Original message is '+message+'\n Appended part is is ' + appended_part + '\n' +
                                 'Transmitted message is ' + transmitted_message, font='sans-serif 18 bold', fg='#DA611E', pady=30
                                 )
    generatorOutputLabel.grid(column=0, row=2)

    # 3-Asking the user to verify or Alter then verify

    verifyButton = Button(text='Verify the original message', bg='#EA5E3D', activebackground='#000000', fg='#FFFFFF',
                          activeforeground='#FFFFFF', font="Helvetica 20", width=30, height=1,
                          command=lambda: verify(transmitted_message),)
    verifyButton.grid(column=0, row=3)

    orLabel = Label(text='or', font='sans-serif 18 bold', fg='#666666', pady=10
                    )
    orLabel.grid(column=0, row=4)

    alterButton = Button(text='Alter original message then verify', bg='#EA5E3D', command=lambda: Alter(transmitted_message),
                         activebackground='#000000', fg='#FFFFFF', activeforeground='#FFFFFF', font="Helvetica 20", width=30, height=1)
    alterButton.grid(column=0, row=5)

    # Defining actions for buttons:

    
    # global variable for knowing whether the message is altered or not
    global alterState
    alterState = False

    # show output
    def output(verification, transmitted_message):
        outputFile = open("CRC-output.txt", "w")

        outputFile.write("Transmitted Message: " + transmitted_message +
                         "\n" + "Verifier Output: " + verification)
        global alterState
        if alterState:
            print(alterState)
            verifierOutputLabel = Label(text='Altered message is ' + transmitted_message
                                        + ' \n Verifier Output: ' + verification
                                        + '\n\n(Note: Output is printed in a file named "CRC-output.txt" in the same directory.)', font='sans-serif 18 bold', fg='red', pady=30)
            alterState = False

        else:
            verifierOutputLabel = Label(
                text='Transmitted message: '+transmitted_message +
                '\n Verifier Output: ' + verification
                + '\n\n(Note: Output is printed in a file named "CRC-output.txt" in the same directory.)', font='sans-serif 18 bold', fg='green', pady=30)

        # delete the previous label if the user clicked again on verify
        for widget in window.grid_slaves():
            if int(widget.grid_info()["row"]) > 5:
                widget.grid_forget()

        # add the ouput label
        verifierOutputLabel.grid(column=0, row=6)

    # verify transmitted message

    print("Calling Verifier")

    def verify(transmitted_message):
        verification = verifier(transmitted_message, g)
        print("Verifier output: " + verification)
        output(verification, transmitted_message)

    # 3-Alter transmitted message

    # Function to take index to be altered
    def takeIndex():
        index = simpledialog.askinteger(
            "index number", prompt='please enter index number to be manipulated')
        return index

    def Alter(transmitted_message):
        global alterState
        alterBit = takeIndex()
        if alterBit:
                    alterState = True
        transmitted_message = list(transmitted_message)
        if (transmitted_message[alterBit] == "0"):
            transmitted_message[alterBit] = "1"
        else:
            transmitted_message[alterBit] = "0"
        transmitted_message = "".join(transmitted_message)
        verify(transmitted_message)
        print("Message after altering: " + transmitted_message)
