movies = [
    {
        "name": "KGF",
        "shows": ["2:30PM", "6:30PM", "9:30PM"],
        "seats": ["A1","A2","A3","B1","B2","B3","C1","C2","C3"],
        "price": 250
    },
    {
        "name": "Pushpa",
        "shows": ["2:30PM", "6:30PM", "9:30PM"],
        "seats": ["A1","A2","A3","B1","B2","B3","C1","C2","C3"],
        "price": 275
    },
    {
        "name": "Peddi",
        "shows": ["2:30PM", "6:30PM", "9:30PM","11:30PM"],
        "seats": ["A1","A2","A3","B1","B2","B3","C1","C2","C3"],
        "price": 350
    }
]


bookings = []


while True:

    print("\n1. User")
    print("2. Admin")
    print("3. Exit")

    choice = input("Choose option: ")
    if choice.isdigit():
        choice=int(choice)


    # USER

    if choice == 1:


        print("\nAVAILABLE MOVIES")

        for movie in movies:
            print("----------------")
            print("Movie :", movie["name"])
            print("Shows :", movie["shows"])
            print("Price :", movie["price"])



        # Movie selection

        while True:

            movie_name = input("\nWhich movie you want: ")

            selected_movie = None


            for movie in movies:

                if movie["name"].lower() == movie_name.lower():
                    selected_movie = movie
                    break



            if selected_movie:
                break

            else:

                print("\nMovie not available.")
                print("Available movies:")

                for movie in movies:
                    print("-",movie["name"])




        # Show selection

        while True:

            show_time = input("Which show time: ").upper()


            if show_time in selected_movie["shows"]:
                break

            else:
                print("Show not available")
                print("Available shows:",selected_movie["shows"])




        # Seat booking

        while True:


            print("\nAvailable Seats:")
            print(selected_movie["seats"])


            seats = input(
                "Enter seats (A1,A2,A3): "
            )


            seats = seats.replace(","," ").split()



            invalid = []

            for seat in seats:

                if seat not in selected_movie["seats"]:
                    invalid.append(seat)



            if invalid:

                print(
                    invalid,
                    "not available. Select another seat"
                )

            else:

                break




        for seat in seats:
            selected_movie["seats"].remove(seat)



        amount = len(seats) * selected_movie["price"]



        print("\n===== BOOKING SUCCESS =====")

        print("Movie :",selected_movie["name"])
        print("Show  :",show_time)
        print("Seats :",seats)
        print("Amount:",amount)



        bookings.append({

            "Movie":selected_movie["name"],
            "Show":show_time,
            "Seats":seats,
            "Amount":amount

        })



    # ADMIN


    elif choice == 2:


        pin = 1234

        entered_pin = int(input("Enter Admin Pin: "))


        if entered_pin != pin:

            print("Wrong Pin")
            continue



        while True:


            print("\nADMIN MENU")

            print("1. Add Movie")
            print("2. Add Show")
            print("3. Manage Seats")
            print("4. Delete Movie")
            print("5. View Bookings")
            print("6. Exit Admin")


            option = int(input("Choose option: "))


            # Add movie

            if option == 1:


                name = input("Movie name: ")


                exists = False


                for movie in movies:

                    if movie["name"].lower()==name.lower():
                        exists=True



                if exists:

                    print("Movie already exists")


                else:

                    price=int(input("Price: "))


                    movies.append({

                        "name":name,
                        "shows":[],
                        "seats":[
                            "A1","A2","A3",
                            "B1","B2","B3",
                            "C1","C2","C3"
                        ],
                        "price":price

                    })


                    print("Movie Added")




            # Add show

            elif option == 2:


                for i,movie in enumerate(movies):

                    print(i+1,movie["name"])



                index=int(input("Select movie: "))-1


                show=input("Enter show time: ").upper()


                movies[index]["shows"].append(show)


                print("Show Added")




            # Manage seats

            elif option == 3:


                for i,movie in enumerate(movies):

                    print(i+1,movie["name"])



                index=int(input("Select movie: "))-1



                seats=input(
                    "Enter seats: "
                ).replace(","," ").split()



                movies[index]["seats"]=seats


                print("Seats Updated")




            # Delete movie

            elif option == 4:


                for i,movie in enumerate(movies):

                    print(i+1,movie["name"])



                index=int(input("Select movie: "))-1


                movies.pop(index)


                print("Movie Deleted")




            # View bookings

            elif option == 5:


                if not bookings:

                    print("No bookings")


                else:


                    for booking in bookings:

                        print("\n----------------")

                        print("Movie :",booking["Movie"])
                        print("Show :",booking["Show"])
                        print("Seats:",booking["Seats"])
                        print("Amount:",booking["Amount"])




            elif option == 6:

                break


            else:

                print("Invalid option")




    # EXIT 


    elif choice == 3:

        print("Thank You!")
        break



    else:

        print("Invalid choice")