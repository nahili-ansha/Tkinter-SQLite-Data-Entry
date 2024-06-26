import tkinter
from tkinter import messagebox  # To use messagebox
from tkinter import ttk  # To use combobox


def enter_data():
    accepted = accept_var.get()  # Get the value of the acceptance variable
    if accepted == "Accepted":
        # User info
        first_name = first_name_entry.get()  # Get the entered first name
        last_name = last_name_entry.get()  # Get the entered last name

        if first_name and last_name:  # Check if first name and last name are provided
            title = title_combobox.get()  # Get the selected title
            age = age_spinbox.get()  # Get the entered age
            nationality = Nationality_combobox.get()  # Get the selected nationality
            # Course info
            registration_status = reg_status_var.get()  # Get the registration status
            numcourses = numcourses_spinbox.get()  # Get the number of completed courses
            semesters = semesters_spinbox.get()  # Get the number of semesters
        else:
            # Show warning if first name or last name is missing
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        # Show warning if terms are not accepted
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms.")
    
    # Print the entered data to the console
    print(f"First Name: {first_name}  Last Name: {last_name}")
    print(f"Title: {title}  Age: {age}  Nationality: {nationality}")
    print(f"# Courses: {numcourses}  # Semesters: {semesters}")
    print(f"Registration status: {registration_status}")
    print("---------------------------------------------------------")

# Create the main window
window = tkinter.Tk()
window.title("Data Entry Form")

# Create a main frame to hold all widgets
frame = tkinter.Frame(window)
frame.pack()

# User Information
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_spinbox.grid(row=3, column=0)
age_label.grid(row=2, column=0)

Nationality_label = tkinter.Label(user_info_frame, text="Nationality")
Nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
Nationality_combobox.grid(row=3, column=1)
Nationality_label.grid(row=2, column=1)

# Add padding to all widgets in the user info frame
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Course Information
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")
registered_label.grid(row=0, column=0)

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

semesters_label = tkinter.Label(courses_frame, text="# Semesters")
semesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
semesters_label.grid(row=0, column=2)
semesters_spinbox.grid(row=1, column=2)

# Add padding to all widgets in the courses frame
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# Run the main event loop
window.mainloop()
