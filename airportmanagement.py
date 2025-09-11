import itertools

class Airport:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def show_flights(self):
        print(f"\n✈️ Flights from {self.name}:")
        for flight in self.flights:
            print(f"  {flight.flight_number}: {flight.origin} -> {flight.destination}")


class Flight:
    def __init__(self, flight_number, origin, destination):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def show_passengers(self):
        print(f"\n👥 Passengers on flight {self.flight_number}:")
        if not self.passengers:
            print("  No passengers yet.")
        for p in self.passengers:
            print(f"  - {p.name}, Age: {p.age}")


class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Ticket:
    ticket_counter = itertools.count(1001)

    def __init__(self, flight, passenger):
        self.flight = flight
        self.passenger = passenger
        self.ticket_number = f"T{next(Ticket.ticket_counter)}-{flight.flight_number}"
        flight.add_passenger(passenger)
        self.issue_ticket()

    def issue_ticket(self):
        print(f"🎟️ Ticket Issued: {self.ticket_number} | Passenger: {self.passenger.name} "
              f"| Flight: {self.flight.flight_number}")


# --- System Menu ---
def main():
    airport = Airport("City Airport", "New York")

    # Add some flights
    flight1 = Flight("AA101", "INDIA", "DELHI")
    flight2 = Flight("DL202", "INDIA", "SURAT")
    flight3 = Flight("UA303", "INDIA", "PRAYAGRAJ")
    flight4= Flight("SW404", "INDIA", "MUMBAI")
    

    airport.add_flight(flight1)
    airport.add_flight(flight2)
    airport.add_flight(flight3)
    airport.add_flight(flight4)

    tickets = []

    while True:
        print("\n==== Airport Management System ====")
        print("1. Show Flights")
        print("2. Book Ticket")
        print("3. Show Passengers on a Flight")
        print("4. Search Passenger by Name")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            airport.show_flights()

        elif choice == "2":
            airport.show_flights()
            flight_no = input("Enter Flight Number: ")
            passenger_name = input("Enter Passenger Name: ")
            passenger_age = input("Enter Passenger Age: ")

            # Find the flight
            selected_flight = next((f for f in airport.flights if f.flight_number == flight_no), None)

            if selected_flight:
                passenger = Passenger(passenger_name, passenger_age)
                ticket = Ticket(selected_flight, passenger)
                tickets.append(ticket)
            else:
                print("❌ Flight not found!")

        elif choice == "3":
            flight_no = input("Enter Flight Number: ")
            selected_flight = next((f for f in airport.flights if f.flight_number == flight_no), None)
            if selected_flight:
                selected_flight.show_passengers()
            else:
                print("❌ Flight not found!")

        elif choice == "4":
            search_name = input("Enter Passenger Name to Search: ")
            found = False
            for ticket in tickets:
                if ticket.passenger.name.lower() == search_name.lower():
                    print(f"✅ Found: {ticket.passenger.name} | "
                          f"Ticket: {ticket.ticket_number} | Flight: {ticket.flight.flight_number}")
                    found = True
            if not found:
                print("❌ Passenger not found.")

        elif choice == "5":
            print("👋 Exiting system. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice, try again.")


if __name__ == "__main__":
    main()
