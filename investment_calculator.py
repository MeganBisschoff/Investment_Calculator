# This program is for a financial company that allows
# a client to calculate their interest on an investment
# or calculate the amount that should be repaid on a 
# home loan each month.

# Libraries
import math

# Display users options.
print('''Choose either Investment or Bond from the menu below to proceed.
Investments calculate the amount of interest you'll earn on interest.
Bonds calculate the amount you'll have to pay on a home loan.''')

# Ask user to input their choice.
user_choice = input("\nWould you like to use the 'Investment' or 'Bond' calculator? ").lower()

# If user chooses INVESTMENT, request data.
if user_choice == "investment":
    
    investment_deposit = float(input("\nEnter the amount you would like to deposit: R "))
    investment_rate = float(input("Enter the interest rate: % "))
    investment_rate = float(investment_rate/100)
    investment_years = float(input("How many years would you like to invest for: "))
    interest = input("Do you want 'Simple' or 'Compound' interest: ").lower()

    # If user chooses SIMPLE interest, calculation begins.
    if interest == "simple":
        simple = int(investment_deposit*(1+(investment_rate*investment_years)))
        print(f"\nYour simple interest = R{simple}")

    # If user chooses COMPOUND interest, calculation begins. 
    elif interest == "compound":
        compound = int(investment_deposit * math.pow((1+ investment_rate),investment_years))
        print(f"\nYour compound interest = R{compound}")

# If user chooses BOND, request data.
elif user_choice == "bond":

    bond_value = float(input("\nEnter the present value of the house: R "))
    bond_rate = float(input("Enter the interest rate: % "))
    monthly_rate = float(bond_rate/12)
    bond_months = float(input("How many months would you like to repay for: "))
    
    # Calculation begins. 
    bond_repayment = int((monthly_rate*bond_value) / (1- (1+monthly_rate)**(-bond_months)))
    print(f"\nYour bond repayment = R{bond_repayment}")

# If user input is invalid, notify them and request again:
else:
    print("\nInvalid entry, please try again by choosing Investment or Bond from the menu to proceed.")
