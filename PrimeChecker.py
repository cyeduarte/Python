#Christopher Eduarte
#Lab 6: PrimeChecker.py
#Due Date: 8/17/17

##
#Test whether a value is prime or not
#@param value may be prime or not
#@return prime is True if value is prime and False if value is not prime.
#
def isPrime(value):
    count = 0
    for i in range (1, value + 1):
        if value % i == 0:
                count += 1
                #print("count is", count)

    if count <= 2:
        prime = True
    else:
        prime = False
    return prime

def main():

    cont = True
    
    while(cont):
        value = int(input("Enter a value at or above 1: "))
        if(value >= 1):
            prime = isPrime(value)

            if prime == True:
                print("The number is a prime number.")
            else:
                print("The number is not prime.")
        else:
            print("You have entered a value below 1. You have decided to quit the program.")
            print("Thank you for using the program.")
            cont = False
            
main()

'''
Test 1:
    Enter a value at or above 1: 1
    The number is a prime number.
    Enter a value at or above 1: 2
    The number is a prime.
    Enter a value at or above 1: 17
    The number is a prime number.
    Enter a value at or above 1: 27
    The number is not prime.
    Enter a value at or above 1: 61
    The number is a prime number.
    Enter a value at or above 1: 237
    The number is not prime.
    Enter a value at or above 1: 255
    The number is not prime.
    Enter a value at or above 1: 0
    You have entered a value below 1. You have decided to quit the program.
    Thank you for using the program.
Test 2:
    Enter a value at or above 1: 0
    You have entered a value below 1. You have decided to quit the program.
    Thank you for using the program.
Test 3:
    Enter a value at or above 1: -5
    You have entered a value below 1. You have decided to quit the program.
    Thank you for using the program.
Test 4:
    Enter a value at or above 1: 103
    The number is a prime number.
    Enter a value at or above 1: 2521
    The number is a prime number.
    Enter a value at or above 1: 0
    You have entered a value below 1. You have decided to quit the program.
 Thank you for using the program.


'''
