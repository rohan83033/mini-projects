# Make python airport management system where there are four class Airport, Flight, Passenger, Ticket.

class Airport:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

class Flight:
    def __init__(self, flight_number, origin, destination):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Ticket:
    def __init__(self, flight, passenger):
        self.flight = flight
        self.passenger = passenger
        self.ticket_number = f"{flight.flight_number}-{passenger.name.replace(' ', '').upper()}"
        flight.add_passenger(passenger)
        self.issue_ticket()
    def issue_ticket(self):
        print(f"Ticket Issued: {self.ticket_number} for {self.passenger.name} on flight {self.flight.flight_number}")
# Example usage:
if __name__ == "__main__":
    airport = Airport("City Airport", "New York")
    flight1 = Flight("AA101", "New York", "Los Angeles")
    flight2 = Flight("DL202", "New York", "Chicago")

    airport.add_flight(flight1)
    airport.add_flight(flight2)

    passenger1 = Passenger("John Doe", 30)
    passenger2 = Passenger("Jane Smith", 25)

    ticket1 = Ticket(flight1, passenger1)
    ticket2 = Ticket(flight2, passenger2)
    ticket3 = Ticket(flight1, passenger2)

