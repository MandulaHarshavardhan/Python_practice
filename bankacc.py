data={}
# a=input("select : ")

def create_account():
        dici={}
        Name=input("Enter Your Name : ")
        dici['Name']=Name
        Age=int(input("Enter Your Age : "))
        dici['Age']=Age
        Phone=int(input("Enter Your Mobile Num : "))
        dici['Phone']=Phone
        dici['Balance']=0
        dici['Statement']=[]
        data[Name]=dici
        print("Account Created Successfully")


def Deposit():
        Name=input("Enter Name : ")
        Amount=int(input("Enter Amount : "))
        data[Name]['Balance']+=Amount
        data[Name]['Statement'].append(f"Deposited {Amount}")
        print(f"Successfully Deposited {Amount} rupees!")

def Withdraw():
        Name=input("Enter Your Name : ")
        Amount=int(input("Enter Amount to withdraw : "))
        data[Name]['Balance']-=Amount
        data[Name]['Statement'].append(f"Withdrawed {Amount}")
        print(f"Successfully withdrawed {Amount} rupees")
        
def checkbalance():
        Name=input("Enter Your Name : ")
        print(f"Your Balance : {data[Name]['Balance']}")
        
def Transfermoney():
        Name=input("Enter Your Name : ")#Harsha
        # print("Now Enter the person name who you wants to Transfer !")
        Name2=input("Enter receiver name : ")#abhi
        Amount=int(input("Enter Amount to be transfered : "))
        data[Name]['Balance']-=Amount
        data[Name2]['Balance']+=Amount
        print("Successfully Amount transfered ! ")
        data[Name]['Statement'].append(f"Transfered {Amount} rupees to {Name2}")
        
def calculate_interest():
        roi=5
        Name=input("Enter Your Name : ")
        Timeperiod=int(input("Enter Num of Years : "))
        interest=(data[Name]['Balance']*roi*Timeperiod)/100
        print(f'The interest for {Timeperiod} years is {interest}')

def Display_statement():
        Name=input("Enter Your Name : ")
        print(data[Name]['Statement'])
def view_all_customers():

    print("*** All Customers ***")

    if len(data) == 0:
        print("No customers found")

    else:
        for customer in data:
            print(customer)


def search_customer():

    Name = input("Enter customer Name : ")

    if Name in data:
        print(data[Name])
    else:
        print("Customer not found")


def update_customer():

    Name = input("Enter customer Name : ")

    if Name not in data:
        print("Customer not found")
        return

    print("""
1. Phone
2. Age
3. Balance
""")

    option = int(
        input("Enter option : ")
    )

    if option == 1:

        New_Phone = int(
            input("Enter New Phone : ")
        )

        data[Name]['Phone'] = New_Phone

    elif option == 2:

        New_Age = int(
            input("Enter New Age : ")
        )

        data[Name]['Age'] = New_Age

    elif option == 3:

        New_Balance = int(
            input("Enter New Balance : ")
        )

        data[Name]['Balance'] = New_Balance

    else:
        print("Invalid option")
        return

    print("Customer details updated successfully!")


def delete_customer():

    Name = input("Enter customer Name : ")

    if Name in data:

        del data[Name]

        print("Account deleted successfully")

    else:
        print("Customer not found")


def freeze_account():

    Name = input("Enter customer Name : ")

    if Name in data:

        data[Name]['Frozen'] = True

        print(f"{Name}'s Account is Frozen!")

    else:
        print("Customer not found")


def unfreeze_account():

    Name = input("Enter customer Name : ")

    if Name in data:

        data[Name]['Frozen'] = False

        print(f"{Name}'s Account is Unfrozen!")

    else:
        print("Customer not found")


def reset_pin():

    Name = input("Enter customer Name : ")

    if Name in data:

        New_pin = int(
            input("Enter New Pin : ")
        )

        data[Name]['Pin'] = New_pin

        print("Pin updated successfully")

    else:
        print("Customer not found")


