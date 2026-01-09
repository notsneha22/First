import csv
import os
import matplotlib.pyplot as plt

FILE_PATH = "expenses.csv"


def initialize_file():
    

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "category", "amount", "description"])


def add_expense():
   
    print("\n--- Add New Expense ---")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food / Travel / Bills etc): ")

    try:
        amount = float(input("Enter amount spent: "))
    except ValueError:
        print("Error: Amount must be a number.")
        return

    description = input("Enter short description: ")

    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully.")


def analyze_expense():
    
    print("\n--- Category-wise Expense Summary ---")
    category_total = {}

    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["category"]
            amount = float(row["amount"])
            category_total[category] = category_total.get(category, 0) + amount

    if not category_total:
        print("No expenses found.")
        return

    for category, total in category_total.items():
        print(f"{category}: ₹{total}")


def category_pie_chart():
    
    category_total = {}

    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["category"]
            amount = float(row["amount"])
            category_total[category] = category_total.get(category, 0) + amount

    if not category_total:
        print("No data available for chart.")
        return

    plt.figure()
    plt.pie(category_total.values(), labels=category_total.keys(), autopct="%1.1f%%")
    plt.title("Category-wise Expense Distribution")
    plt.show()


def monthly_bar_chart():
    
    monthly_total = {}

    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            month = row["date"][:7]  # YYYY-MM
            amount = float(row["amount"])
            monthly_total[month] = monthly_total.get(month, 0) + amount

    if not monthly_total:
        print("No monthly data found.")
        return

    plt.figure()
    plt.bar(monthly_total.keys(), monthly_total.values())
    plt.xlabel("Month")
    plt.ylabel("Total Expense (₹)")
    plt.title("Monthly Expense Summary")
    plt.show()


def budget_alert():
    
    print("\n--- Budget Check ---")
    month = input("Enter month (YYYY-MM): ")

    try:
        budget = float(input("Enter monthly budget amount: "))
    except ValueError:
        print("Error: Budget must be a number.")
        return

    total_spent = 0

    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["date"].startswith(month):
                total_spent += float(row["amount"])

    print(f"Total spent in {month}: ₹{total_spent}")

    if total_spent > budget:
        print("Warning: Budget limit exceeded.")
    else:
        print("You are within the budget.")


def export_report():
    
    month = input("Enter month (YYYY-MM): ")
    category_total = {}

    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["date"].startswith(month):
                category = row["category"]
                amount = float(row["amount"])
                category_total[category] = category_total.get(category, 0) + amount

    if not category_total:
        print("No data available for this month.")
        return

    report_name = f"expense_report_{month}.txt"
    with open(report_name, "w") as file:
        file.write(f"Expense Report for {month}\n")
        file.write("-" * 35 + "\n")
        for category, total in category_total.items():
            file.write(f"{category}: ₹{total}\n")

    print(f"Report saved successfully as '{report_name}'")


def main():
    
    initialize_file()

    while True:
        print("\n====== Personal Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Category-wise Summary")
        print("3. View Category Pie Chart")
        print("4. View Monthly Bar Chart")
        print("5. Check Budget Limit")
        print("6. Export Monthly Report")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            analyze_expense()
        elif choice == "3":
            category_pie_chart()
        elif choice == "4":
            monthly_bar_chart()
        elif choice == "5":
            budget_alert()
        elif choice == "6":
            export_report()
        elif choice == "7":
            print("Thank you for using the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

