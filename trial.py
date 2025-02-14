# This is a trial app for the Centrala underground system 
# Please open readme-trial file for a detailed app description

import tkinter as tk
from datetime import datetime, time as dt_time
from datetime import timedelta
import os

FONT = "Tahoma"

STATION_ID = "Centrala"

# List of stations and zones
stations = [
    "Erean", "Brunad", "Marend", "Ryall", "Pryn", "Ederif", "Ruril",
    "Holmer", "Vertwall", "Adohad", "Elyot", "Keivia", "Perinad", "Zord",
    "Quthiel", "Riclya", "Agralle", "Docia", "Stonyam", "Obelyn", "Ralith",
    "Garion", "Sylas", "Oloadus", "Riladia", "Wicyt", "Yaen", "Rede", "Bylyn",
    "Frestin", "Soth", "Lomil", "Ninia", "Tallan", "Jaund", "Centrala"
]

alphabetical_stations = sorted(stations)

DOWNTOWN = ["Erean", "Brunad", "Marend", "Ryall", "Pryn", "Ederif", "Ruril",
            "Holmer", "Vertwall", "Adohad", "Elyot", "Keivia", "Perinad", "Zord"]

MIDTOWN = ["Quthiel", "Riclya", "Agralle", "Docia", "Stonyam", "Obelyn", "Ralith",
        "Garion", "Sylas", "Oloadus", "Riladia", "Wicyt"]

CENTRAL = ["Yaen", "Rede", "Bylyn", "Frestin", "Soth", "Lomil", "Ninia",
        "Tallan", "Jaund", "Centrala"]

# create the variables
def create_trial_vars():
    global trial_selected_station, trial_selected_time, trial_is_return
    global trial_adult_tickets, trial_child_tickets, trial_senior_tickets, trial_student_tickets 
    global trial_departing_from_here, trial_departing_today, trial_departure_station, trial_departure_date
    global map_image_path

    trial_selected_station = tk.StringVar(master=trial_window)
    trial_selected_time = tk.StringVar(master=trial_window)
    trial_is_return = tk.StringVar(master=trial_window, value="No")
    trial_adult_tickets = tk.IntVar(master=trial_window, value=0)
    trial_child_tickets = tk.IntVar(master=trial_window, value=0)
    trial_senior_tickets = tk.IntVar(master=trial_window, value=0)
    trial_student_tickets = tk.IntVar(master=trial_window, value=0)
    trial_departing_from_here = tk.StringVar(master=trial_window, value="Yes")
    trial_departing_today = tk.StringVar(master=trial_window, value="Yes")
    trial_departure_station = tk.StringVar(master=trial_window, value="Centrala")
    trial_departure_date = tk.StringVar(master=trial_window, value=datetime.now().strftime("%Y-%m-%d"))
    map_image_path = os.path.join(os.path.dirname(__file__), "smaller-map.PNG")  # Path to the map image

# help_screen function
def help_screen():
    global trial_window  # Make the window global
    trial_window = tk.Toplevel()
    trial_window.title("Trial Ticketing System")
    trial_window.geometry("1000x600")

    # Call create_trial_vars() here, AFTER creating trial_window
    create_trial_vars()
    trial_reset_window()

    helpline_frame = tk.Frame(trial_window)
    helpline_frame.pack(padx=20, pady=50)
    tk.Label(
        helpline_frame,
        text="Helpline number is 12345678",
        wraplength=300,
        font=("Arial", 25)
    ).pack()

    easy_mode_frame = tk.Frame(trial_window)
    easy_mode_frame.pack(padx=20)
    tk.Label(
        easy_mode_frame,
        text="Would you like to try our trial version?",
        wraplength=400,
        font=("Arial", 25)
    ).pack(pady=20)
    tk.Button(easy_mode_frame, text="Yes", command=trial_mode, font=("Arial", 22)).pack()

    def back_to_main():
        trial_close_window()  # Closes the trial screen

    tk.Button(
        trial_window,
        text="Back to previous screen",
        command=back_to_main, 
        font=("Arial", 20)
    ).pack(side=tk.BOTTOM, pady=40)

