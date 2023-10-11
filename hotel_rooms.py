hotel = {
    "1": {
        "185": ["George Jefferson", "Wheezy Jefferson"],
    },
    "2": {
        "237": ["Jack Torrance", "Wendy Torrance"],
    },
    "3": {"333": ["Neo", "Trinity", "Morpheus"]},
}

welcome = input("Checking in or out?: ")

if welcome == "in":
    print("You are checking in.")
    room_occupied = True

    while room_occupied:
        room_number = input("Pick a room number: ")
        room_occupied = any(room_number in hotel[key] for key in hotel)

        if room_occupied:
            print("That room is occupied. Please choose a different room number.")
        else:
            print("That room is available")
            occupant_num = int(input("How many people are staying?: "))
            occupant_names = []
            for i in range(occupant_num):
                occupant_name = input(f"Enter name of occupant {i + 1}: ")
                occupant_names.append(occupant_name)
            hotel[str(len(hotel) + 1)] = {room_number: occupant_names}

elif welcome == "out":
    print("You are checking out.")
    checkout_room = input("What room are you checking out of? ")
    room_found = False

    while not room_found:
        for key in hotel:
            if checkout_room in hotel[key]:
                del hotel[key][checkout_room]
                print(f"You have been checked out of room {checkout_room}")
                room_found = True
                break
        else:
            print("That is not your room number. Please try again.")
        if not room_found:
            checkout_room = input("What room are you checking out of? ")

else:
    print("Invalid input. You can only check in or out.")

print(hotel)
