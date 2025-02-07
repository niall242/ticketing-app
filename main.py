# This is a ticketing app for the Centrala underground system 
# Please open readme file for a detailed app description

from tkinter import *
from tkinter import messagebox
import os
import datetime  
import uuid    # Generates unique IDs

# List of stations and zones
stations = [
    "Erean", "Brunad", "Marend", "Ryall", "Pryn", "Ederif", "Ruril",
    "Holmer", "Vertwall", "Adohad", "Elyot", "Keivia", "Perinad", "Zord",
    "Quthiel", "Riclya", "Agralle", "Docia", "Stonyam", "Obelyn", "Ralith",
    "Garion", "Sylas", "Oloadus", "Riladia", "Wicyt", "Yaen", "Rede", "Bylyn",
    "Frestin", "Soth", "Lomil", "Ninia", "Tallan", "Jaund", "Centrala"
]

DOWNTOWN = ["Erean", "Brunad", "Marend", "Ryall", "Pryn", "Ederif", "Ruril",
            "Holmer", "Vertwall", "Adohad", "Elyot", "Keivia", "Perinad", "Zord"]

MIDTOWN = ["Quthiel", "Riclya", "Agralle", "Docia", "Stonyam", "Obelyn", "Ralith",
        "Garion", "Sylas", "Oloadus", "Riladia", "Wicyt"]

CENTRAL = ["Yaen", "Rede", "Bylyn", "Frestin", "Soth", "Lomil", "Ninia",
        "Tallan", "Jaund", "Centrala"]

# Global variables
current_screen = None
selected_tickets = {"adult": 0, "child": 0, "senior": 0, "student": 0}

map_image_path = os.path.join(os.path.dirname(__file__), "smaller-map.PNG")  # Path to the map image

# Initialize the main window
window = Tk()
window.title("Centrala Underground Ticket App")
window.geometry("1000x600")

start_zone = StringVar(value="None")  # Default to no selection
destination_zone = StringVar(value="None")  # Default to no selection

class TravelTicket:
    # Represents a travel ticket with relevant details
    def __init__(self, start_zone, destination_zone, selected_tickets_summary, total_price):
        self.ticket_id = str(uuid.uuid4())[:8]  # Generate a short unique ID
        self.timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.start_zone = start_zone
        self.destination_zone = destination_zone
        self.selected_tickets_summary = selected_tickets_summary
        self.total_price = total_price

    # Method that could be used on a printer
    def print_ticket(self):
        """Returns a formatted string representing the ticket for future printing."""
        ticket_text = f"--- Centrala Underground Travel Ticket ---\n"
        ticket_text += f"Ticket ID: {self.ticket_id}\n"
        ticket_text += f"Time and Date: {self.timestamp}\n"
        ticket_text += f"From: {self.start_zone}\n"
        ticket_text += f"To: {self.destination_zone}\n"
        ticket_text += f"Tickets:\n"
        
        for ticket_type, quantity in self.selected_tickets_summary.items():
            ticket_text += f"  {ticket_type}: {quantity}\n"

        ticket_text += f"Total Price: ${self.total_price:.2f}\n"
        ticket_text += f"------------------------------------------"
        
        return ticket_text

# The window must be reset after every new screen
def reset_window():
    for widget in window.winfo_children():
        widget.destroy()

# Error messages when the correct buttons are not pressed
def show_error(message):
    messagebox.showerror("Error", message)

# Welcome screen
def screen_1():
    reset_window()

    Label(window, text="Welcome to Centrala Underground", font=("Arial", 18, "bold")).pack(pady=5)

    # Map display
    map_image = PhotoImage(file=map_image_path) 
    map_label = Label(window, image=map_image)
    map_label.pack(pady=0)
    window.map_image = map_image  # Prevent garbage collection

    # Table display
    table_frame = Frame(window)
    table_frame.pack(fill=BOTH, pady=0)

    # Central zone station list
    central_frame = Frame(table_frame)
    central_frame.pack(fill=X, pady=5)
    Label(central_frame, text="Central Zone (Pink/Grey): ", font=("Arial", 14, "bold"), anchor="w").pack(side=LEFT)
    Label(central_frame, text=", ".join(sorted(CENTRAL)), font=("Arial", 14), anchor="w").pack(side=LEFT, padx=5)

    # Midtown zone station list
    midtown_frame = Frame(table_frame)
    midtown_frame.pack(fill=X, pady=5)
    Label(midtown_frame, text="Midtown Zone (Blue): ", font=("Arial", 14, "bold"), anchor="w").pack(side=LEFT)
    Label(midtown_frame, text=", ".join(sorted(MIDTOWN)), font=("Arial", 14), anchor="w").pack(side=LEFT, padx=5)

    # Downtown zone station list
    downtown_frame = Frame(table_frame)
    downtown_frame.pack(fill=X, pady=5)
    Label(downtown_frame, text="Downtown Zone (Yellow): ", font=("Arial", 14, "bold"), anchor="w").pack(side=LEFT)
    Label(downtown_frame, text=", ".join(sorted(DOWNTOWN)), font=("Arial", 14), anchor="w").pack(side=LEFT, padx=5)

    Button(window, text="Next", font=("Arial", 24), command=screen_2).pack(side=BOTTOM, pady=5)

