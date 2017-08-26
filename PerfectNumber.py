#Christopher Eduarte
#CS299: PerfectNumber.py
#8/17/17

value = int(input("Check if value is a perfect number: "))
sum = 0

for factor in range(1, value):
    if(value % factor == 0):
        sum += factor
    factor += 1
    
if sum  == value:
    print("yes, it is a perfect number.")
else:
    print("No, it is not a perfect number.")

'''
Test 1:
    Check if value is a perfect number: 6
    yes

Test 2:
    Check if value is a perfect number: 28
    yes

Test 3:
    Check if value is a perfect number: 8128
    yes
Test 4:
    Check if value is a perfect number: 8000
    No
Test 5:
    Check if value is a perfect number: 5
    No
Test 6:
    Check if value is a perfect number: 325
    No
Test 7:
    Check if value is a perfect number: 496
    yes
Test 8:
    Check if value is a perfect number: 495
    No, it is not a perfect number.

    
'''
