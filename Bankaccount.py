# data={}
# # a=input("select : ")
# dontstop=True
# while dontstop:
#     dici={}
#     a=input("select : ")

#     if a=="create_account":
#         # dici={}
#         Name=input("Enter Your Name : ")
#         dici['Name']=Name
#         Age=int(input("Enter Your Age : "))
#         dici['Age']=Age
#         Phone=int(input("Enter Your Mobile Num : "))
#         dici['Phone']=Phone
#         Password=int(input("Set Your Pin : "))
#         dici['Pin']=Password
#         dici['Balance']=0
#         dici['Statement']=[]
#         data[Name]=dici
#         print("Account Created Successfully")

#     elif a=="Exit":
#         dontstop=False

#     elif a=="Deposit":
#         Name=input("Enter Name : ")
#         Amount=int(input("Enter Amount : "))
#         data[Name]['Balance']+=Amount
#         data[Name]['Statement'].append(f"Deposited {Amount}")
#         print("Done !")

#     elif a=="Withdraw":
#         Name=input("Enter Your Name : ")
#         Amount=int(input("Enter Amount to withdraw : "))
#         if data[Name]['Balance'] >= Amount:
#             data[Name]['Balance'] -= Amount
#             data[Name]['Statement'].append(f"Withdrawed {Amount}")
#             print(f"Successfully withdrew {Amount} rupees")
#         else:
#             print("Insufficient balance")
        
#     elif a=="checkbalance":
#         Name=input("Enter Your Name : ")
#         print(f'Your Balance : {data[Name]['Balance']}')
        
#     elif a=="Transfermoney":
#         Name=input("Enter Your Name : ")#Harsha
#         print("Now Enter the person name who you wants to Transfer !")
#         Name2=input("Enter : ")#abhi
#         Amount=int(input("Enter Amount to be transfered : "))
#         if data[Name]['Balance'] >= Amount:
#            data[Name]['Balance'] -= Amount
#            data[Name2]['Balance'] += Amount
#            print("Successfully Amount transferred!")
#         else:
#             print("Insufficient balance")
#         data[Name]['Statement'].append(f"Transfered +{Amount}")
        
#     elif a=="calculate_interest":
#         roi=5
#         Name=input("Enter Your Name : ")
#         Timeperiod=int(input("Enter Num of Years : "))
#         interest=(data[Name]['Balance']*roi*Timeperiod)/100
#         print(f'The interest for {Timeperiod} years is {interest}')

#     elif a=="Display_statement":
#         Name=input("Enter Your Name : ")
#         print(data[Name]['Statement'])

