*TICKETING SYSTEM MAIN APP*

*PLEASE DOWNLOAD ALL FILES TO THE SAME FOLDER AND THEN RUN MAIN.PY*

The program is mainly modular, every screen is a built inside a function
To move between screens the navigation buttons use "command" to bind a function to it. When the button is pressed the function is called and another screen is opened  

-------------------------------------------------------------------------------------------------------------------

The program uses the Tkinter GUI toolkit
TKINTER FEATURES USED: 
PhotoImage - image upload 
widgets - the building blocks of Tkinter (labels, frames, buttons etc)
Label - general purpose display for text
Frames - organizes things into sections
StringVar - a class in Tkinter. It can bind to widgets such as buttons or labels, so can then be changed dynamically
messagebox - pop up message boxes
Button 
Radiobutton - only 1 can be selected at a time
Configuration of the main window - Title, size, reset etc.
Confuguration of widgets - font, size, colour, placement etc.

-------------------------------------------------------------------------------------------------------------------

PYTHON FEATURES USED:
pre-installed modules - reusable pieces of code
lists - organizes data into iterable indexes
dictionaries - organizes data into key/value pairs
global variables - can be used anywhere in the code
local variables - only usable within its function
classes - blueprint for creating objects. Also reusable
functions - perform a specific task
if/elif/else - makes the program make a decision, and then the path will change based on the decision
for loop - iterates over something and executes block of code multiple times. This helped when creating the ticket selection buttons
dictionary comprehension - an efficient way of creating a new dictionary using details from a previous dictionary

-------------------------------------------------------------------------------------------------------------------

REGARDING OOP

A class is created for the travel ticket so every ticket can be unique. Each ticket also has an ID using "import uuid"

A print ticket method is added, so they could be easily printed out at a later date

I decided against turning the app itself in to a class because it would just encapsulate the whole code in a class, making it too bloated (eg. lots of "self.") 

I decided a UML was not necessary because there is only 1 class, there is nothing to relate the class to.

-------------------------------------------------------------------------------------------------------------------

WAYS VALIDATION WAS USED:

Several error screens are implemented in case there is wrong user input, including a validate_selection function

Exception handling is used in reset_window function and calculate_total_fare function

There are a few places where I have added debugging to make sure what is printed on the terminal is the expected value 

The following test plan has been created:

+----------+--------------------+----------------------------------------------+-------------------------------+---------------+------------+
| Test ID  | Feature            | Test Steps                                  | Expected Result               | Actual Result | Pass/Fail  |
+----------+--------------------+----------------------------------------------+-------------------------------+---------------+------------+
| TC001    | Screen Navigation  | Start at Screen 1 → Click "Next" → Screen 2 | Screen 2 loads correctly      |               |            |
| TC002    | Station Selection  | Select "Central" → Click "Next"             | Moves to destination screen   |               |            |
| TC003    | Invalid Selection  | Click "Next" without selecting a station    | Shows error message           |               |            |
| TC004    | Fare Calculation   | Select "Central" to "Downtown" → 2 Adults   | Price = $126.30               |               |            |
| TC005    | Payment Handling   | Select Card → Click "Insert Card"           | Shows "Verifying Payment..."  |               |            |
| TC006    | Print Ticket       | Click "Print Ticket"                        | Prints ticket with correct ID |               |            |
| TC007    | Reset Window       | Click "Back" multiple times                 | Returns to Screen 1 smoothly  |               |            |
| TC008    | Error Handling     | Enter invalid zone selection                | Shows "Invalid zone" error    |               |            |
+----------+--------------------+----------------------------------------------+-------------------------------+---------------+------------+

All tests have passed, except TC005 and TC006 becuase the payment and printing features have not been implemented yet

There was much more testing of the fare calculation. There was 9 scenarios in the logic from starting point to destination. All 9 scenarios were tested, with variations of ticket types included. All tests showed correct ticket prices.

-------------------------------------------------------------------------------------------------------------------

*TICKETING SYSTEM TRIAL APP*

I have decided to implement a trial version of the ticketing app

This can be accessed with the new help button, which is in the top right corner of the screen

The help button shows a helpline number, and also the option to use the trial version

------------------------------------------------------------------------------------------------------------------- 

FUNCTIONALITY

The trial version has the following features:

The map is removed from the main screen. The user chooses their station directly. Price calculation is still made per zone but this is all done in the background. There is map button in the top corner of the screen that the user can view if necessary

The pricing system is more comprehensive. There are now 33 travel scenarios instead of 9

Users are charged twice if they travel through the same zone twice. The price per zone is lowered to compensate for the extra calculations

A return feature is added

Current time is displayed on the main screen

Stations are arranged aplhabetically for easier reading

The user can choose their departing station if necessary but it is default set to the current station (using station IDs)

The user has the option to buy a ticket for a journey in the future, up to 1 month in advance

The user now chooses their time slots. This could allow for a peak/off peak pricing feature if necessary

Similar testing was done on this, as was done to the original app

Although this version is technically more complicated, it could make the buying experience faster - there are only 2 screens before the user is taken to the payment gateway

-------------------------------------------------------------------------------------------------------------------

This trial version is a response to user feedback:

Some users don't want to look at a map and find their zone, they are in a rush and want to print a ticket out as quickly as possible. They know their starting station and destination station

There is some inconsistencies with the current pricing calculation; because only zones are selected, it means a user can pay for too many zones or not enough zones
eg. 
Travelling from Agralle to Docia, the user actually only stays in 1 zone but is charged for 2
If a user travels from Zord to Ederif, the default downtown to downtown journey is 3 zones. It is actually travelling through 5 zones

The trial app is trying to create a faster and more accurate user experience



