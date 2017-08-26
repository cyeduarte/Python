#Christopher Eduarte
#CS299: PizzaOrder.py
#Due Date: 8/22/17

##
#@param none
#@return return size is the size of the pizza
#
def getSize():
    
    wrongChoice = True
    count = 0
    
    while wrongChoice == True and count < 3: #loop if wrong choice

        print("The list of sizes you can choose from: 10, 12, 14, 16.")
        size = input("Please enter one of the following sizes: ")
        size = int(size)
        
        if size == 10:
            wrongChoice = False
        elif size == 12:
            wrongChoice = False
        elif size == 14:
            wrongChoice = False
        elif size == 16:
            wrongChoice = False
        else:
            wrongChoice = True
            count += 1
            print("There is no size for that pizza. Wrong choice.")

        if count >= 3: #exit if the user failed to enter the size 3 times
            print("Very Sorry. You have used up all of your tries. Please try again at a later time.")
            return - 1
        if wrongChoice == False: #Return if the choice is correct
            return size

##
#@param none
#@return extra is the extra cost of the crust type
#
def getCrust():
    print("Choose one of the following crust:\nh or H for hand-tossed.\nT or t for thin crust.\nD or d for deep crust.")
    crust = input("Please enter type: ")

    #Set extra from crust type entered
    if crust == "h" or crust == "H":
        print("You ordered a hand-tossed crust.")
        extra = 0
    elif crust == "t" or crust == "T":
        print("You have ordered a thin crust.")
        extra = 1
    elif crust == "d" or crust == "D":
        print("You have ordered a deep crust.")
        extra = 2
    else:
        print("You have ordered a hand-tossed crust.")
        extra = 0

    return extra

##
#@param none
#@return discount is the discount created from the coupon
#
def applyDiscount():
    
    print("Coupon Code", " " * 5, "Discount")
    print("Holiday10 %10d" % 10,"percent discount.","\nWinter20 %11d" % 20,"percent discount.","\nVIPMax %13d" % 25,"percent discount.")

    coupon = input("Please enter one of the coupon discounts above:")

    disc = 0

    #Set the discount from the coupon entered
    if coupon == "Holiday10":
        print("10 percent discount")
        disc = 0.10
    elif coupon == "Winter20":
        print("20 percent discount")
        disc = 0.20
    elif coupon == "VIPMax":
        print("25 percent discount")
        disc = 0.25
    else:
        print("The discount is 0 percent")

    return disc
    

def main():
    size = getSize()
    #print("size is", size)
    print("")

    if size != -1: #program ends when an incorrect size is entered 3 times
        extra = getCrust()
        print("extra is", extra)
        print("")
        disc = applyDiscount()
        print("discount is", disc)
        print("")
        totalCost = cost(size, extra, disc)
        print("The total cost is $%.2f" % totalCost)

##
#@param size is the pizza size, extra is the cost of the crust, and disc is the discount from the coupon
#@return totalCost is the total cost of the pizza
#
def cost(size, extra, disc):
    cost = 0

    #set the cost for the size of the pizza
    if size == 10:  
        cost = 10.99
    elif size == 12:
        cost = 12.99
    elif size == 14:
        cost = 14.99
    elif size == 16:
        cost = 16.99
    elif size == -1:
        cost = 0

    print("The cost is for the size is $%.2f." % cost)

    discount = (cost + extra) * disc
    print("The discount is $%.2f" % discount)

    totalCost = (cost + extra) - discount

    return totalCost

main()

'''
Test 1:
    The list of sizes you can choose from: 10, 12, 14, 16.
    Please enter one of the following sizes: 15
    There is no size for that pizza. Wrong choice.
    The list of sizes you can choose from: 10, 12, 14, 16.
    Please enter one of the following sizes: 17
    There is no size for that pizza. Wrong choice.
    The list of sizes you can choose from: 10, 12, 14, 16.
    Please enter one of the following sizes: 11
    There is no size for that pizza. Wrong choice.
    Very Sorry. You have used up all of your tries. Please try again at a later time.
    size is -1 
Test 2:
    The list of sizes you can choose from: 10, 12, 14, 16.
    Please enter one of the following sizes: 17
    There is no size for that pizza. Wrong choice.
    The list of sizes you can choose from: 10, 12, 14, 16.
    Please enter one of the following sizes: 16
    size is 16

    Choose one of the following crust:
    h or H for hand-tossed.
    T or t for thin crust.
    D or d for deep crust.
    Please enter type: e
    You have ordered a hand-tossed crust.
    extra is 0

    Coupon Code       Discount
    Holiday10         10 percent discount. 
    Winter20          20 percent discount. 
    VIPMax            25 percent discount.
    Please enter one of the coupon discounts above:Winter20
    20 percent discount
    discount is 0.2

    The cost is for the size is $16.99.
    The discount is $3.40
    The total cost is $13.59
Test 3:
    The list of sizes you can choose from: 10, 12, 14, 16.
    Please enter one of the following sizes: 12
    size is 12

    Choose one of the following crust:
    h or H for hand-tossed.
    T or t for thin crust.
    D or d for deep crust.
    Please enter type: d
    You have ordered a deep crust.
    extra is 2

    Coupon Code       Discount
    Holiday10         10 percent discount. 
    Winter20          20 percent discount. 
    VIPMax            25 percent discount.
    Please enter one of the coupon discounts above:0
    The discount is 0 percent
    discount is 0

    The cost is for the size is $12.99.
    The discount is $0.00
    The total cost is $14.99
Test 4:
    Please enter one of the following sizes:10, 12, 14, 16: 14
    size is 14

    Choose one of the following crust:
    h or H for hand-tossed.
    T or t for thin crust.
    D or d for deep crust.
    Please enter type: t
    You have ordered a thin crust.
    extra is 1

    Coupon Code            Discount
    Holiday10 for 10 percent discount.
    Winter20 for 20 percent discount. 
    VIPmax for 25 percent discount.
    Please enter one of the coupon discounts above:VIPmax
    The discount is 0 percent
    discount is 0

    The cost is 14.99
    The total cost is $15.99
Test 5:
    The list of sizes you can choose from: 10, 12, 14, 16.
    Please enter one of the following sizes: 11
    There is no size for that pizza. Wrong choice.
    The list of sizes you can choose from: 10, 12, 14, 16.
    Please enter one of the following sizes: -20
    There is no size for that pizza. Wrong choice.
    The list of sizes you can choose from: 10, 12, 14, 16.
    Please enter one of the following sizes: 100
    There is no size for that pizza. Wrong choice.
    Very Sorry. You have used up all of your tries. Please try again at a later time.
    size is -1
Test 6:
    The list of sizes you can choose from: 10, 12, 14, 16.
    Please enter one of the following sizes: 15
    There is no size for that pizza. Wrong choice.
    The list of sizes you can choose from: 10, 12, 14, 16.
    Please enter one of the following sizes: 18
    There is no size for that pizza. Wrong choice.
    The list of sizes you can choose from: 10, 12, 14, 16.
    Please enter one of the following sizes: 10
    size is 10

    Choose one of the following crust:
    h or H for hand-tossed.
    T or t for thin crust.
    D or d for deep crust.
    Please enter type: D
    You have ordered a deep crust.
    extra is 2

    Coupon Code       Discount
    Holiday10         10 percent discount. 
    Winter20          20 percent discount. 
    VIPMax            25 percent discount.
    Please enter one of the coupon discounts above:Winter20
    20 percent discount
    discount is 0.2

    The cost is for the size is $10.99.
    The discount is $2.60
    The total cost is $10.39
'''
    

