password = "123"
username = "abc"
def load_bus_data():
    try:
        with open('bus_data.txt', 'r') as f:
            return [line.strip().split(',') for line in f.readlines()]
    except FileNotFoundError:
        return []

def load_booking_data():
    try:
        with open('booking_data.txt', 'r') as f:
            return [line.strip().split(',') for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_data(bus_data, booking_data):
    with open('bus_data.txt', 'w') as f:
        for bus in bus_data:
            f.write(','.join(map(str, bus)) + '\n')

    with open('booking_data.txt', 'w') as f:
        for booking in booking_data:
            f.write(','.join(map(str, booking)) + '\n')

# Add the content-writing script here
with open('bus_data.txt', 'w') as bus_file:
    bus_file.write("1,Urban transport,20,10\n")
    bus_file.write("2,Greenline transport,30,15\n")
    bus_file.write("3,Night owl express,15,8\n")
    bus_file.write("4,Madhavi travels,20,8\n")
    bus_file.write("5,GoldenGate shuttle,30,8\n")

with open('booking_data.txt', 'w') as booking_file:
    booking_file.write("2,meyyappan,diya\n")
    booking_file.write("1,anushka,jayasree,deborah\n")
    booking_file.write("3,radhi\n")

def display_options():
    print("\n1. View Bus List")
    print("2. Book Tickets")
    print("3. Cancel Booking")
    print("4. Bus Status Board")
    print("5. Exit")

# ... (rest of your code remains the same)
def view_bus_list(bus_data):
    print("\nBus List:")
    for bus in bus_data:
        print(f"{bus[0]}: {bus[1]} - Seats available: {bus[2]}")

def book_tickets(bus_data, booking_data):
    view_bus_list(bus_data)
    bus_number = input("\nEnter the bus number you want to book tickets for: ")

    for bus in bus_data:
        if bus[0] == bus_number and int(bus[2]) > 0:
            num_seats = int(input("Enter the number of seats you want to book: "))
            if num_seats <= int(bus[2]):
                passengers = []
                for i in range(num_seats):
                    name = input(f"Enter the name of passenger {i + 1}: ")
                    passengers.append(name)

                booking_details = [bus_number] + passengers
                booking_data.append(booking_details)
                bus[2] = str(int(bus[2]) - num_seats)
                print(f"Booking successful! Total fare: {num_seats * int(bus[3])}")
                save_data(bus_data, booking_data)
                return
            else:
                print("Not enough seats available.")
                return

    print("Bus not found or no seats available.")

def cancel_booking(bus_data, booking_data):
    view_bookings(booking_data)
    booking_number = int(input("\nEnter the booking number you want to modify: "))

    if 1 <= booking_number <= len(booking_data):
        booking_to_cancel = booking_data[booking_number - 1]
        bus_number = booking_to_cancel[0]

        print(f"\nBooking Details: Bus {bus_number}: {', '.join(booking_to_cancel[1:])}")
        passenger_to_cancel = input("Enter the name of the passenger you want to cancel: ")

        if passenger_to_cancel in booking_to_cancel[1:]:
            booking_to_cancel.remove(passenger_to_cancel)
            for bus in bus_data:
                if bus[0] == bus_number:
                    bus[2] = str(int(bus[2]) + 1)
                    print(f"Passenger {passenger_to_cancel} canceled successfully.")
                    save_data(bus_data, booking_data)
                    return
        else:
            print("Passenger not found in the booking.")

    print("Invalid booking number.")


def view_bookings(booking_data):
    print("\nBooking List:")
    for i, booking in enumerate(booking_data, start=1):
        print(f"{i}. Bus {booking[0]}: {', '.join(booking[1:])}")

def bus_status_board(bus_data):
    print("\nBus Status Board:")
    for bus in bus_data:
        print(f"Bus {bus[0]} - Seats available: {bus[2]}")

def main_menu():
    bus_data = load_bus_data()
    booking_data = load_booking_data()

    name = input("enter name: ")
    passwd = input("enter password: ")

    while name==username and passwd==password:
        print("\nWelcome to the Bus Booking System!")
        display_options()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_bus_list(bus_data)
        elif choice == '2':
            book_tickets(bus_data, booking_data)
        elif choice == '3':
            cancel_booking(bus_data, booking_data)
        elif choice == '4':
            bus_status_board(bus_data)
        elif choice == '5':
            print("Thank you for using the Bus Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main_menu()

