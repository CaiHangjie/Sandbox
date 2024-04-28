from silver_service_taxi import SilverServiceTaxi

hummer_taxi = SilverServiceTaxi("Hummer", 200, 2, 2.50)

hummer_taxi.drive(18)

print("SilverServiceTaxi details:")
print(hummer_taxi)


fare = 48.78
assert hummer_taxi.get_fare() == fare
print(f"Fare: ${fare:.2f}")
print(f"Actual fare: ${hummer_taxi.get_fare():.2f}")
