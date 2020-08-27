"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
def main():
    sales_ammount = float(input("What is the Sales Amount?: "))
    if sales_ammount < 1000:
        bonus = sales_ammount * 0.10
    else:
        bonus = sales_ammount * 0.15
    print("Your Bonus:", bonus)


main()
