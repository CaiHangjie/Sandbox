from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    more_guitars = True

    while more_guitars:
        name = input("Name: ")
        if name:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"{new_guitar} added.\n")
        else:
            more_guitars = False

    print("\n...snip...")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
