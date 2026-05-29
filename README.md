# Student Attendance Management System

A desktop attendance management application built with Python, Tkinter, CustomTkinter, Pillow, and SQLite. The app is designed for a VIT Pune BTEH Semester 2 project and supports separate teacher and student workflows.

## Features

- Role-based login for teachers and students
- Teacher dashboard with attendance summary cards
- Add and delete student records
- Mark bulk attendance as Present or Absent
- Search students by roll number or name
- View student attendance history and percentage
- Generate subject-wise attendance reports
- Export reports as CSV files
- SQLite database initialization on startup

## Tech Stack

- Python
- Tkinter
- CustomTkinter
- Pillow
- SQLite

## Project Structure

```text
.
|-- main.py
|-- requirements.txt
|-- vit logo1.jpg
|-- data/
|   `-- attendance.db
|-- database/
|   |-- __init__.py
|   `-- db_manager.py
|-- gui/
|   |-- __init__.py
|   |-- add_student.py
|   |-- app.py
|   |-- attendance_report.py
|   |-- login.py
|   |-- mark_attendance.py
|   |-- search_student.py
|   |-- student_dashboard.py
|   `-- styles.py
|-- reports/
`-- utils/
    |-- __init__.py
    `-- validators.py
```

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment.

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
python main.py
```

The database is initialized automatically when the app starts.

## Default Login

Teacher login:

```text
Teacher ID: PY-TEACH
Password: python123
```

Student login requires a student record to already exist in the database. Students can log in with their roll number and full name if they belong to branch `CS A`.

## Notes

- Attendance data is stored in `data/attendance.db`.
- Report CSV files can be exported from the Reports screen.
- The default teacher is assigned to the Python subject.
