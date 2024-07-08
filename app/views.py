from flask import Blueprint, request, jsonify
from .models import db, patient_details

bp = Blueprint('views', __name__)

@bp.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    diagnosis = data.get('diagnosis')

    if not all([name, age, gender, diagnosis]):
        return jsonify({"error": "Missing data"}), 400

    new_patient = patient_details(name=name, age=age, gender=gender, diagnosis=diagnosis)
    db.session.add(new_patient)
    db.session.commit()

    return jsonify(new_patient.to_dict()), 201

@bp.route('/patients', methods=['GET'])
def get_patients():
    patients = patient_details.query.all()
    return jsonify([patient.to_dict() for patient in patients]), 200

@bp.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    patient = patient_details.query.get_or_404(id)
    return jsonify(patient.to_dict()), 200

@bp.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    data = request.get_json()
    patient = patient_details.query.get_or_404(id)

    patient.name = data.get('name', patient.name)
    patient.age = data.get('age', patient.age)
    patient.gender = data.get('gender', patient.gender)
    patient.diagnosis = data.get('diagnosis', patient.diagnosis)

    db.session.commit()
    return jsonify(patient.to_dict()), 200

@bp.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    patient = patient_details.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return '', 204
