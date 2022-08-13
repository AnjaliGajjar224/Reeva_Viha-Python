data = {}
print("WELCOME TO THE SYSTEM")


while(True):
    print("1---->Sign Up")
    print("2---->Login")
    print("3---->Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Username: ")
        pw = input("Enter Password: ")

        data.setdefault(name,pw)
        print("-----------------------")
        print("Your Username: ",name)
        print("Your password: ",pw)

        print("You are Successfully Registered".center(50,"*"))
        print()

    elif choice == 2:
        name = input("Enter Username: ")
        pw = input("Enter password: ")

        if name in data.keys():
            if pw == data.get(name):
                print("You are Login Successfully".center(50,"*"))
                break
            else:
                print("Wrong Password")
                print() 
        else:
            print("User Not found")
            print("You have to SignUp first")

    elif choice == 3:
        break