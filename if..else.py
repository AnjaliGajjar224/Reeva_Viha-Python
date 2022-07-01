"""
Conditional Statements:
1) if
2) if..else
3) if , elif, .....,else

Syntax:

if condition:
    //Logic Code
"""

# num1 = int(input("Enter Number 1:"))
# num2 = int(input("Enteer Number 2:"))

# if num1 > num2:
#     print(num1,"is maximum")
# else:
#     print(num2,"is maximum")


n1 = int(input("Enter number 1:"))
n2 = int(input("Enter number 2:"))
print("+ , - , * , / , // , ** , % ")
choice = input("Enter Sign :")

if choice == "+":
    print(n1,"+",n2,"=",n1+n2)

elif choice == "-":
    print(n1,"-",n2,"=",n1-n2)

elif choice == "*":
    print(n1,"*",n2,"=",n1*n2)

elif choice == "/":
    print(n1,"/",n2,"=",n1/n2)

elif choice == "//":
    print(n1,"//",n2,"=",n1//n2)

elif choice == "**":
    print(n1,"**",n2,"=",n1**n2)

elif choice == "%":
    print(n1,"%",n2,"=",n1%n2)

else:
    print("You have entered Wrong Choice!!!")


