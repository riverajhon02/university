from fastapi import HTTPException
from models.student import Student
from database import students_db

class StudentController:
    @staticmethod
    def get_all()-> list[dict]:
        return students_db
    
    @staticmethod
    def get_by_id(student_id: int)->dict:
        for student in students_db:
            if student["id"] == student_id:
                return student
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")    


    @staticmethod
    def create(student: Student)->dict:
        new_student  = student.dict()
        new_student["id"] = len(students_db) + 1
        students_db.append(new_student)
        return new_student