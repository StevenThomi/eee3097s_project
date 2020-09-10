from FireMarshall import FireMarshall

def main():
    fireMarshall = FireMarshall(2)

    print("The following fire marshall has been registered: ")
    fireMarshall.printMarshall()

    print("\nLet's change some of their attributes;")

    print("First of all, lets change their name. ")
    newName = input("Input a cool name: ")
    fireMarshall.setName(newName)

    print("\nA password of \'0\' doesn't sound so strong. ")
    newPassword = input("Input a strong password: ")
    fireMarshall.setPassword(newPassword)

    print("\nWhat about a phone number? It's always good to be accessible. ")
    newPhone = input("Input a phone number: ")
    fireMarshall.setPhone(newPhone)

    print("\nLooking good! Their account is now starting to take shape: ")
    fireMarshall.printMarshall()

    print("\nOne last thing, what about a fancier user ID " + str(fireMarshall.getUserID()) + " sounds a little bit bulky. ")
    answer = input("Would you like to change it (Y/N)?")

    if (answer == "Y"):
        print("Processing changes...")
        fireMarshall.setUserID()

        print("\nJackpot! Hit my lucky number of " + str(fireMarshall.getUserID()))
    else:
        print("No is as good an answer as any")

    print("\nHere are the changes: ")
    fireMarshall.printMarshall()

    print("\nLogging out session... ")
    fireMarshall.setLoginStatus()

    print("\nFinally: ")
    fireMarshall.printMarshall()

main() # Call the main function
