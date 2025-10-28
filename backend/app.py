from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from db_config import host, user, password, database, port

app = Flask(__name__)
CORS(app)

# PostgreSQL connection URI
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# SCP Subjects Model
class SCPSubject(db.Model):
    __tablename__ = 'scp_subjects'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(50))
    class_type = db.Column(db.String(50))
    description = db.Column(db.Text)
    containment = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'item': self.item,
            'class': self.class_type,
            'description': self.description,
            'containment': self.containment
        }

# Routes
@app.route('/api/scp', methods=['GET'])
def get_all_scp():
    scps = SCPSubject.query.all()
    return jsonify([scp.to_dict() for scp in scps])

@app.route('/api/scp/<int:id>', methods=['GET'])
def get_scp(id):
    scp = SCPSubject.query.get_or_404(id)
    return jsonify(scp.to_dict())

@app.route('/api/scp', methods=['POST'])
def add_scp():
    data = request.get_json()
    new_scp = SCPSubject(
        item=data['item'],
        class_type=data['class'],
        description=data['description'],
        containment=data['containment']
    )
    db.session.add(new_scp)
    db.session.commit()
    return jsonify(new_scp.to_dict()), 201

@app.route('/api/scp/<int:id>', methods=['PUT'])
def update_scp(id):
    scp = SCPSubject.query.get_or_404(id)
    data = request.get_json()
    scp.item = data.get('item', scp.item)
    scp.class_type = data.get('class', scp.class_type)
    scp.description = data.get('description', scp.description)
    scp.containment = data.get('containment', scp.containment)
    db.session.commit()
    return jsonify(scp.to_dict())

@app.route('/api/scp/<int:id>', methods=['DELETE'])
def delete_scp(id):
    scp = SCPSubject.query.get_or_404(id)
    db.session.delete(scp)
    db.session.commit()
    return jsonify({'message': 'Deleted successfully'}), 200

if __name__ == '__main__':
    # Create tables if not exist (first time)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
