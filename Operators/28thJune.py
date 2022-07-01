"""
Logical Operators

1) and

condition 1     condition 2     answer
True            True            True
True            False           False
False           True            False
False           False           False


2) or


condition 1     condition 2     answer
True            True            True
True            False           True
False           True            True
False           False           False


3) not

input       output
True        False
False       True
"""

print(15>12 and 12>10)          #True and True = True
print(not(15>12 and 12>10))     # not(True)  = False
print(15>12 or 12<10)           # True or False = True
"""
1) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

2)  A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

3) A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.

4) A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not
"""