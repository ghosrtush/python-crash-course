number_of_people = int(input("How many people are comming?: "))

if number_of_people > 10:
    print("We do not have enough seats")
else:
    print(f"{number_of_people} people will fit")