def screen_2():
    reset_window()

    # Reset the StringVar to ensure no button is selected by default
    start_zone.set("None")

    Label(window, text="What zone are you in (start zone)?", font=("Arial", 18, "bold")).pack(pady=5)

    # Map display
    map_image = PhotoImage(file=map_image_path) 
    map_label = Label(window, image=map_image)
    map_label.pack(pady=0)
    window.map_image = map_image  # Prevent garbage collection

    # Zone buttons frame - frames allow multiple buttons to appear on the same line
    button_frame = Frame(window)
    button_frame.pack(fill=NONE, pady=10)

    # Zone buttons
    # These button presses are stored in variables
    Radiobutton(button_frame, text="Central Zone", variable=start_zone, value="Central", indicatoron=False, font=("Arial", 20)).pack(side=LEFT, padx=15)
    Radiobutton(button_frame, text="Midtown Zone", variable=start_zone, value="Midtown", indicatoron=False, font=("Arial", 20)).pack(side=LEFT, padx=15)
    Radiobutton(button_frame, text="Downtown Zone", variable=start_zone, value="Downtown", indicatoron=False, font=("Arial", 20)).pack(side=LEFT, padx=15)

    # Back/next buttons frame
    nav_button_frame = Frame(window)
    nav_button_frame.pack(fill=NONE, pady=10)

    # Back/next buttons
    Button(nav_button_frame, text="Back", font=("Arial", 20), command=screen_1).pack(side=LEFT, padx=30)
    Button(nav_button_frame, text="Next", font=("Arial", 20), command=lambda: validate_selection(start_zone, screen_3)).pack(side=LEFT, padx=30)

def validate_selection(zone, next_screen):
    if zone.get() in ("None"):  # Check if no valid button is selected
        show_error("Please select a zone before proceeding.")
    else:   # If all is good, go to next screen
        next_screen()


def screen_3():
    reset_window()

    # Reset the StringVar to ensure no button is selected by default
    destination_zone.set("None")

    Label(window, text="Where are you going (destination zone)?", font=("Arial", 18, "bold")).pack(pady=5)

    # Map display
    map_image = PhotoImage(file=map_image_path) 
    map_label = Label(window, image=map_image)
    map_label.pack(pady=0)
    window.map_image = map_image  # Prevent garbage collection

    # Zone buttons frame
    button_frame = Frame(window)
    button_frame.pack(fill=NONE, pady=10)

    # Zone buttons
    # These button presses are stored in variables
    Radiobutton(button_frame, text="Central Zone", variable=destination_zone, value="Central", indicatoron=False, font=("Arial", 20)).pack(side=LEFT, padx=15)
    Radiobutton(button_frame, text="Midtown Zone", variable=destination_zone, value="Midtown", indicatoron=False, font=("Arial", 20)).pack(side=LEFT, padx=15)
    Radiobutton(button_frame, text="Downtown Zone", variable=destination_zone, value="Downtown", indicatoron=False, font=("Arial", 20)).pack(side=LEFT, padx=15)

    # Back/next buttons frame
    nav_button_frame = Frame(window)
    nav_button_frame.pack(fill=NONE, pady=10)

    # Back/Next buttons
    Button(nav_button_frame, text="Back", font=("Arial", 20), command=screen_2).pack(side=LEFT, padx=30)
    Button(nav_button_frame, text="Next", font=("Arial", 20), command=lambda: validate_selection(destination_zone, screen_4)).pack(side=LEFT, padx=30)

