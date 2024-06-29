# Tkinter Data Entry Form with SQLite

This repository features a functional data entry form built using Tkinter, Python’s standard GUI toolkit, and SQLite for datastorage. This project demonstrates the creation of a graphical user interface for collecting user information and course details, with built-in validation to ensure completeness and accuracy.

## Features

- **User Information Collection**: The form gathers essential user details including:
  - First Name
  - Last Name
  - Title (Mr., Ms., Dr.)
  - Age (using a Spinbox for age selection)
  - Nationality (selectable from a dropdown list)

- **Course Information Collection**: Users can provide their course-related details:
  - Registration Status (indicating whether currently registered)
  - Number of Completed Courses (using a Spinbox)
  - Number of Semesters (using a Spinbox)

- **Validation**: The form includes checks to ensure that:
  - Both first name and last name are provided.
  - Terms and conditions are accepted before submission.

- **User Feedback**: If required fields are missing or terms are not accepted, the application will display a warning message.

## Prerequisites

- Python 3.x
- SQLite

## Setup

1. Clone the repository:
    ```bash
    git clone  https://github.com/nahili-ansha/Tkinter-SQLite-Data-Entry.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Tkinter-SQLite-Data-Entry
    ```

## Usage

1. Run the script:
    ```bash
    python main.py
    ```

2. Fill out the form and submit to insert data into the database.




