from unreliable_car import UnreliableCar


def main():
    my_car = UnreliableCar("Unreliable", 77, 33)
    print("Attempting to drive 50km:")
    print("Distance driven:", my_car.drive(77))
    print("Attempting to drive 50km again:")
    print("Distance driven:", my_car.drive(33))


main()