def trial_mode():
    trial_reset_window() # Clears the previous screen

    # ✅ Reset all selection values to defaults
    trial_selected_station.set("")
    trial_selected_time.set("")
    trial_is_return.set("No")
    trial_adult_tickets.set(0)
    trial_child_tickets.set(0)
    trial_senior_tickets.set(0)
    trial_student_tickets.set(0)
    trial_departing_from_here.set("Yes")
    trial_departing_today.set("Yes")
    trial_departure_station.set("Centrala")
    trial_departure_date.set(datetime.now().strftime("%d-%m-%Y"))

    back_to_main = tk.Button(trial_window, text="Back to Main App",
                    font=(FONT, 13),
                    command=trial_close_window)
    back_to_main.place(x=50, y=10)  # Adjust placement to top-left corner
    # Layout
    # Welcome Label
    tk.Label(trial_window, text=f"Welcome to {STATION_ID} Station", font=("Arial", 18, "bold")).pack(pady=10)

    tk.Button(trial_window, text="Reset Buttons", font=(FONT, 13), command=trial_mode).place(x=850, y=10)  # Adjust placement to top-right corner

    tk.Button(trial_window, text="Show Map", font=(FONT, 13), command=map_screen).place(x=750, y=10)  

    # Top Grid Containers
    frame_top = tk.Frame(trial_window)
    frame_top.pack(pady=0)

    # Left Grid for Stations
    frame_left = tk.Frame(frame_top)
    frame_left.pack(side=tk.LEFT, padx=10)
    tk.Label(frame_left, text="Choose Destination", font=("Arial", 12, "bold")).pack(pady=5)

    station_grid = tk.Frame(frame_left)
    station_grid.pack()

    for i, station in enumerate(alphabetical_stations):
        btn = tk.Radiobutton(
            station_grid, text=station, variable=trial_selected_station, value=station,
            indicatoron=False, width=8, relief="raised", font=(FONT, 12)
        )
        btn.grid(row=i // 6, column=i % 6, padx=5, pady=5)

    # Right Grid for Times
    frame_right = tk.Frame(frame_top)
    frame_right.pack(side=tk.LEFT, padx=10)
    current_time = datetime.now().strftime("%H:%M")
    #tk.Label(frame_right, text=f"Departure Time (current time {current_time})", font=("Arial", 12)).pack(pady=5)
    tk.Label(frame_right, text=f"Departure Time\n(current time {current_time})", font=("Arial", 12, "bold"), wraplength=200).pack(pady=5)

    # Time Grid
    time_grid = tk.Frame(frame_right)
    time_grid.pack()

    for i, time in enumerate(get_time_slots()):
        btn = tk.Radiobutton(
            time_grid, text=time, variable=trial_selected_time, value=time,
            indicatoron=False, width=5, relief="raised", font=(FONT, 11)
        )
        btn.grid(row=i // 6, column=i % 6, padx=5, pady=5, sticky="n")

    # Create a middle container for Return, Departing, and Ticket Selection
    frame_middle = tk.Frame(trial_window)
    frame_middle.pack(fill=tk.BOTH, padx=10, pady=10)

    # Create a left frame for Return & Departing selections
    frame_left = tk.Frame(frame_middle)
    frame_left.grid(row=0, column=0, padx=70, pady=5)

    # Create a right frame for Ticket Selection
    frame_right = tk.Frame(frame_middle)
    frame_right.grid(row=0, column=1, padx=70, pady=5)

    # ==============================
    # Left Side - Return & Departing Selections
    # ==============================

    # Return Selection
    tk.Label(frame_left, text="Return?", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    tk.Radiobutton(frame_left, text="Yes", font=(FONT, 12), variable=trial_is_return, value="Yes").grid(row=0, column=1, padx=5, pady=5)
    tk.Radiobutton(frame_left, text="No", font=(FONT, 12), variable=trial_is_return, value="No").grid(row=0, column=2, padx=5, pady=5)

    # Departing From This Station
    tk.Label(frame_left, text="Departing from this station?", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=5, pady=5)
    tk.Radiobutton(frame_left, text="Yes", font=(FONT, 12), variable=trial_departing_from_here, value="Yes").grid(row=1, column=1, padx=5, pady=5)
    tk.Radiobutton(frame_left, text="No", font=(FONT, 12), variable=trial_departing_from_here, value="No").grid(row=1, column=2, padx=5, pady=5)

    # Departing Today?
    tk.Label(frame_left, text="Departing Today?", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=5, pady=5)
    tk.Radiobutton(frame_left, text="Yes", font=(FONT, 12), variable=trial_departing_today, value="Yes").grid(row=2, column=1, padx=5, pady=5)
    tk.Radiobutton(frame_left, text="No", font=(FONT, 12), variable=trial_departing_today, value="No").grid(row=2, column=2, padx=5, pady=5)

    # ==============================
    # Right Side - Ticket Selection
    # ==============================

    # List of ticket types and corresponding variables
    ticket_types = [
        ("No of Adult Tickets", trial_adult_tickets),
        ("No of Child Tickets", trial_child_tickets),
        ("No of Senior Tickets", trial_senior_tickets),
        ("No of Student Tickets", trial_student_tickets)
    ]

    # Loop through each ticket type and create labels + radio buttons
    for row, (label_text, variable) in enumerate(ticket_types):
        tk.Label(frame_right, text=label_text, font=("Arial", 12, "bold")).grid(row=row, column=0, padx=5, pady=5, sticky="w")

        for i in range(1, 6):  # Create radio buttons from 1 to 5
            btn = tk.Radiobutton(
                frame_right, text=str(i), font=(FONT, 12), variable=variable, value=i,
                indicatoron=False, relief="raised", width=3
            )
            btn.grid(row=row, column=i, padx=2, pady=2)

    # Enter Button
    tk.Button(trial_window, text="Enter", command=validate_and_proceed, font=("Arial", 16)).pack(pady=0)

def map_screen():
    trial_reset_window()

        # Map display
    map_image = tk.PhotoImage(file=map_image_path) 
    trial_window.map_image = map_image  # Prevent garbage collection
    map_label = tk.Label(trial_window, image=map_image)
    map_label.pack(pady=70)

    tk.Button(trial_window, text="Go Back", font=(FONT, 13), command=trial_mode).place(x=50, y=10)

def calculate_price(departure_station, selected_station, is_return, adult_tickets, child_tickets, 
                    senior_tickets, student_tickets):

    print(f"Starting Point: {departure_station}, Destination: {selected_station}")
    print(f"Is Return: {is_return}\n"
        f"Number of adult Tickets: {adult_tickets}\n"
        f"Number of child Tickets: {child_tickets}\n"
        f"Number of senior Tickets: {senior_tickets}\n"
        f"Number of student Tickets: {student_tickets}")


    number_of_zones = 0
    # Look for all downtown to downtown, through 1 zone
    if departure_station in ["Erean", "Brunad"] and selected_station in ["Erean", "Brunad"]:
        number_of_zones += 1
        print("1") # Print numbers are for debugging
    elif departure_station in ["Ryall", "Pryn"] and selected_station in ["Ryall", "Pryn"]:
        number_of_zones += 1
        print("2")
    elif departure_station in ["Holmer", "Vertwall", "Ruril"] and selected_station in ["Holmer", "Vertwall", "Ruril"]:
        number_of_zones += 1
        print("3")
    elif departure_station in ["Elyot", "Adohad"] and selected_station in ["Elyot", "Adohad"]:
        number_of_zones += 1
        print("4")

    # Look for all downtown to downtown, through 3 zones
    elif departure_station == "Marend" and selected_station in ["Ryall", "Pryn"]:
        number_of_zones += 3
        print("5")
    elif departure_station in ["Ryall", "Pryn"] and selected_station == "Marend":
        number_of_zones += 3
        print("6")

    # Look for all downtown to midtown, through 2 zones
    elif departure_station in ["Erean", "Brunad"] and selected_station == "Riclya":
        number_of_zones += 2
        print("7")
    elif departure_station in ["Marend", "Ryall", "Pryn"] and selected_station in ["Agralle", "Docia", "Stonyam"]:
        number_of_zones += 2
        print("8")
    elif departure_station == "Ederif" and selected_station == "Obelyn":
        number_of_zones += 2
        print("9")
    elif departure_station in ["Holmer", "Vertwall", "Ruril"] and selected_station in ["Garion", "Ralith"]:
        number_of_zones += 2
        print("10")
    elif departure_station in ["Elyot", "Adohad"] and selected_station == "Sylas":
        number_of_zones += 2
        print("11")
    elif departure_station == "Keivia" and selected_station == "Oloadus":
        number_of_zones += 2
        print("12")
    elif departure_station == "Perinad" and selected_station == "Riladia":
        number_of_zones += 2
        print("13")
    elif departure_station == "Zord" and selected_station == "Quthiel":
        number_of_zones += 2
        print("14")

    # Look for all midtown to downtown, through 2 zones
    elif departure_station == "Riclya" and selected_station in ["Erean", "Brunad"]:
        number_of_zones += 2
        print("15")
    elif departure_station in ["Agralle", "Docia", "Stonyam"] and selected_station in ["Marend", "Ryall", "Pryn"]:
        number_of_zones += 2
        print("16")
    elif departure_station == "Obelyn" and selected_station == "Ederif":
        number_of_zones += 2
        print("17")
    elif departure_station in ["Garion", "Ralith"] and selected_station in ["Holmer", "Vertwall", "Ruril"]:
        number_of_zones += 2
        print("18")
    elif departure_station == "Sylas" and selected_station in ["Elyot", "Adohad"]:
        number_of_zones += 2
        print("19")
    elif departure_station == "Oloadus" and selected_station == "Keivia":
        number_of_zones += 2
        print("20")
    elif departure_station == "Riladia" and selected_station == "Perinad":
        number_of_zones += 2
        print("21")
    elif departure_station == "Quthiel" and selected_station == "Zord":
        number_of_zones += 2
        print("22")

    # Look for all midtown to midtown, through 1 zone
    elif departure_station in ["Agralle", "Docia", "Stonyam"] and selected_station in ["Agralle", "Docia", "Stonyam"]:
        number_of_zones += 1
        print("23")
    elif departure_station in ["Garion", "Ralith"] and selected_station in ["Garion", "Ralith"]:
        number_of_zones += 1
        print("24")

    # Look for all other scenarios
    elif departure_station in DOWNTOWN and selected_station in DOWNTOWN:
        number_of_zones += 5
        print("25")
    elif departure_station in DOWNTOWN and selected_station in MIDTOWN:
        number_of_zones += 4
        print("26")
    elif departure_station in MIDTOWN and selected_station in DOWNTOWN:
        number_of_zones += 4
        print("27")
    elif departure_station in MIDTOWN and selected_station in MIDTOWN:
        number_of_zones += 3
        print("28")
    elif departure_station in DOWNTOWN and selected_station in CENTRAL:
        number_of_zones += 3
        print("29")
    elif departure_station in MIDTOWN and selected_station in CENTRAL:
        number_of_zones += 2
        print("30")
    elif departure_station in CENTRAL and selected_station in DOWNTOWN:
        number_of_zones += 3
        print("31")
    elif departure_station in CENTRAL and selected_station in MIDTOWN:
        number_of_zones += 2
        print("32")
    elif departure_station in CENTRAL and selected_station in CENTRAL:
        number_of_zones += 1
        print("33")

    # Calculate the total fare based on selected tickets
    adult_price = float(trial_adult_tickets.get()) * 10.55 * number_of_zones
    child_price = float(trial_child_tickets.get()) * 7.05 * number_of_zones
    senior_price = float(trial_senior_tickets.get()) * 5.15 * number_of_zones
    student_price = float(trial_student_tickets.get()) * 8.75 * number_of_zones

    total_price = adult_price + child_price + senior_price + student_price

    # add return price if applicable
    if is_return == "Yes":
        total_price *= 2

    total_price = "{:.2f}".format(total_price)   # always show price to 2d.p eg. "£17.00"
    return total_price

# Helper function to calculate time slots based on the current time
def get_time_slots():
    now = datetime.now()
#    start_time = now.replace(minute=(now.minute // 30) * 30, second=0, microsecond=0)
    start_time = datetime.combine(datetime.now().date(), dt_time(7, 0))
    times = []
    while start_time <= now.replace(hour=23, minute=30):
        times.append(start_time.strftime("%H:%M"))
        start_time += timedelta(minutes=30)
    return times

# Functions for button click actions
def validate_and_proceed():
    print(trial_selected_station.get())
    print(trial_selected_time.get())

    if (
    not trial_selected_station.get()  # Ensure a destination is selected
    or not trial_selected_time.get()  # Ensure a departure time is selected
    or (  # Ensure at least one ticket type is selected
        trial_adult_tickets.get() == 0
        and trial_child_tickets.get() == 0
        and trial_senior_tickets.get() == 0
        and trial_student_tickets.get() == 0
    )
    ):

        display_error("Please make sure all selections are made.")
    elif trial_departing_from_here.get() == "No" and trial_departing_today.get() == "No":
        choose_dep_station_and_time()
    elif trial_departing_from_here.get() == "No":
        choose_dep_station()
    elif trial_departing_today.get() == "No":
        choose_dep_time()
    else:
        confirm_screen()

def display_error(message):
    error_popup = tk.Toplevel(trial_window)
    error_popup.title("Error")
    error_popup.geometry("400x100")

    # Center the error popup
    x = trial_window.winfo_x() + (trial_window.winfo_width() // 2) - 150
    y = trial_window.winfo_y() + (trial_window.winfo_height() // 2) - 50
    error_popup.geometry(f"400x100+{x}+{y}")

    tk.Label(error_popup, text=message, font=(22), fg="red").pack(pady=10)
    tk.Button(error_popup, text="OK", font=(22), command=error_popup.destroy).pack()

def choose_dep_station():
    trial_reset_window()

    tk.Button(trial_window, text="Start Again", font=(FONT, 13), command=trial_mode).place(x=50, y=10)

    # Reset departure_station to ensure no pre-selection
    trial_departure_station.set("")

    tk.Label(trial_window, text="Choose Departure Station", font=("Arial", 16, "bold")).pack(pady=10)

    station_grid = tk.Frame(trial_window)
    station_grid.pack(pady=50)

    for i, station in enumerate(alphabetical_stations):
        btn = tk.Radiobutton(
            station_grid, text=station, variable=trial_departure_station, value=station,
            indicatoron=False, width=12, height=2, relief="raised", font=(FONT, 12)
        )
        btn.grid(row=i // 6, column=i % 6, padx=5, pady=5)

    def confirm_selection():
        if not trial_departure_station.get():
            display_error("Please select a station.")
        else:
            confirm_screen()

    tk.Button(trial_window, text="Confirm", command=confirm_selection, font=("Arial", 16)).pack(pady=10)



def choose_dep_time():
    trial_reset_window()

    tk.Button(trial_window, text="Start Again", font=(FONT, 13), command=trial_mode).place(x=50, y=10)

    # Reset departure_date and selected_time to ensure no pre-selection
    trial_departure_date.set("")
    trial_selected_time.set("")

    tk.Label(trial_window, text="Choose Departure Date and Time", font=("Arial", 16, "bold")).pack(pady=10)

    # Date grid
    date_grid = tk.Frame(trial_window)
    date_grid.pack(pady=10)

    for i in range(28):
        date = (datetime.now() + timedelta(days=i)).strftime("%d-%m-%Y")  # Format as DD-MM-YYYY
        btn = tk.Radiobutton(
            date_grid, text=date, variable=trial_departure_date, value=date,
            indicatoron=False, width=10, relief="raised", font=(FONT, 12)
        )
        btn.grid(row=i // 7, column=i % 7, padx=5, pady=5)

    # Time grid
    time_grid = tk.Frame(trial_window)
    time_grid.pack(pady=10)

    times = [f"{hour:02}:{minute:02}" for hour in range(7, 24) for minute in range(0, 60, 30)]
    for i, time in enumerate(times):
        btn = tk.Radiobutton(
            time_grid, text=time, variable=trial_selected_time, value=time,
            indicatoron=False, width=5, relief="raised", font=(FONT, 12)
        )
        btn.grid(row=i // 6, column=i % 6, padx=5, pady=5)

    def confirm_selection():
        if not trial_departure_date.get() or not trial_selected_time.get():
            display_error("Please select a date and time.")
        else:
            confirm_screen()

    tk.Button(trial_window, text="Confirm", command=confirm_selection, font=("Arial", 14)).pack(pady=15)

def choose_dep_station_and_time():
    trial_reset_window()

    tk.Button(trial_window, text="Start Again", font=(FONT, 13), command=trial_mode).place(x=50, y=10)

    # Reset variables to ensure fresh selection
    trial_departure_station.set("")  # Reset the station
    trial_departure_date.set("")     # Reset the date
    trial_selected_time.set("")      # Reset the time

    # Title Label
    tk.Label(trial_window, text="Choose a Departure Station and Date/Time", font=("Arial", 16, "bold")).pack()

    # Create main container
    container = tk.Frame(trial_window)
    container.pack(fill=tk.BOTH, expand=True, padx=10, pady=20)

    # Station Grid (middle left)
    station_frame = tk.Frame(container, width=400, height=300)
    station_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

    tk.Label(station_frame, text="Stations", font=("Arial", 12)).pack(pady=3)
    station_grid = tk.Frame(station_frame)
    station_grid.pack(fill=tk.BOTH, expand=True)

    for i, station in enumerate(alphabetical_stations):
        btn = tk.Radiobutton(
            station_grid, text=station, variable=trial_departure_station, value=station,
            indicatoron=False, width=8, relief="raised", font=(FONT, 12)
        )
        btn.grid(row=i // 6, column=i % 6, padx=5, pady=5)

    # Time Grid (middle right)
    time_frame = tk.Frame(container, width=400, height=300)
    time_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)

    tk.Label(time_frame, text="Times", font=("Arial", 12)).pack(pady=3)
    time_grid = tk.Frame(time_frame)
    time_grid.pack(fill=tk.BOTH, expand=True)

    times = [f"{hour:02}:{minute:02}" for hour in range(7, 24) for minute in range(0, 60, 30)]
    for i, time in enumerate(times):
        btn = tk.Radiobutton(
            time_grid, text=time, variable=trial_selected_time, value=time,
            indicatoron=False, width=5, relief="raised", font=(FONT, 12)
        )
        btn.grid(row=i // 6, column=i % 6, padx=5, pady=5)

    # Date Grid (bottom)
    date_frame = tk.Frame(trial_window)
    date_frame.pack(fill=tk.BOTH, expand=True, padx=35)

    tk.Label(date_frame, text="Dates", font=("Arial", 12)).pack()
    date_grid = tk.Frame(date_frame)
    date_grid.pack(fill=tk.BOTH, expand=True)

    for i in range(28):
        date = (datetime.now() + timedelta(days=i)).strftime("%d-%m-%Y")  # Format as DD-MM-YYYY
        btn = tk.Radiobutton(
            date_grid, text=date, variable=trial_departure_date, value=date,
            indicatoron=False, width=12, relief="raised", font=(FONT, 12)
        )
        btn.grid(row=i // 7, column=i % 7, padx=5, pady=5)

    # Confirm Button (bottom)
    def confirm_selection():
        if not trial_departure_station.get() or not trial_departure_date.get() or not trial_selected_time.get():
            display_error("Please select all options.")
        else:
            confirm_screen()

    tk.Button(trial_window, text="Confirm", command=confirm_selection, font=("Arial", 14)).pack(pady=15)

# confirm_screen function
def confirm_screen():
    trial_reset_window()

    tk.Button(trial_window, text="Start Again", font=(FONT, 13), command=trial_mode).place(x=50, y=10)

    price = float(calculate_price(
        trial_departure_station.get(), trial_selected_station.get(),
        trial_is_return.get(), trial_adult_tickets.get(), trial_child_tickets.get(),
        trial_senior_tickets.get(), trial_student_tickets.get()
    ))

    formatted_date = trial_departure_date.get()

    # Fonts for text
    regular_font = ("Arial", 14)
    bold_font = ("Arial", 14, "bold")
    total_font = ("Arial", 22, "bold")  # Slightly larger font for total

    # Line 1
    tk.Label(trial_window, text="Your ticket is", font=regular_font).pack(pady=20)

    # Line 2
    tk.Label(
        trial_window,
        text=f"{trial_departure_station.get()} to {trial_selected_station.get()}",
        font=bold_font
    ).pack(pady=10)

    # Line 3
    tk.Label(
        trial_window,
        text=f"{formatted_date} at {trial_selected_time.get()}",
        font=bold_font
    ).pack(pady=10)

    # Line 4
    tk.Label(
        trial_window,
        text=f"Return: {trial_is_return.get()}",
        font=regular_font
    ).pack(pady=10)

    # Line 5
    total_tickets = (
    trial_adult_tickets.get() + trial_child_tickets.get() +
    trial_senior_tickets.get() + trial_student_tickets.get()
    )
    tk.Label(
        trial_window,
        text=f"Number of tickets: {total_tickets}",
        font=regular_font
    ).pack(pady=10)

    # Line 6
    tk.Label(
        trial_window,
        text=f"Your total today is £{price:.2f}",
        font=total_font
    ).pack(pady=30)

    # Line 7
    tk.Label(
        trial_window,
        text="How do you want to pay?",
        font=regular_font
    ).pack(pady=10)

    # Line 8 (Buttons for Cash and Card)
    buttons_frame = tk.Frame(trial_window)
    buttons_frame.pack(pady=20)

    tk.Button(
        buttons_frame, text="Cash", font=("Arial", 14),
        command=lambda: trial_cash(price),
        width=12, height=2  # Larger buttons
    ).pack(side=tk.LEFT, padx=20)

    tk.Button(
        buttons_frame, text="Card", font=("Arial", 14),
        command=lambda: trial_card(price),
        width=12, height=2  # Larger buttons
    ).pack(side=tk.RIGHT, padx=20)

# The window must be reset after every new screen
def trial_reset_window():
    try:
        for widget in trial_window.winfo_children():
            widget.destroy()

        # Get absolute path of the image
        image_path = os.path.abspath("train-station-image.png")

    except Exception as e:
        print(f"Warning: Could not reset window - {e}")

def trial_cash(price):
    trial_reset_window()

    # Display the total price
    total_label = tk.Label(trial_window, text=f"Total: £{price:.2f}", font=(FONT, 40))
    total_label.pack(pady=80)

    # Button to insert cash
    insert_button = tk.Button(trial_window, text="Insert Cash",
                        font=(FONT, 30),
                        command=trial_insert_cash)
    insert_button.pack(pady=30)

def trial_insert_cash():
    trial_reset_window()
    # Show "Printing tickets" message for 5 seconds
    printing_label = tk.Label(trial_window, text="Printing tickets...", font=(FONT, 36))
    printing_label.pack(pady=230)

    trial_window.after(2000, trial_show_thank_you)  # Wait for 5 seconds before showing the thank you message

def trial_show_thank_you():
    trial_reset_window()

    # Show thank you message
    thank_you_label = tk.Label(trial_window, text="Thank you. Have a nice day!", font=(FONT, 36))
    thank_you_label.pack(pady=230)

    trial_window.after(3000, trial_close_window)  # Wait for 3 seconds before closing the screen"""

def trial_card(price):
    trial_reset_window()

    # Display the total price
    total_label = tk.Label(trial_window, text=f"Total: £{price:.2f}", font=(FONT, 40))
    total_label.pack(pady=80)

    # Button to insert card
    insert_button = tk.Button(trial_window, text="Insert Card",
                        font=(FONT, 30),
                        command=trial_insert_card)
    insert_button.pack(pady=30)

def trial_insert_card():
    # Clear the previous screen
    trial_reset_window()

    verifying_label = tk.Label(trial_window, text="Verifying payment...", font=(FONT, 36))
    verifying_label.pack(pady=230)

    trial_window.after(2000, trial_show_payment_accepted)  # Wait for 2 seconds before showing payment accepted

def trial_show_payment_accepted():
    # Clear the previous screen
    trial_reset_window()

    payment_label = tk.Label(trial_window, text="Payment accepted. Printing tickets...",
                        wraplength=650,
                        font=("Tahoma", 36))
    payment_label.pack(pady=230)

    trial_window.after(3000, trial_show_thank_you)  # Wait for 3 seconds before showing the thank you message"""

def trial_close_window():

    trial_window.destroy()  # Close the app 
