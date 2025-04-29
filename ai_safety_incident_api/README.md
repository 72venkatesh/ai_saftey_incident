# AI Safety Incident Log API

This project is a simple RESTful API built using **Python Flask** and **SQLite** to log and manage AI safety incidents.  
It was developed as part of a backend development assignment for HumanChain AI Safety Startup.

---

## 📚 Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy (ORM)
- SQLite (local database)

---

## 🚀 How to Run This Project Locally

### 1. Clone the project or download the zip
Unzip if necessary.

### 2. Install Python dependencies
Open a terminal inside the project folder and run:

```bash
pip install -r requirements.txt

### Run the Flask server
python app.py

##you should see 
Running on http://127.0.0.1:5000/

### How to Test API Endpoints
###Example: POST /incidents
# POST http://127.0.0.1:5000/incidents
# Content-Type: application/json

# {
#   "title": "Chatbot Error",
#   "description": "Bot gave wrong advice",
#   "severity": "High"
# }
##Created by a passionate learne for HumanChain AI Safety assignmet
# Thank you for the opportunity!


