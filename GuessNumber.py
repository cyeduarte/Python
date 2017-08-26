#Christopher Eduarte
#CS299: Project 2
#Due Date: 8/17/17

import random

rounds = 0
win = False

hidden = random.randint(1, 100) #Hidden will have a value between 1 to 100
#print("Hidden is ", hidden)

while rounds < 5: #5 rounds before the program quits

    count = 0
    
    guess = (input("Please enter a number between 1 to 100: "))

    if not guess.isdigit(): #When the value is not a digit
        while not guess.isdigit() and count < 3:

            guess = input("The value must be a digit and between 1 to 100: ")
            count += 1

            if count == 3: #quit the program when the user uses all 3 tries
                rounds = 5
                print("round is", rounds)

        #guess = float(guess)
    else:
        guess = float(guess)

    if(float(guess) < 0 or float(guess) > 100): #When value is out of bound go to loop
        while (float(guess) < 0 or float(guess) > 100) and count < 3: # 3 tries for loop
            count += 1
            guess = input("The value must be between 1 to 100: ")
            print("count is", count)

            if count == 3 and (float(guess ) < 0 or float(guess) > 100): #Quit the program when the user uses up all 3 tries
                rounds = 5
                print("round is ", rounds)
        guess = float(guess)
        correct = True
            
    rounds += 1
    print("Round is", rounds)

    if count < 3 or correct == True:         
        if float(guess) > hidden:
            print("Too high. Please guess again.")
        elif float(guess) < hidden:
            print("Too low. Please guess again")
        elif float(guess) == hidden:
            print("You win.")
            win = True
            rounds = 5

    if rounds >= 5 and win == True: #Exit the program and show the hidden value
        print("The value is %d." % hidden)
    elif rounds >= 5 and win == False:
        print("The value is %d." % hidden)
        print("The computer wins")
    

'''
Test 1:
    Please enter a number betwen 1 to 100: 100
    Too high
    Please enter a number betwen 1 to 100: 50
    Too high
    Please enter a number betwen 1 to 100: 57
    Too high
    The value is  40
Test 2:
    Hidden is  30
    Please enter a number betwen 1 to 100: 10
    Too low
    Please enter a number betwen 1 to 100: 40
    Too high
    Please enter a number betwen 1 to 100: 30
    You win. The value is 30
    The value is  30
Test 3:
    Hidden is  14
    Please enter a number betwen 1 to 100: 200
    The number must be between 1 to 100: -10
    The number must be between 1 to 100: 2
    Please enter a number betwen 1 to 100: 2
    Too low
    Please enter a number betwen 1 to 100: 4
    Too low
    The value is  14
Test 4:
    Please enter a number betwen 1 to 100: -1
    The number must be between 1 to 100: -2
    The number must be between 1 to 100: -3
    The number must be between 1 to 100: 97
    You win. The value is 97
    The value is  97
Test 5:
    Hidden is  41
    Please enter a number betwen 1 to 100: 1
    Too low
    Please enter a number betwen 1 to 100: 2
    Too low
    Please enter a number betwen 1 to 100: 3
    Too low
    Please enter a number betwen 1 to 100: 4
    Too low
    Please enter a number betwen 1 to 100: 5
    Too low
    The value is  41
Test 6:
    Hidden is  63
    Please enter a number betwen 1 to 100: -1
    count is 1
    The number must be between 1 to 100: -2
    count is 2
    The number must be between 1 to 100: -3
    count is 3
    Please enter a number betwen 1 to 100: 5
    Please enter a number betwen 1 to 100: 6
    Please enter a number betwen 1 to 100: 8
    Please enter a number betwen 1 to 100: 9
    The value is  63
Test 7:
    Hidden is  38
    Please enter a number between 1 to 100: fjewioa;f 
    The value must be a digit and between 1 to 100: a
    The value must be a digit and between 1 to 100: 80.0
    The value must be a digit and between 1 to 100: 80
    round is 5
    The value is 38.
    The computer wins
'''
