user_input = input("How was the day?(hot/cold/other) ").strip().lower()
if user_input == "hot":
    print("It's a hot day!")
    print("Drink planty of water.")
elif user_input == "cold":
    print("It's a cold day!")
    print("Wear warm cloth.")
else:
    print("It's a nice day!")
    print("Enjoy your day!")