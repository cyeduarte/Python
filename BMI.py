#Christopher Eduarte
#CS299 eduarteBMI.py
#8/3/17

sys = input("Choose e|E for English system, or m/M for metric system: ")

if sys == "e" or sys == "E":
    
    height = (float)(input("Enter the height in inches: "))
    weight = (float)(input("Enter the weight in pounds: "))

    while height == 0:
       print("Division by zero is not allowed.")
       height = (float)(input("reenter height: "))
    
    eBMI = ((weight)/(height*height))*703 #BMI that uses english system
    
    print("You are using the english system.")
    print("your BMI is %5.2f" % eBMI)
    #use an if else to prevent division by zero
    if eBMI <= 24:
        print("Your BMI is normal.")
    elif eBMI >= 25 and eBMI <= 29:
        print("You are overweight.")
    elif eBMI >= 30 and eBMI <= 39:
        print("You are obese.")
    elif eBMI >= 40:
        print("You are extremely obese.")
elif sys == "M" or sys == "m":

    height = (float)(input("Enter the height in meters: "))
    weight = (float)(input("Enter the weight in kilograms: "))
	    #use an if else to prevent division by zero

    while height == 0:
        print("Division by zero is not allowed.")
        height = (float)(input("reenter height: "))
    
    mBMI = (weight)/(height*height) #BMI that uses the metric system
    
    print("You are using the metric system.")
    print("Your BMI is %5.2f" % mBMI)

    if mBMI <= 24:
        print("Your BMI is normal.")
    elif mBMI > 24 and mBMI <= 29:
        print("You are overweight.")
    elif mBMI > 30 and mBMI <= 39:
        print("You are obese.")
    elif mBMI >= 40:
        print("You are extremely obese.")
else:
    print("You have chosen an invalid option.")

'''
   
'''
