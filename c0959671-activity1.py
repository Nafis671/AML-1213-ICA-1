# AML-1213
# Assignment 1
# Name: Nafis Ahmed
# 23 January 2025

# Task - 1
food_cost = float(input("Bill of food purchased : "))
TIP = .18
HST = .13
total_amount = food_cost + (food_cost * TIP) + (food_cost * HST)

print('Total amount to be paid :', format(total_amount,'.2f'))




# Task - 2
import os
import sys

principal_amount = float(input("Total amount deposited/loaned : "))
annual_interest_rate = float(input("Annual Interest Rate : ")) 

INTEREST_RATE = annual_interest_rate * 1/100

interest_compound_term = input("Write 'm' for monthly or 'q' for quarterly interest compound term: ")

if(interest_compound_term == 'm'):
    interest_compound_rate = 12
elif(interest_compound_term == 'q'):
    interest_compound_rate = 4
else:
    os.execl(sys.executable, sys.executable, *sys.argv)

account_term = float(input("Account contract term(in years) : "))

accumalated_amount = principal_amount * pow((1 + (INTEREST_RATE / interest_compound_rate)),(interest_compound_rate * account_term))

print("Accumulated balance of the account :", format(accumalated_amount,',.2f'))
