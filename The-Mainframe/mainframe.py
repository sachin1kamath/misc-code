import time, sys, random
from login import loading_bar, spaz_out

def mainframe():
    time.sleep(1)
    print("\nWelcome to the Mainframe!")
    loading_bar("Reauthenticating...")

    choice = int(input("What would you like to do? \n1. Hack the Mainframe \n2. Remove a website of your choice \n3. Turn off the internet \nEnter the number of your choice: "))

    if choice == 1:
        loading_bar("Entering backdoor...", 0.02)
        loading_bar("Hacking in progress...", 0.03)
        print("d0Nee|.")
        time.sleep(1)
        for i in range(5):
            print(".")
        print("^&*!@%#&")
        spaz_out(1, 20)
        time.sleep(1)
        print("WARNNINGGGggg...")
        time.sleep(1)
        print("CriTICal EEErOr.,..")
        loading_bar("geh", 0.01, "!%$@^&$&")
    elif choice == 2:
        input("Please enter the URL of your website: ")
        loading_bar("Removing...", 0.06)
        print("Done!")
        loading_bar("Leaving the Mainframe...", 0.015)
    elif choice == 3:
        loading_bar("Attempting to remove the internet...", 0.07, "!")
        print("CRITICAL MAINFRAME ERROR")
        time.sleep(1)
        print("ABORTING ATTEMPT")
        time.sleep(0.5)
        loading_bar("ABORT", 0.01, "*")
        print("SUCCESSFULLY ABORTED. YOU HAVE BEEN TEMPORARILY BANNED FROM THE MAINFRME. SCRAM")