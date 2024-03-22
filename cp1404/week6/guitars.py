from guitar import Guitar


def user_guitar():
    name = input("Name: ")
    if name == "":
        print("No blank name.")
        return user_guitar()

    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    return Guitar(name, year, cost)


