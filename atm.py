import pandas as pd
df = pd.read_csv('atm/accounts.csv')

# Request Pin from user
selectedPin = int(input("Enter PIN: "))

#Extracts the row with the pin from the data frame
acctIndex = df[df['pin']==selectedPin].index.values
selectedAcct = df.iloc[acctIndex,]

"""
# Add to balance and return new balance
def make_Deposit():
        depositAmt = float(input("How much would you like to deposit? "))
        global balance
        balance +=  depositAmt
        print("You deposited {} dollars. Your new balance is: {} ".format(depositAmt, balance))
"""

# Withdraw from balance, checks if balance is greater than zero, returns new balance
def withdraw_Amt():
    withdrawAmt = float((input("How much would you like to withdraw? ")))
    withBal = selectedAcct.at[int(acctIndex), 'balance']
    withBal -= withdrawAmt

    if withBal > 0:
            print("You withdrew {} dollars. Your remaining balance is: {} dollars".format(withdrawAmt, withBal))
    else:
            print("You're broke! Please control your spending habits!")
            loggedIn = 0

# Formats and prints balance from data frame slice determined by selectedPin
def check_balance():
    curBal = selectedAcct.at[int(acctIndex), 'balance']
    curBalF = "${:,.2f}".format(curBal)
    print(f"Your current balance is {curBalF}")
    
     

# Set Logged in value to 1 now user is logged in
# Checks pin input against saved pin
if selectedPin in df.values:
    loggedIn = 1
else:
    loggedIn = 0

while loggedIn == 1:
    # Print menu options
    print("1 - Check Balance")
    print("2 - withdraw")
    print("3 - End Session")
    print("4 - Deposit")
    print(acctIndex)
    # Get selection Input
    selection = input("Enter Selection: ")

    # Selection 1
    if selection == "1":
        check_balance()
    
        
    # Selection 2
    elif selection == "2":
        withdraw_Amt()
        
    # Selection 3
    elif selection == "3":
        print("logging out")

        # Log out user (exit loop)
        loggedIn = 0
    
    elif selection  == "4":
        make_Deposit()
        
    else:
        print("Invalid selection")
