from tkinter import *
from tkinter import messagebox
import os
import datetime  

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

map_image_path = os.path.join(os.path.dirname(__file__), "underground-map.PNG")  # Path to the map image

# Initialize main window
window = Tk()
window.title("Centrala Underground Ticket App")
window.geometry("1050x820")

start_zone = StringVar(value="None")  # Default to no selection
destination_zone = StringVar(value="None")  # Default to no selection

def reset_window():
    for widget in window.winfo_children():
        widget.destroy()

def show_error(message):
    messagebox.showerror("Error", message)

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

    # Central Zone
    central_frame = Frame(table_frame)
    central_frame.pack(fill=X, pady=5)
    Label(central_frame, text="Central Zone (Pink/Grey): ", font=("Arial", 14, "bold"), anchor="w").pack(side=LEFT)
    Label(central_frame, text=", ".join(sorted(CENTRAL)), font=("Arial", 14), anchor="w").pack(side=LEFT, padx=5)

    # Midtown Zone
    midtown_frame = Frame(table_frame)
    midtown_frame.pack(fill=X, pady=5)
    Label(midtown_frame, text="Midtown Zone (Blue): ", font=("Arial", 14, "bold"), anchor="w").pack(side=LEFT)
    Label(midtown_frame, text=", ".join(sorted(MIDTOWN)), font=("Arial", 14), anchor="w").pack(side=LEFT, padx=5)

    # Downtown Zone
    downtown_frame = Frame(table_frame)
    downtown_frame.pack(fill=X, pady=5)
    Label(downtown_frame, text="Downtown Zone (Yellow): ", font=("Arial", 14, "bold"), anchor="w").pack(side=LEFT)
    Label(downtown_frame, text=", ".join(sorted(DOWNTOWN)), font=("Arial", 14), anchor="w").pack(side=LEFT, padx=5)

    Button(window, text="Next", font=("Arial", 24), command=screen_2).pack(side=BOTTOM, pady=5)

def screen_2():
    reset_window()

    # Reset the StringVar to ensure no button is selected
    start_zone.set("None")

    Label(window, text="What zone are you in (start zone)?", font=("Arial", 18, "bold")).pack(pady=5)

    # Map display
    map_image = PhotoImage(file=map_image_path) 
    map_label = Label(window, image=map_image)
    map_label.pack(pady=0)
    window.map_image = map_image  # Prevent garbage collection

    # Zone buttons frame
    button_frame = Frame(window)
    button_frame.pack(fill=NONE, pady=10)

    # Zone buttons
    Radiobutton(button_frame, text="Central Zone", variable=start_zone, value="Central", indicatoron=False, font=("Arial", 20)).pack(side=LEFT, padx=15)
    Radiobutton(button_frame, text="Midtown Zone", variable=start_zone, value="Midtown", indicatoron=False, font=("Arial", 20)).pack(side=LEFT, padx=15)
    Radiobutton(button_frame, text="Downtown Zone", variable=start_zone, value="Downtown", indicatoron=False, font=("Arial", 20)).pack(side=LEFT, padx=15)

    # Back/next buttons frame
    nav_button_frame = Frame(window)
    nav_button_frame.pack(fill=NONE, pady=10)

    # Navigation buttons
    Button(nav_button_frame, text="Back", font=("Arial", 20), command=screen_1).pack(side=LEFT, padx=30)
    Button(nav_button_frame, text="Next", font=("Arial", 20), command=lambda: validate_selection(start_zone, screen_3)).pack(side=LEFT, padx=30)

def validate_selection(zone, next_screen):
    if zone.get() in ("None"):  # Check if no valid button is selected
        show_error("Please select a zone before proceeding.")
    else:
        next_screen()


def screen_3():
    reset_window()

    # Reset the StringVar to ensure no button is selected
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
    Radiobutton(button_frame, text="Central Zone", variable=destination_zone, value="Central", indicatoron=False, font=("Arial", 20)).pack(side=LEFT, padx=15)
    Radiobutton(button_frame, text="Midtown Zone", variable=destination_zone, value="Midtown", indicatoron=False, font=("Arial", 20)).pack(side=LEFT, padx=15)
    Radiobutton(button_frame, text="Downtown Zone", variable=destination_zone, value="Downtown", indicatoron=False, font=("Arial", 20)).pack(side=LEFT, padx=15)

    # Back/next buttons frame
    nav_button_frame = Frame(window)
    nav_button_frame.pack(fill=NONE, pady=10)

    # Navigation buttons
    Button(nav_button_frame, text="Back", font=("Arial", 20), command=screen_2).pack(side=LEFT, padx=30)
    Button(nav_button_frame, text="Next", font=("Arial", 20), command=lambda: validate_selection(destination_zone, screen_4)).pack(side=LEFT, padx=30)

