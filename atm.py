import pandas as pd
df = pd.read_csv('atm/accounts.csv')

# Request Pin from user
selectedPin = int(input("Enter PIN: "))


# Add to balance and return new balance
def make_Deposit():
        depositAmt = float(input("How much would you like to deposit? "))
        global balance
        balance +=  depositAmt
        print("You deposited {} dollars. Your new balance is: {} ".format(depositAmt, balance))

# Withdraw from balance, checks if balance is greater than zero, returns new balance
def withdraw_Amt():
    withdrawAmt = float((input("How much would you like to withdraw? ")))
    global balance
    balance -= withdrawAmt
    if balance > 0:
            print("You withdrew {} dollars. Your remaining balance is: {} dollars".format(withdrawAmt, balance))
    else:
            print("You're broke! Please control your spending habits!")
            loggedIn = 0

# Returns current balance
def check_balance():
     print("This is your current Balance: {}".format(df.loc[df['pin'] == selectedPin])(0, 'balance'))

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
