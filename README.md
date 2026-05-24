E-Voting/
│
├── app.py
├── database.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── vote.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── images/
│
└── README.md
app.py

Main Python Flask program.
Contains:
Routes
Login logic
Voting system
Database connection

database.db
Stores:
User details
Votes
Candidates
Usually created using SQLite.

templates Folder
Contains HTML pages.
Example:
login page
voting page
result page

static Folder
Contains:
CSS
Images
JavaScript
Example:
style.css

requirements.txt
Contains project libraries.
Example:
flask
sqlite3

README.md
Project description file shown on GitHub.
Example:
# E-Voting System
A simple online voting system using Flask and Python.
