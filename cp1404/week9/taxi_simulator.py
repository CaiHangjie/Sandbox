from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def list_of_available_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(taxi):
    if taxi is None:
        print("You need to choose a taxi before you can drive")
        return
    distance = float(input("Drive how far? "))
    taxi.drive(distance)
    print(f"Your {taxi.name} trip cost you ${taxi.get_fare():.2f}")


def choose_taxi(taxis):
    list_of_available_taxis(taxis)
    choice = input("Choose taxi: ")

    if choice.isdigit():
        choice = int(choice)
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    else:
        print("Invalid input")

    return None


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    current_taxi = None

    print("Let's drive!")
    while True:
        choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
        print(f"Bill to date: ${bill_to_date:.2f}")
        if choice == 'q':
            print(f"Total trip cost: ${bill_to_date:.2f}")
            print("Taxis are now:")
            list_of_available_taxis(taxis)
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            drive_taxi(current_taxi)
            if current_taxi:
                bill_to_date += current_taxi.get_fare()
        else:
            print("Invalid option")

main()
