def print_itineraries(itineraries):
    for i, (traveler_name, origin, destination) in enumerate(itineraries, 1):
        print(f"Itinerary {i}: {traveler_name} - From {origin} to {destination}")

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print_itineraries(itineraries)