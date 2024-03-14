"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        bonus = calculate_bonus(sales)
        print(f"{bonus}")
        sales = float(input("Enter sales: $"))
    print("Do next thing")


def calculate_bonus(sales):
    if sales < 1000:
        bonus = sales * 0.1
    elif sales >= 1000:
        bonus = sales * 0.15
    return bonus


main()
