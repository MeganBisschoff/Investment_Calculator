# Investment and Bond Repayment Calculator

A Python calculator that allows a client to calculate their investment earnings and bond repayment amounts.

## Description

This program is for a financial company that allows a client to calculate their interest on an investment or calculate the amount that should be repaid on a home loan each month.

The investment calculator allows the client to:

* Calculate the Simple interest given the interest rate, principal amount and time period.
* Calculate the Compound interest given the interest rate, accumulated amount and the time period.

The bond repayment calculator allows the client to:

* Calculate the monthly bond repayments given the property value, interest rate and payment period.

## Functionality summary

* Calculates investment earnings
* Calculates bond repayments

## Programming principles

This program employs the fundamental programming principles of Python variables and control structures.

## Dependencies

    import math

## Running the program

Run the inventory.py file in any Python IDE.

## Code preview

```python 
# If user chooses INVESTMENT, request data.
if user_choice == "investment":
    
    investment_deposit = float(input("\nEnter the amount you would like to deposit: R "))
    investment_rate = float(input("Enter the interest rate: % "))
    investment_rate = float(investment_rate/100)
    investment_years = float(input("How many years would you like to invest for: "))
    interest = input("Would you like to calculate 'Simple' or 'Compound' interest: ").lower()
    
    # If user chooses SIMPLE interest, calculation begins.
    if interest == "simple":
        simple = int(investment_deposit*(1+(investment_rate*investment_years)))
        print(f"\nYour simple earnings = R{simple}")
    
    # If user chooses COMPOUND interest, calculation begins. 
    elif interest == "compound":
        compound = int(investment_deposit * math.pow((1+ investment_rate),investment_years))
        print(f"\nYour compound earnings = R{compound}")
```

## Program preview

```
Enter the amount you would like to deposit: R 1000000
Enter the interest rate: % 5
How many years would you like to invest for: 5
Would you like to calculate 'Simple' or 'Compound' interest: Compound

Your compound interest = R1276281
```

&nbsp;
***
_The most important quality for an investor is temperament, not intellect._ \~ Warren Buffet  
***  
&nbsp;
  
## Author  

Megan Bisschoff

Project submitted for Software Engineering learnership Level 1 Task 11 at [HyperionDev](https://www.hyperiondev.com/)

[View](https://www.hyperiondev.com/portfolio/86596/) submission results and code review.