def total_customers():

    print(
        "Total Number of customers :",
        len(data)
    )


def total_bank_balance():

    total = sum(
        value['Balance']
        for value in data.values()
    )

    print("Total Bank Balance :", total)


def complete_transaction_history():

    print("*** Complete Transaction History ***")

    for account in data.values():

        print("-" * 40)
        print("Customer :", account['Name'])

        if len(account['Statement']) == 0:
            print("No transactions")

        else:

            for transaction in account['Statement']:
                print(transaction)

        print("-" * 40)


def apply_interest_all():

    roi = int(
        input("Enter interest rate (%) : ")
    )

    for account in data.values():

        interest = (
            account['Balance']
            * roi
        ) / 100

        account['Balance'] += interest

        account['Statement'].append(
            f"Interest credited: {interest}"
        )

    print(
        "Interest applied to all accounts successfully!"
    )


def apply_service_charges():

    charges = int(
        input("Enter service charge : ")
    )

    for account in data.values():

        if account['Balance'] >= charges:

            account['Balance'] -= charges

            account['Statement'].append(
                f"Service charge: {charges}"
            )

        else:

            print(
                f"Insufficient balance for "
                f"{account['Name']}"
            )

    print(
        "Service charges applied successfully!"
    )


def customer_report():

    print("*** Customer Report ***")

    if len(data) == 0:
        print("No customers found")
        return

    for account in data.values():

        print("-" * 40)

        print("Name         :", account['Name'])
        print("Age          :", account['Age'])
        print("Phone        :", account['Phone'])
        print("Balance      :", account['Balance'])
        print(
            "Transactions :",
            len(account['Statement'])
        )

        print("-" * 40)
def Admin():

    admin_password = 1213

    pin = int(
        input("Enter Admin Pin : ")
    )

    if pin != admin_password:

        print("Wrong Admin Pin!")
        return "LOGOUT"

    print("Admin Login Successful!")

    while True:

        print("""
================ ADMIN MENU ================

1. Create Customer Account
2. View All Customer Accounts
3. Search Customer
4. Update Customer Details
5. Delete Customer Account
6. Freeze Account
7. Unfreeze Account
8. Reset Customer Pin
9. View Total Number of Customers
10. View Total Bank Balance
11. View Complete Transaction History
12. Apply Interest to All Customer Accounts
13. Apply Service Charges
14. Generate Customer Report
15. Logout
16. Exit

=============================================
""")

        choose = int(
            input("Choose option : ")
        )

        if choose == 1:

            create_account()

        elif choose == 2:

            view_all_customers()

        elif choose == 3:

            search_customer()

        elif choose == 4:

            update_customer()

        elif choose == 5:

            delete_customer()

        elif choose == 6:

            freeze_account()

        elif choose == 7:

            unfreeze_account()

        elif choose == 8:

            reset_pin()

        elif choose == 9:

            total_customers()

        elif choose == 10:

            total_bank_balance()

        elif choose == 11:

            complete_transaction_history()

        elif choose == 12:

            apply_interest_all()

        elif choose == 13:

            apply_service_charges()

        elif choose == 14:

            customer_report()

        elif choose == 15:

            print("Admin Logged Out!")
            return "LOGOUT"

        elif choose == 16:

            print(
                "Thank you for using our banking system!"
            )

            return "EXIT"

        else:

            print("Invalid Admin option!")

        
while True:

    a = input("Select : ")

    if a == "create_account":
        create_account()

    elif a == "Deposit":
        Deposit()

    elif a == "Withdraw":
        Withdraw()

    elif a == "checkbalance":
        checkbalance()

    elif a == "Transfermoney":
        Transfermoney()

    elif a == "calculate_interest":
        calculate_interest()

    elif a == "Display_statement":
        Display_statement()
    
    elif a == "Exit":
        break
    else:
        print("Sorry , You've Entered Invalid input !")