# ATM

This is a simple ATM style program that reads the contents of a CSV into a Pandas Dataframe and prompts the user to enter a PIN.  The program then presents the user with a menu of 4 options that act on the account information associated with the PIN selected.  A user can check the balance, withdraw from the account provided that the amount does not go negative thus yielding an insufficient funds warning and returning the amount attempted to withdraw to the balance, desposit to the balance, or exit the menu which closes the while loop and writes the contents of the Dataframe back to the CSV.

# Implementation

Install Pandas
clone the file to your machine and navigate to the folder with a command line interface

# Useage Instructions

in a command line opened in the ATM folder you can run the program by typing 
```
python atm.py
```

You should see the prompt to enter a PIN.  At present there is no logic to run if a pin is not in the Dataframe so if you enter any number other than the ones listed below the program will terminate.

Enter one of the following PINS to continue
- 1234
- 4321
- 7890
- 9876

From there you can select any menu item to interact with the account information selected by the PIN entered.  

# Requirements

1. The program reads from a CSV and stores the contents in a Pandas dataframe for interaction and writes back to the CSV when you exit the program.
2. The menu operates as a master while loop based on the PIN entered in the first input dialogue
3. Each menu item is a function (3) that interracts with the datafrme in some way
<<<<<<< HEAD
=======

>>>>>>> 257f25cad695d269002620cb9a96d90e6d2a8b0a
