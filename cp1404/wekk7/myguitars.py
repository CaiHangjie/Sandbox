from guitar import Guitar
import csv


def enter_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars_files(filename, guitars):
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for guitar in guitars:
            csv_writer.writerow([guitar.name, guitar.year, guitar.cost])


def sort_by_year(guitar):
    return guitar.year


def main():
    filename = 'guitars.csv'
    guitars = enter_guitars(filename)
    print("These are old guitars:")
    for guitar in guitars:
        print(guitar)

    guitars.sort(key=sort_by_year)

    print("\nGuitars sorted by year (oldest to newest):")
    for guitar in guitars:
        print(guitar)

    print("\nPlease input your new guitar:")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)

    save_guitars_files(filename, guitars)


main()
