import pandas as pd
import numpy as np
df = pd.read_csv('accounts.csv')

# Request Pin from user
selectedPin = int(input("Enter PIN: "))

#Extracts the row with the pin from the data frame
acctIndex = df[df['pin']==selectedPin].index.values

# Add to balance and return new balance
def deposit_Amt():
    depositAmt = int((input("How much would you like to deposit? ")))
    df.loc[acctIndex, 'balance'] = df.loc[acctIndex, 'balance'] + depositAmt
    

# Withdraw from balance, checks if balance is greater than zero, returns new balance
def withdraw_Amt():
    withdrawAmt = int((input("How much would you like to withdraw? ")))
    df.loc[acctIndex, 'balance'] = df.loc[acctIndex, 'balance'] - withdrawAmt
           
"""
    if withBal > 0:
            print("You withdrew {} dollars. Your remaining balance is: {} dollars".format(withdrawAmt, withBal))
    else:
            print("You're broke! Please control your spending habits!")
            loggedIn = 0
"""
# Formats and prints balance from data frame slice determined by selectedPin
def check_balance():
    curBalF = "${:,.2f}".format(df.at[int(acctIndex), 'balance'])
    print(f"Your current balance is {curBalF}")
    
     

# Set Logged in value to 1 now user is logged in
# Checks pin input against saved pin
if selectedPin in df.values:
    loggedIn = 1
else:
    loggedIn = 0

while loggedIn == 1:
    # Print menu options
    print(f"Hello, what would you like to do today?")
    print("1 - Check Balance")
    print("2 - withdraw")
    print("3 - Deposit")
    print("4 - End Session")
    # Get selection Input
    selection = input("Enter Selection: ")

    # Selection 1
    if selection == "1":
        check_balance()
            
    # Selection 2
    elif selection == "2":
        withdraw_Amt()
            
    elif selection  == "3":
        deposit_Amt()
                
    # Selection 4
    elif selection == "4":
        print("logging out")
        df.to_csv(('accounts.csv'))

        # Log out user (exit loop)
        loggedIn = 0

    else:
        print("Invalid selection")
