import pandas as pd

#User input
cardname = input("Enter Card Name: ")

restaurant_cb = input('Enter Restaurant Cashback Percentage as Decimal:')
gas_cb = input('Enter Auto & Gas Cashback Percentage as Decimal:')
grocery_cb = input('Enter Grocery Cashback Percentage as Decimal:')
misc_cb = input('Enter All Other Cashback Percentage as Decimal:')

csv_input = input('Enter path of desired PNC credit card data: ')

# reading the CSV file
df = pd.read_csv(csv_input)

#Find all rows with purchases
filtered_df = df.loc[df['Withdrawals'].notnull()]

#Convert Withdrawals to number
filtered_df['Withdrawals'] = filtered_df['Withdrawals'].replace('[\$,]', '', regex=True).astype(float)

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

filtered_df['CashbackPercentage'] = filtered_df.apply(new_column, axis=1)

filtered_df['CashbackPercentage'] = filtered_df['CashbackPercentage'].astype("float")

filtered_df['Cashback'] = filtered_df['Withdrawals'] * filtered_df["CashbackPercentage"]

#Output
cashback_sum = sum(filtered_df['Cashback'])
print(cardname, "cashback is: ", cashback_sum ) 