#     elif a=="Admin":
#         password=1213
#         pin=int(input("Enter pin : "))
#         if pin==password:
#             print("1.Create Customer Account \n 2.View All Customer Accounts \n 3.Search Customer by Account Number \n 4. Update customer details \n 5.Delete customer Account\n 6.Freeze Account \n 7.Unfreeze Account \n 8.Reset Customer pin\n 9.view total number of customers\n10.view total bank balance\n 11.view complete transaction history \n 12.apply interest to all customer accounts \n 13.apply service charges \n 14.generate customer report \n 15.backup customer data \n 16.Restore customer data \n 17.Logout \n18.Exit")
#             choose=int(input("Choose option : "))
#             admin_login=True
#             while admin_login:
#                 if choose==1:
#                     print("***create customer account***")
#                     Name=input("Enter Your Name : ")
#                     dici['Name']=Name
#                     Age=int(input("Enter Your Age : "))
#                     dici['Age']=Age
#                     Phone=int(input("Enter Your Mobile Num : "))
#                     dici['Phone']=Phone
#                     dici['Balance']=0
#                     dici['Statement']=[]
#                     data[Name]=dici
#                     print("Account Created Successfully")
#                 elif choose==2:
#                     print("***All customers accounts : ***")  
#                     for i in data:
#                         print(i)
#                 elif choose==3:
#                     print("***Search customer by Name***")
#                     Name=input("Enter customer Name : ")
#                     print(data[Name])
#                 elif choose==4:
#                     print("***update customer details***")
#                     Name=input("Enter customer Name : ")
#                     print("1.Phone\n2.Age\n3.Balance")
#                     choose=int(input("Enter option : "))
#                     if choose==1:
#                         New_Phone=input("Enter New Phone : ")
#                         dici[Name]['Phone']= New_Phone
#                     elif choose==2:
#                         New_Age=int(input("Enter New Age : "))
#                         dici[Name]['Age']=New_Age
#                     elif choose==3:
#                         New_Balance=int(input("Enter New Account balance :"))
#                         dici[Name]['Balance']=New_Balance  
#                 elif choose==5:
#                     print("***Delete Customer Account***")   
#                     Name=input("Enter customer Name : ")
#                     del data[Name]
#                     print("Account deleted successfully")
#                 elif choose==6:
#                     Name=input("Enter customer Account : ")
#                     print(f"{Name}'s Account is Freezed !")      
#                 elif choose==7:
#                     Name=input("Enter customer Account : ")
#                     print(f"{Name}'s Account is Unfreezed !") 
#                 elif choose==8:
#                     print("Reset customer pin : ")
#                     Name=input("Enter customer Account : ")
#                     New_pin=int(input("Enter New Pin : "))
#                     data[Name]['Pin']=New_pin            
#                 elif choose==9:
#                     print("Total Number of customers : ")
#                     print(len(data)) 
#                 elif choose==10:
#                     print("Total balance : ")
#                     total = sum(value["Balance"] for value in data.values())
#                     print(total)       
#                 elif choose==11:
#                     print("***View complete transaction history***")
#                     for value in data.values():
#                         print(value["Name"], value["Statement"])
#                 elif choose==12:
#                     print("Apply interest to all customer accounts") 
#                     roi=int(input("Enter interest : "))    
#                     for account in data.values():
#                         interest = account['Balance'] * roi / 100
#                         account['Balance'] += interest

#                     print("Interest applied to all accounts successfully!")
#                 elif choose==13:
#                     print("***Apply service charges***")
#                     charges=int(input("Enter charges : "))
#                     for account in data.values():
#                         if account['Balance'] >= charges:
#                             account['Balance'] -= charges
#                             account['Statement'].append(f"Service charge: {charges}")
#                         else:
#                             print(f"Insufficient balance for {account['Name']}")
#                     print("Service charges applied to all accounts!")
#                 elif choose==14:
#                     print("***Generate customer report***")            
#                     for account in data.values():
#                         print("-" * 30)
#                         print("Name      :", account['Name'])
#                         print("Age       :", account['Age'])
#                         print("Phone     :", account['Phone'])
#                         print("Balance   :", account['Balance'])
#                         print("Transactions:", len(account['Statement']))
#                         print("-" * 30)
#                 elif choose==15:
#                     print("***Backup customer Data***")
#                     Name=input("Enter customer name : ")
#                     print(f"{Name}'s data is backuped !")
#                 elif choose==16:
#                     print("***Restore customer Data***")
#                     Name=input("Enter customer name : ")
#                     print(f"{Name}'s data is backuped !")
#                 elif choose==17:
#                     print("Logout !")
#                     admin_login=False
#                 elif choose == 18:
#                     print("Thank you for using our banking system!")
#                     dontstop = False
#                     admin_logged_in = False


        
# print(data) 





import json

data = {}

dontstop = True

