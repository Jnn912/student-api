from flask import jsonify, request
from app import app, db
from app.models import Student

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict())

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student = Student(
        name=data['name'],
        grade=data['grade'],
        email=data['email']
    )
    db.session.add(student)
    db.session.commit()
    return jsonify(student.to_dict()), 201

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    
    student.name = data['name']
    student.grade = data['grade']
    student.email = data['email']
    
    db.session.commit()
    return jsonify(student.to_dict())

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return '', 204