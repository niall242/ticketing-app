from tkinter import *
from tkinter import messagebox
import os

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
start_zone = None
destination_zone = None
selected_tickets = {"adult": 0, "child": 0, "senior": 0, "student": 0}

map_image_path = os.path.join(os.path.dirname(__file__), "underground-map.PNG")  # Path to the map image

# Initialize main window
window = Tk()
window.title("Centrala Underground Ticket App")
window.geometry("1050x820")

def reset_window():
    for widget in window.winfo_children():
        widget.destroy()

def show_error(message):
    messagebox.showerror("Error", message)

def screen_1():
    reset_window()

    Label(window, text="Welcome to Centrala Underground", font=("Arial", 16, "bold")).pack(pady=5)

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

# Initialize the app
screen_1()
window.mainloop()