while dontstop:

    a = input("select : ")

    if a == "create_account":

        dici = {}

        Name = input("Enter Your Name : ")
        dici['Name'] = Name

        Age = int(input("Enter Your Age : "))
        dici['Age'] = Age

        Phone = int(input("Enter Your Mobile Num : "))
        dici['Phone'] = Phone

        Password = int(input("Set Your Pin : "))
        dici['Pin'] = Password

        dici['Balance'] = 0
        dici['Statement'] = []

        data[Name] = dici

        print("Account Created Successfully")

    elif a == "Exit":
        dontstop = False

    elif a == "Deposit":

        Name = input("Enter Name : ")
        Amount = int(input("Enter Amount : "))

        if Name in data:
            data[Name]['Balance'] += Amount
            data[Name]['Statement'].append(f"Deposited {Amount}")
            print("Done !")
        else:
            print("Account not found")

    elif a == "Withdraw":

        Name = input("Enter Your Name : ")
        Amount = int(input("Enter Amount to withdraw : "))

        if Name in data:

            if data[Name]['Balance'] >= Amount:
                data[Name]['Balance'] -= Amount
                data[Name]['Statement'].append(f"Withdrawed {Amount}")
                print(f"Successfully withdrew {Amount} rupees")
            else:
                print("Insufficient balance")

        else:
            print("Account not found")

    elif a == "checkbalance":

        Name = input("Enter Your Name : ")

        if Name in data:
            print(f"Your Balance : {data[Name]['Balance']}")
        else:
            print("Account not found")

    elif a == "Transfermoney":

        Name = input("Enter Your Name : ")

        if Name not in data:
            print("Sender account not found")
            continue

        print("Now Enter the person name who you want to Transfer!")

        Name2 = input("Enter : ")

        if Name2 not in data:
            print("Receiver account not found")
            continue

        Amount = int(input("Enter Amount to be transferred : "))

        if data[Name]['Balance'] >= Amount:

            data[Name]['Balance'] -= Amount
            data[Name2]['Balance'] += Amount

            data[Name]['Statement'].append(
                f"Transferred {Amount} to {Name2}"
            )

            data[Name2]['Statement'].append(
                f"Received {Amount} from {Name}"
            )

            print("Successfully Amount transferred!")

        else:
            print("Insufficient balance")

    elif a == "calculate_interest":

        roi = 5

        Name = input("Enter Your Name : ")

        if Name in data:

            Timeperiod = int(input("Enter Num of Years : "))

            interest = (
                data[Name]['Balance'] * roi * Timeperiod
            ) / 100

            print(
                f"The interest for {Timeperiod} years is {interest}"
            )

        else:
            print("Account not found")

    elif a == "Display_statement":

        Name = input("Enter Your Name : ")

        if Name in data:
            print(data[Name]['Statement'])
        else:
            print("Account not found")

    elif a == "Admin":

        password = 1213
        pin = int(input("Enter pin : "))

        if pin == password:

            admin_login = True

            while admin_login:

                print("""
1. Create Customer Account
2. View All Customer Accounts
3. Search Customer by Account Number
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
15. Backup Customer Data
16. Restore Customer Data
17. Logout
18. Exit
""")

                choose = int(input("Choose option : "))

                # 1. Create Customer Account
                if choose == 1:

                    print("*** Create Customer Account ***")

                    dici = {}

                    Name = input("Enter Your Name : ")
                    dici['Name'] = Name

                    Age = int(input("Enter Your Age : "))
                    dici['Age'] = Age

                    Phone = int(input("Enter Your Mobile Num : "))
                    dici['Phone'] = Phone

                    Password = int(input("Set Your Pin : "))
                    dici['Pin'] = Password

                    dici['Balance'] = 0
                    dici['Statement'] = []

                    data[Name] = dici

                    print("Account Created Successfully")

                # 2. View All Customers
                elif choose == 2:

                    print("*** All Customers Accounts ***")

                    if len(data) == 0:
                        print("No customers found")
                    else:
                        for i in data:
                            print(i)

                # 3. Search Customer
                elif choose == 3:

                    print("*** Search Customer by Name ***")

                    Name = input("Enter customer Name : ")

                    if Name in data:
                        print(data[Name])
                    else:
                        print("Customer not found")

                # 4. Update Customer Details
                elif choose == 4:

                    print("*** Update Customer Details ***")

                    Name = input("Enter customer Name : ")

                    if Name in data:

                        print("""
1. Phone
2. Age
3. Balance
""")

                        option = int(input("Enter option : "))

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
                                input("Enter New Account Balance : ")
                            )

                            data[Name]['Balance'] = New_Balance

                        else:
                            print("Invalid option")

                    else:
                        print("Customer not found")

                # 5. Delete Customer
                elif choose == 5:

                    print("*** Delete Customer Account ***")

                    Name = input("Enter customer Name : ")

                    if Name in data:

                        del data[Name]

                        print("Account deleted successfully")

                    else:
                        print("Customer not found")

                # 6. Freeze Account
                elif choose == 6:

                    Name = input("Enter customer Account : ")

                    if Name in data:

                        print(f"{Name}'s Account is Freezed !")

                    else:
                        print("Customer not found")

                # 7. Unfreeze Account
                elif choose == 7:

                    Name = input("Enter customer Account : ")

                    if Name in data:

                        print(f"{Name}'s Account is Unfreezed !")

                    else:
                        print("Customer not found")

                # 8. Reset Customer Pin
                elif choose == 8:

                    print("*** Reset Customer Pin ***")

                    Name = input("Enter customer Account : ")

                    if Name in data:

                        New_pin = int(
                            input("Enter New Pin : ")
                        )

                        data[Name]['Pin'] = New_pin

                        print("Pin updated successfully")

                    else:
                        print("Customer not found")

                # 9. Total Customers
                elif choose == 9:

                    print(
                        "Total Number of customers : ",
                        len(data)
                    )

                # 10. Total Bank Balance
                elif choose == 10:

                    total = sum(
                        value["Balance"]
                        for value in data.values()
                    )

                    print("Total balance :", total)

                # 11. Complete Transaction History
                elif choose == 11:

                    print("*** Complete Transaction History ***")

                    for value in data.values():

                        print("-" * 30)

                        print("Customer :", value["Name"])

                        if len(value["Statement"]) == 0:
                            print("No transactions")

                        else:
                            for transaction in value["Statement"]:
                                print(transaction)

                        print("-" * 30)

                # 12. Apply Interest
                elif choose == 12:

                    print(
                        "*** Apply Interest to All Customer Accounts ***"
                    )

                    roi = int(
                        input("Enter interest rate (%) : ")
                    )

                    for account in data.values():

                        interest = (
                            account['Balance'] * roi
                        ) / 100

                        account['Balance'] += interest

                        account['Statement'].append(
                            f"Interest credited: {interest}"
                        )

                    print(
                        "Interest applied to all accounts successfully!"
                    )

                # 13. Apply Service Charges
                elif choose == 13:

                    print("*** Apply Service Charges ***")

                    charges = int(
                        input("Enter charges : ")
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
                        "Service charges applied to all accounts!"
                    )

                # 14. Generate Customer Report
                elif choose == 14:

                    print("*** Generate Customer Report ***")

                    if len(data) == 0:
                        print("No customers found")

                    else:

                        for account in data.values():

                            print("-" * 30)

                            print(
                                "Name         :",
                                account['Name']
                            )

                            print(
                                "Age          :",
                                account['Age']
                            )

                            print(
                                "Phone        :",
                                account['Phone']
                            )

                            print(
                                "Balance      :",
                                account['Balance']
                            )

                            print(
                                "Transactions :",
                                len(account['Statement'])
                            )

                            print("-" * 30)

                # 15. Backup Customer Data
                elif choose == 15:

                    print("*** Backup Customer Data ***")

                    Name=input("Enter Customer name :")
                    print(f"{Name} Data Backuped !")

                # 16. Restore Customer Data
                elif choose == 16:

                    print("*** Restore Customer Data ***")
                    Name=input("Enter Customer name :")
                    print(f"{Name} Data Restored !")
                    

                # 17. Logout
                elif choose == 17:

                    print("Admin logged out successfully!")

                    admin_login = False

                # 18. Exit
                elif choose == 18:

                    print(
                        "Thank you for using our banking system!"
                    )

                    admin_login = False
                    dontstop = False

                else:

                    print("Invalid option")

        else:

            print("Wrong admin pin")


print(data)