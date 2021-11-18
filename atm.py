import pandas as pd
from datetime import datetime

df = pd.read_csv('accounts.csv')

loggedIn = 0

#Logs changes to the balance in a textfile
def change_logger():
    f = open('log.txt', "a")
    f.write("{0} -- {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"), 'Balance Changed'))
    f.close()

# Formats and prints balance from data frame slice determined by selectedPin
def check_balance():
    curBalF = "${:,.2f}".format(df.at[int(acctIndex), 'balance'])
    print(f"Your current balance is {curBalF}") 

# Withdraw from balance, if balance is less than 0 return insufficient funds 
# and restore balance, else print new balance
def withdraw_Amt():
    withdrawAmt = int((input("How much would you like to withdraw? ")))
    df.loc[acctIndex, 'balance'] = df.loc[acctIndex, 'balance'] - withdrawAmt
    if (df['balance'] < 0).any():
        print('Insufficient Funds, please try a lesser amount')
        df.loc[acctIndex, 'balance'] = df.loc[acctIndex, 'balance'] + withdrawAmt
    else:
        return withdrawAmt
    
# Add to balance and return new balance
def deposit_Amt():
    depositAmt = int((input("How much would you like to deposit? ")))
    df.loc[acctIndex, 'balance'] = df.loc[acctIndex, 'balance'] + depositAmt
    return depositAmt
    
# Request Pin from user
selectedPin = int(input("Enter PIN: "))

#Extracts the row with the pin from the data frame
acctIndex = df[df['pin']==selectedPin].index.values

# Set Logged in value to 1 now user is logged in
if selectedPin in df.values:
    loggedIn = 1
else:
    print('Invalid PIN, please enter a valid PIN')
    selectedPin = int(input("Enter PIN: "))
    
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
        check_balance()
        change_logger()
            
    elif selection  == "3":
        deposit_Amt()
        check_balance()
        change_logger()
                
    # Selection 4
    elif selection == "4":
        print("logging out")
        df.to_csv('accounts.csv', index=False)

        # Log out user (exit loop)
        loggedIn = 0

    else:
        print("Invalid selection")