def screen_4():
    reset_window()

    # Global variable for selected tickets
    global selected_tickets

    # Dictionary is created to allow storage of all 4 ticket types
    selected_tickets = {
        "adult": {"quantity": StringVar(value="None"), "fare": 21.05},
        "child": {"quantity": StringVar(value="None"), "fare": 14.10},
        "senior": {"quantity": StringVar(value="None"), "fare": 10.25},
        "student": {"quantity": StringVar(value="None"), "fare": 17.50},
    }

    Label(window, text="How many of each tickets would you like?", font=("Arial", 18, "bold")).pack(pady=10)

    # Ticket selection frame
    ticket_frame = Frame(window)
    ticket_frame.pack(pady=30)

    # Function for creating ticket type rows. Each row has a Label, an "None" button, and a "1""2""3""4""5" button
    def create_ticket_row(ticket_type, details):
        frame = Frame(ticket_frame)
        frame.pack(fill=X, pady=5)

        # Ticket type label
        Label(frame, text=ticket_type.capitalize(), font=("Arial", 18, "bold"), width=10, anchor="w").pack(side=LEFT, padx=10)

        # "None" button
        Radiobutton(frame, text="None", variable=details["quantity"], value="None",
                    indicatoron=False, font=("Arial", 18), width=6).pack(side=LEFT, padx=5, pady=5)

        # Quantity buttons
        for i in range(1, 6):
            Radiobutton(frame, text=str(i), variable=details["quantity"], value=str(i),
                indicatoron=False, font=("Arial", 18), width=5).pack(side=LEFT, padx=5, pady=5)

    # A row is created for every entry in the dictionary - "adult""child""senior""student"
    for ticket_type, details in selected_tickets.items():
        create_ticket_row(ticket_type, details)

    # Back/Next buttons frame
    nav_button_frame = Frame(window)
    nav_button_frame.pack(pady=0)

    # Back/Next buttons
    Button(nav_button_frame, text="Back", font=("Arial", 20), command=screen_3).pack(side=LEFT, padx=30)
    Button(nav_button_frame, text="Next", font=("Arial", 20), command=lambda: validate_ticket_selection(screen_5)).pack(side=LEFT, padx=30)

def validate_ticket_selection(next_screen):
    # Check if no tickets are selected
    if all(details["quantity"].get() == "None" for details in selected_tickets.values()):
        show_error("Please select at least one ticket.")
    else:   # If all is good, go to next screen
        print("Selected Tickets:", {k: details["quantity"].get() for k, details in selected_tickets.items()})   # For debugging purposes to see if button 
                                                                                                                # presses are saved properly
        next_screen()

def screen_5():
    reset_window()

    # Get the current time and date
    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Collect ticket selections using dictionary comprehension. A new dictionary is created only including selected tickets
    selected_tickets_summary = {
        k.capitalize(): v["quantity"].get()
        for k, v in selected_tickets.items()
        if v["quantity"].get() != "None"
    }

    # Calculate total travellers 
    total_travelers = sum(int(v) for v in selected_tickets_summary.values() if v.isdigit())

    # Calculate total price using function
    total_price = calculate_total_fare(start_zone, destination_zone, selected_tickets_summary, selected_tickets)

    if total_price is None:
        return  # Stop execution if there was an error in zone selection

    # Create a TravelTicket object
    ticket = TravelTicket(start_zone.get(), destination_zone.get(), selected_tickets_summary, total_price)

    Label(window, text="Your Travel Ticket", font=("Arial", 22, "bold")).pack(pady=50)

    # Information frame
    info_frame = Frame(window)
    info_frame.pack(pady=10)

    Label(info_frame, text=f"Ticket ID: {ticket.ticket_id}", font=("Arial", 16, "bold")).pack(anchor="w", pady=5)
    Label(info_frame, text=f"Time and Date: {ticket.timestamp}", font=("Arial", 16)).pack(anchor="w", pady=5)
    Label(info_frame, text=f"From: {ticket.start_zone}", font=("Arial", 16)).pack(anchor="w", pady=5)
    Label(info_frame, text=f"To: {ticket.destination_zone}", font=("Arial", 16)).pack(anchor="w", pady=5)

    # Uses the new dicitonary to display how many of each ticket were selected
    for ticket_type, quantity in ticket.selected_tickets_summary.items():
        Label(info_frame, text=f"  {ticket_type}: {quantity}", font=("Arial", 16)).pack(anchor="w", pady=5)

    Label(info_frame, text=f"Total number of travelers: {total_travelers}", font=("Arial", 16)).pack(anchor="w", pady=5)
    Label(info_frame, text=f"Total price: ${ticket.total_price:.2f}", font=("Arial", 22, "bold")).pack(anchor="w", pady=20)

    # Store ticket object for later use (e.g., printing)
    window.ticket_object = ticket 

    # Navigation buttons
    nav_button_frame = Frame(window)
    nav_button_frame.pack(pady=20)

    Button(nav_button_frame, text="Back", font=("Arial", 20), command=screen_4).pack(side=LEFT, padx=30)
    Button(nav_button_frame, text="Next", font=("Arial", 20), command=lambda: screen_6(total_price)).pack(side=LEFT, padx=30)

def screen_6(total_price):
    reset_window()

    # Total price and payment option
    Label(window, text=f"Total: ${total_price:.2f}", font=("Arial", 22, "bold")).pack(pady=20)
    Label(window, text="How would you like to pay?", font=("Arial", 22, "bold")).pack(pady=50)

    # Navigation buttons - Cash/Card
    nav_button_frame = Frame(window)
    nav_button_frame.pack(pady=20)

    Button(nav_button_frame, text="Cash", font=("Arial", 20), command=lambda: cash(total_price)).pack(side=LEFT, padx=30)
    Button(nav_button_frame, text="Card", font=("Arial", 20), command=lambda: card(total_price)).pack(side=LEFT, padx=30)

