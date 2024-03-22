import csv


def main():
    champions = {}
    countries = {}
    filename = "wimbledon.csv"
    data_file(filename, champions, countries)
    show_champions(champions)
    display_countries(countries)


def data_file(filename, champions, countries):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        extract_csv = csv.reader(in_file)
        next(extract_csv)  # Skip header row
        for row in extract_csv:
            champion = row[2]  # Change the index to 2 to correctly read the champion's name
            country = row[1]

            champions[champion] = champions.get(champion, 0) + 1
            countries[country] = countries.get(country, 0) + 1


def show_champions(champions):
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion}: {count}")


def display_countries(countries):
    print(f"These {len(countries)} countries have won Wimbledon:")
    country_list = list(countries.keys())
    print(", ".join(country_list))


main()
