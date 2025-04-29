from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(10), nullable=False)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create tables
with app.app_context():
    db.create_all()

# Home page (optional)
@app.route('/')
def home():
    return "Welcome to AI Safety Incident API 🚀"

# POST /incidents
@app.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()
    if not data or not all(k in data for k in ('title', 'description', 'severity')):
        return jsonify({'error': 'Missing data'}), 400

    new_incident = Incident(
        title=data['title'],
        description=data['description'],
        severity=data['severity']
    )
    db.session.add(new_incident)
    db.session.commit()

    return jsonify({
        "id": new_incident.id,
        "title": new_incident.title,
        "description": new_incident.description,
        "severity": new_incident.severity,
        "reported_at": new_incident.reported_at.isoformat()
    }), 201

# GET /incidents
@app.route('/incidents', methods=['GET'])
def get_all_incidents():
    incidents = Incident.query.all()
    return jsonify([{
        "id": i.id,
        "title": i.title,
        "description": i.description,
        "severity": i.severity,
        "reported_at": i.reported_at.isoformat()
    } for i in incidents])

if __name__ == '__main__':
    app.run(debug=True)
