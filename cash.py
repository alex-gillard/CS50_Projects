# TODO
from cs50 import get_float

def main():
    # Ask how many cents is owed
    cents = get_cents()

    # Calculate number of quarters to give to customer
    quarters = calc_quarters(cents)
    cents = cents - quarters * 25

    # Calculate number of dimes to give to customer
    dimes = calc_dimes(cents)
    cents = cents - dimes * 10

    # Calculate number of nickels to give to customer
    nickels = calc_nickels(cents)
    cents = cents - nickels * 5

    # Calculate number of pennies to give to customer
    pennies = cents

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print total number of coins to give to customer
    print(coins)



def get_cents():
    while True:
        dollars = get_float("Change owed: ")
        if dollars > -1:
            cents = round(dollars * 100)
            return cents


def calc_quarters(cents):
    calc_quart = cents // 25
    return calc_quart

def calc_dimes(cents):
    calc_dime = cents // 10
    return calc_dime

def calc_nickels(cents):
    calc_nickel = cents // 5
    return calc_nickel

def calc_pennies(cents):
    calc_penny = cents // 1
    return calc_penny


main()