def screen_4():
    reset_window()
    
    # Global variable for selected tickets
    global selected_tickets
    selected_tickets = {"adult": StringVar(value="None"),
                        "child": StringVar(value="None"),
                        "senior": StringVar(value="None"),
                        "student": StringVar(value="None")}

    Label(window, text="How many of each tickets would you like?", font=("Arial", 18, "bold")).pack(pady=40)

    # Ticket selection frame
    ticket_frame = Frame(window)
    ticket_frame.pack(pady=130)

    # Create ticket type rows
    def create_ticket_row(ticket_type):
        frame = Frame(ticket_frame)
        frame.pack(fill=X, pady=5)

        # Ticket type label
        Label(frame, text=ticket_type.capitalize(), font=("Arial", 18, "bold"), width=10, anchor="w").pack(side=LEFT, padx=10)

        # "None" button
        Radiobutton(frame, text="None", variable=selected_tickets[ticket_type], value="None",
                    indicatoron=False, font=("Arial", 18), width=6).pack(side=LEFT, padx=5, pady=5)

        # Quantity buttons
        for i in range(1, 6):
            Radiobutton(frame, text=str(i), variable=selected_tickets[ticket_type], value=str(i),
                        indicatoron=False, font=("Arial", 18), width=5).pack(side=LEFT, padx=5, pady=5)

    # Add rows for each ticket type
    for ticket_type in selected_tickets:
        create_ticket_row(ticket_type)

    # Navigation buttons
    nav_button_frame = Frame(window)
    nav_button_frame.pack(pady=20)

    Button(nav_button_frame, text="Back", font=("Arial", 20), command=screen_3).pack(side=LEFT, padx=30)
    Button(nav_button_frame, text="Next", font=("Arial", 20), command=lambda: validate_ticket_selection(screen_5)).pack(side=LEFT, padx=30)

def validate_ticket_selection(next_screen):
    # Check if at least one ticket is selected
    if all(value.get() == "None" for value in selected_tickets.values()):
        show_error("Please select at least one ticket.")
    else:
        print("Selected Tickets:", {k: v.get() for k, v in selected_tickets.items()})  # Debugging
        next_screen()

def screen_5():
    reset_window()

    # Get the current time and date
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Ticket details for display
    selected_tickets_summary = {k.capitalize(): v.get() for k, v in selected_tickets.items() if v.get() != "None"}

    total_travelers = sum(int(v) for v in selected_tickets_summary.values() if v.isdigit())

    # Calculate total price

    print(start_zone.get())
    print(destination_zone.get())
    # 9 Scenarios for how many zones travelling in
    if (start_zone.get() == "Central" and destination_zone.get() == "Central") or \
        (start_zone.get() == "Midtown" and destination_zone.get() == "Midtown") or \
        (start_zone.get() == "Downtown" and destination_zone.get() == "Downtown"):
            num_zones = 1
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
        return  # Exit the function early

    adult_per_zone = 2105 
    child_per_zone = 1410
    senior_per_zone = 1025
    student_per_zone = 1750

    adult_price = int(selected_tickets_summary.get("Adult", 0)) * adult_per_zone * num_zones
    child_price = int(selected_tickets_summary.get("Child", 0)) * child_per_zone * num_zones
    senior_price = int(selected_tickets_summary.get("Senior", 0)) * senior_per_zone * num_zones
    student_price = int(selected_tickets_summary.get("Student", 0)) * student_per_zone * num_zones

    total_price = adult_price + child_price + senior_price + student_price

    Label(window, text="Your travel voucher", font=("Arial", 18, "bold")).pack(pady=10)

    # Information frame
    info_frame = Frame(window)
    info_frame.pack(pady=10)

    # Add information rows
    Label(info_frame, text=f"Time and Date: {current_time}", font=("Arial", 14)).pack(anchor="w")
    Label(info_frame, text=f"Travelling from: {start_zone.get()}", font=("Arial", 14)).pack(anchor="w")
    Label(info_frame, text=f"Travelling to: {destination_zone}", font=("Arial", 14)).pack(anchor="w")
    Label(info_frame, text="Tickets:", font=("Arial", 14)).pack(anchor="w")
    for ticket_type, quantity in selected_tickets_summary.items():
        Label(info_frame, text=f"  {ticket_type}: {quantity}", font=("Arial", 14)).pack(anchor="w")
    Label(info_frame, text=f"Total number of travelers: {total_travelers}", font=("Arial", 14)).pack(anchor="w")
    Label(info_frame, text=f"Total price: ${total_price:.2f}", font=("Arial", 14, "bold")).pack(anchor="w")

    # Navigation buttons
    nav_button_frame = Frame(window)
    nav_button_frame.pack(pady=20)

    Button(nav_button_frame, text="Back", font=("Arial", 20), command=screen_4).pack(side=LEFT, padx=30)
    Button(nav_button_frame, text="Next", font=("Arial", 20), command=screen_6).pack(side=LEFT, padx=30)

def screen_6():
    reset_window()

# Initialize the app
screen_1()
window.mainloop()