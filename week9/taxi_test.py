from taxi import Taxi

# Create a new taxi object
first_taxi = Taxi("Prius 1", 100, 1.23)

# Drive the taxi 40 km
first_taxi.drive(40)

# Print the taxi's details and the current fare
print("Taxi details:")
print(first_taxi)

# Restart the meter (start a new fare) and then drive the car 100 km
first_taxi.start_fare()
first_taxi.drive(100)

# Print the details and the current fare
print("Taxi details :")
print(first_taxi)
