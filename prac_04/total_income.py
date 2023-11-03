"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
#commit but don't commit AND push otherwise can't modify or undo existing commits!!!


def main():
    """Generate income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    display_income_report(incomes)


def display_income_report(incomes):
    """Calculate the total income and display the income report"""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
