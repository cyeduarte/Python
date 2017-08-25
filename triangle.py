#Chrisotpher Eduarte
#Lab 6: triangle.py
#Due Date: 8/17/17

from math import*

def main():
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = triangle(a, b)
    print("c is %.1f" % c)
    deg = calcDeg(a, b)
    print("degree of c is %.2f" % deg)

##
#@param a is side a of the triangle
#@param b is side b of the triangle
#@return c is side c of the triangle
def triangle(a, b):
    c = sqrt(a*a + b*b)
    return c

##
#@param a is the side of the triangle
#@param b is the side of the triangle
#@return deg the degree opposing a and b
def calcDeg(a, b):
    x = atan(a/b)
    deg = degrees(x)
    return deg

main()

'''
Test 1:
    Enter side a: 7.5
    Enter side b: 7.5
    c is 10.6
    degree of c is 45.00

Test 2:
    Enter side a: 7.5
    Enter side b: 10
    c is 12.5
    degree of c is 36.87
Test 3:
    Enter side a: 6.0
    Enter side b: 4.5
    c is 7.5
    degree of c is 53.13
    
'''
        
