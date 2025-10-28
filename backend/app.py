from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# PostgreSQL Config
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_PORT", 5432)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# SCP Model
class SCP(db.Model):
    __tablename__ = 'scp_subjects'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(50))
    class_ = db.Column("class", db.String(50))
    description = db.Column(db.Text)
    containment = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "item": self.item,
            "class": self.class_,
            "description": self.description,
            "containment": self.containment
        }

# Routes
@app.route('/api/scp', methods=['GET'])
def get_all_scp():
    scps = SCP.query.all()
    return jsonify([s.to_dict() for s in scps])

@app.route('/api/scp/<int:id>', methods=['GET'])
def get_scp(id):
    s = SCP.query.get_or_404(id)
    return jsonify(s.to_dict())

@app.route('/api/scp', methods=['POST'])
def add_scp():
    data = request.json
    new_scp = SCP(
        item=data['item'], 
        class_=data['class'], 
        description=data['description'], 
        containment=data['containment']
    )
    db.session.add(new_scp)
    db.session.commit()
    return jsonify(new_scp.to_dict()), 201

@app.route('/api/scp/<int:id>', methods=['PUT'])
def update_scp(id):
    data = request.json
    s = SCP.query.get_or_404(id)
    s.item = data['item']
    s.class_ = data['class']
    s.description = data['description']
    s.containment = data['containment']
    db.session.commit()
    return jsonify(s.to_dict())

@app.route('/api/scp/<int:id>', methods=['DELETE'])
def delete_scp(id):
    s = SCP.query.get_or_404(id)
    db.session.delete(s)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
