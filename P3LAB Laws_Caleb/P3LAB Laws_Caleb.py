#Caleb Laws
#3/22/2026
#P3LAB - Money Calculator
#This program will calculate the break down of a given amount of money into the number of dollars and coins needed to make that amount.

def main():
    #Get the amount of money from the user
    amount = float(input("Enter the amount of money: "))
    
#conversion to avoid floating point issues
    cents = int(round(amount * 100))
    
# Calculate the dollars
    dollars = cents // 100
    cents = cents % 100

# Calculate the quarters
    quarters = cents // 25
    cents = cents % 25

# Calculate the dimes
    dimes = cents // 10
    cents = cents % 10

# Calculate the nickels
    nickels = cents // 5   
    cents = cents % 5
    
# Calculate the pennies
    pennies = cents // 1

#show the results (only those that are greater than 0)
    if dollars > 0:
        print(f"{dollars} {'Dollar' if dollars == 1 else 'Dollars'}")
    if quarters > 0:
        print(f"{quarters} {'Quarter' if quarters == 1 else 'Quarters'}")
    if dimes > 0:
        print(f"{dimes} {'Dime' if dimes == 1 else 'Dimes'}")
    if nickels > 0:
        print(f"{nickels} {'Nickel' if nickels == 1 else 'Nickels'}")
    if pennies > 0:
        print(f"{pennies} {'Penny' if pennies == 1 else 'Pennies'}")

if __name__ == "__main__":
    main()