def calculate_total_fare(start_zone, destination_zone, selected_tickets_summary, selected_tickets):
    """Calculate the total fare based on the number of zones and ticket quantities."""
    
    print(start_zone.get())    # For debugging
    print(destination_zone.get())    # For debugging

    # Determine the number of zones traveled
    if (start_zone.get() == "Central" and destination_zone.get() == "Central"):
        num_zones = 1
    elif (start_zone.get() == "Midtown" and destination_zone.get() == "Midtown"):
        num_zones = 2
    elif (start_zone.get() == "Downtown" and destination_zone.get() == "Downtown"):
        num_zones = 3
    elif (start_zone.get() == "Central" and destination_zone.get() == "Midtown") or \
        (start_zone.get() == "Midtown" and destination_zone.get() == "Central"):
        num_zones = 2
    elif (start_zone.get() == "Central" and destination_zone.get() == "Downtown") or \
        (start_zone.get() == "Downtown" and destination_zone.get() == "Central"):
        num_zones = 3
    elif (start_zone.get() == "Midtown" and destination_zone.get() == "Downtown") or \
        (start_zone.get() == "Downtown" and destination_zone.get() == "Midtown"):
        num_zones = 2
    else:
        # Fallback in case no valid zones are set
        show_error("Invalid zones selected. Please go back and select valid zones.")
        return None  # Return None to indicate an error

    # Calculate the total fare based on selected tickets
    adult_price = float(selected_tickets_summary.get("Adult", 0)) * selected_tickets["adult"]["fare"] * num_zones
    child_price = float(selected_tickets_summary.get("Child", 0)) * selected_tickets["child"]["fare"] * num_zones
    senior_price = float(selected_tickets_summary.get("Senior", 0)) * selected_tickets["senior"]["fare"] * num_zones
    student_price = float(selected_tickets_summary.get("Student", 0)) * selected_tickets["student"]["fare"] * num_zones

    total_price = adult_price + child_price + senior_price + student_price

    return total_price  # Return the computed total price


# The functions below are just there to simulate a payment gateway


def cash(price):
    reset_window()

    # Display the total price
    total_label = Label(window, text=f"Total: £{price:.2f}", font=("Arial", 40))
    total_label.pack(pady=70)

    # Button to insert cash
    insert_button = Button(window, text="Insert Cash",
                        font=("Arial", 30),
                        command=insert_cash)
    insert_button.pack(pady=30)


def insert_cash():
    reset_window()

    printing_label = Label(window, text="Printing tickets...", font=("Arial", 36))
    printing_label.pack(pady=190)

    window.after(2000, show_thank_you)  # Wait for 2 seconds before showing the thank you message

def card(price):
    reset_window()

    # Display the total price
    total_label = Label(window, text=f"Total: £{price:.2f}", font=("Arial", 40))
    total_label.pack(pady=70)

    # Button to insert card
    insert_button = Button(window, text="Insert Card",
                        font=("Arial", 30),
                        command=insert_card)
    insert_button.pack(pady=30)


def insert_card():
    reset_window()

    verifying_label = Label(window, text="Verifying payment...", font=("Arial", 36))
    verifying_label.pack(pady=190)

    window.after(2000, show_payment_accepted)  # Wait for 2 seconds before showing payment accepted


def show_payment_accepted():
    reset_window()

    payment_label = Label(window, text="Payment accepted. Printing tickets...",
                        wraplength=650,
                        font=("Arial", 36))
    payment_label.pack(pady=190)

    window.after(3000, show_thank_you)  # Wait for 3 seconds before showing the thank you message

def show_thank_you():
    reset_window()

    # Show thank you message
    thank_you_label = Label(window, text="Thank you. Would you like to buy more tickets?",  wraplength= 600, font=("Arial", 36))
    thank_you_label.pack(pady=190)

    # Navigation buttons
    nav_button_frame = Frame(window)
    nav_button_frame.pack(pady=20)

    Button(nav_button_frame, text="Yes", font=("Arial", 20), command= screen_1).pack(side=LEFT, padx=30)
    Button(nav_button_frame, text="No", font=("Arial", 20), command= have_nice_day).pack(side=LEFT, padx=30)

def have_nice_day():
    reset_window()

    # Show thank you message
    thank_you_label = Label(window, text="Thank you. Have a nice day", font=("Arial", 36))
    thank_you_label.pack(pady=190)

    window.after(3000, window.destroy)  # Close the app after 3 seconds

# Initialize the app
screen_1()
window.mainloop()