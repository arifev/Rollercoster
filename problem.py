def roller_coaster():
    pay = 15
    print("Welcome to the Roller Coaster ride!")
    print("-----------------------------------")
    name = input("Enter your name: ").capitalize()
    if len(name) >= 3:
        print("You're aligeble for this ride!")
        info = input(f"Thank you so much MR.{name}.\nWe need some info can you give us your info. If you want then type (Y)es or (N)o: ").capitalize()
        if info == "Y":
            print("Ok, we are asking our requeried info!")
            age = int(input("Enter your age: "))
            if age >= 12:
                print("You are passing 1st step...")
                height = int(input("What's your height: "))
                if height >= 120:
                    print("You are passing 2nd step...")
                    weight = int(input("What's your weight: "))
                    if weight >= 30 and weight <= 70:
                        print(f"Hurrey MR.{name} you're passed all the steps...")
                        ticket = input("Please buy a ticket!. Each ticket price is 15$\nIf you want then (Y)es or (N)o: ").capitalize()
                        if ticket == "Y":
                            payment = int(input("Please pay your ticket price: "))
                            if payment == pay:
                                print(f"MR.{name} enjoy your ride...")
                            else:
                                print("Please pay your actual ticket price...")
                        else:
                            print("Ok, good bye...")
                    else:
                        print("You are not requeried weight!")
                else:
                    print("You are not requeried height!")
            else:
                print("You are not requeried age!")
        else:
            print(f"Have a nice day, MR.{name}. Come again!")
    else:
        print("You're name is too short!")
roller_coaster()