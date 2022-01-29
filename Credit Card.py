import pandas as pd
from decimal import Decimal

# Define function for cashback percentage
def new_column(row):
    if row['Category'] == "Restaurants":
        return restaurant_cb
    elif row['Category'] == "Auto + Gas":
        return gas_cb
    elif row['Category'] == "Groceries":
        return grocery_cb     
    else:
        return misc_cb

def bounded_input(value_name, lower_limit, upper_limit):
    valid_input = False
    inp = 0
    while (not valid_input):
        inp = input("Please input {} as a percent: ".format(value_name))
        inp = Decimal(inp)
        if(inp > upper_limit or inp < lower_limit):
            print("Input is out of bounds. Please input a value between {0} and {1} percent.".format(lower_limit, upper_limit))
        else:
            inp /= 100
            valid_input = True
    return inp

#User input
cardname = input("Enter Card Name: ")

#restaurant_cb = input('Enter Restaurant Cashback Percentage as Decimal:')
restaurant_cb = bounded_input('Restaurant Cashback', 0, 5)
print(restaurant_cb)

#gas_cb = input('Enter Auto & Gas Cashback Percentage as Decimal:')
gas_cb = bounded_input('Auto + Gas Cashback', 0, 5)
print(gas_cb)

#grocery_cb = input('Enter Grocery Cashback Percentage as Decimal:')
grocery_cb = bounded_input('Grocery Cashback', 0, 5)
print(grocery_cb)

#misc_cb = input('Enter All Other Cashback Percentage as Decimal:')
misc_cb = bounded_input('All Other Cashback', 0, 5)
print(misc_cb)

quit()


# reading the CSV file
df = pd.read_csv('CreditCardSample.csv')

#Find all rows with purchases
filtered_df = df.loc[df['Withdrawals'].notnull()].copy()

#Convert Withdrawals to number
filtered_df['Withdrawals'] = filtered_df['Withdrawals'].replace('[\$,]', '', regex=True).astype(float)

filtered_df['CashbackPercentage'] = filtered_df.apply(new_column, axis=1)

filtered_df['CashbackPercentage'] = filtered_df['CashbackPercentage'].astype("float")

filtered_df['Cashback'] = filtered_df['Withdrawals'] * filtered_df["CashbackPercentage"]

#Output
cashback_sum = sum(filtered_df['Cashback'])
print(cardname, "cashback is: ", cashback_sum ) 
