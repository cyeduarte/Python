#Christopher Eduarte
#CS299 Barcode.py
#Due Date: 8/29/17

import turtle

##Signals the start and end of the encoding process
#@param none
#@return
#
def startStop():
    return "----1"

##Reads in a digit and converts into a code
#@param index is the digit that is to be converted into the code
#@return encode is the 5 digit code that will eventually be converted to a barcode
#
def encode(index):
    encode = ""
    
    if index == 0:
        encode += "11100"
    elif index == 1:
        encode += "00011"
    elif index == 2:
        encode += "00101"
    elif index == 3:
        encode += "00110"
    elif index == 4:
        encode += "01001"
    elif index == 5:
        encode += "01010"
    elif index == 6:
        encode += "01100"
    elif index == 7:
        encode += "10001"
    elif index == 8:
        encode += "10011"
    elif index == 9:
        encode += "10100"
            
    return encode

##Draws the coded message into barcode 
#@param code is the encoded message that will be converted into a barcode
#@param length is the length of the coded message
#@return none
def draw(code, length):
    t = turtle.pen()
    
    for i in range(0, length):
        if code[i] == "0":
            turtle.left(90)
            turtle.forward(5)
            turtle.right(90)
            turtle.forward(5)
            turtle.right(90)
            turtle.forward(5)
            turtle.left(90)
            
        elif code[i] == "1":
            turtle.left(90)
            turtle.forward(20)
            turtle.right(90)
            turtle.forward(5)
            turtle.right(90)
            turtle.forward(20)
            turtle.left(90)
        

#main function of the program      
def main():
    barLst = []

    for i in range(0, 10):
        digit = input("Please enter the digit: ")
        digit = int(digit)
        barLst.append(digit)

    length = len(barLst)

    code = ""

    code += startStop()

    for i in range(0, length):
        code += encode(barLst[i])

    code += startStop()

    print(code)

    codeLength = len(code)
    print(draw(code, codeLength), end = " ")

    
main()
    
