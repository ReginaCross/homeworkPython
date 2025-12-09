import pytest
from models import Student, Course
from sqlalchemy.exc import IntegrityError

class TestStudentCRUD:
    """Тесты для операций CRUD со студентами"""
    
    def test_create_student(self, db_session):
        """Тест создания нового студента"""
        
        student_data = {
            "name": "Иван Иванов",
            "email": "ivan@example.com"
        }
        
        
        new_student = Student(**student_data)
        db_session.add(new_student)
        db_session.commit()
        db_session.refresh(new_student)
        
        
        assert new_student.id is not None
        assert new_student.name == "Иван Иванов"
        assert new_student.email == "ivan@example.com"
        assert new_student.is_active == True
        
        
        db_session.delete(new_student)
        db_session.commit()
    
    def test_update_student(self, db_session):
        """Тест обновления данных студента"""
        
        student = Student(
            name="Петр Петров",
            email="petr@example.com"
        )
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)
        
        
        student.name = "Петр Сидоров"
        student.email = "petr.sidorov@example.com"
        db_session.commit()
        db_session.refresh(student)
        
        
        assert student.name == "Петр Сидоров"
        assert student.email == "petr.sidorov@example.com"
        
        
        db_session.delete(student)
        db_session.commit()
    
    def test_soft_delete_student(self, db_session):
        """Тест мягкого удаления студента"""
        
        student = Student(
            name="Анна Смирнова",
            email="anna@example.com"
        )
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)
        
        student_id = student.id
        
        
        student.is_active = False
        db_session.commit()
        
        
        deleted_student = db_session.query(Student).filter_by(id=student_id).first()
        assert deleted_student is not None
        assert deleted_student.is_active == False
        
        
        db_session.delete(deleted_student)
        db_session.commit()

class TestCourseCRUD:
    """Тесты для операций CRUD с курсами"""
    
    def test_create_course(self, db_session):
        """Тест создания нового курса"""
        
        course_data = {
            "name": "Математика",
            "description": "Курс высшей математики"
        }
        
        
        new_course = Course(**course_data)
        db_session.add(new_course)
        db_session.commit()
        db_session.refresh(new_course)
        
        
        assert new_course.id is not None
        assert new_course.name == "Математика"
        assert new_course.description == "Курс высшей математики"
        assert new_course.is_active == True
        
        
        db_session.delete(new_course)
        db_session.commit()
    
    def test_update_course(self, db_session):
        """Тест обновления данных курса"""
        
        course = Course(
            name="Физика",
            description="Базовый курс физики"
        )
        db_session.add(course)
        db_session.commit()
        db_session.refresh(course)
        
        
        course.name = "Квантовая физика"
        course.description = "Продвинутый курс квантовой физики"
        db_session.commit()
        db_session.refresh(course)
        
        
        assert course.name == "Квантовая физика"
        assert course.description == "Продвинутый курс квантовой физики"
        
        
        db_session.delete(course)
        db_session.commit()
    
    def test_hard_delete_course(self, db_session):
        """Тест полного удаления курса"""
        
        course = Course(
            name="Химия",
            description="Органическая химия"
        )
        db_session.add(course)
        db_session.commit()
        db_session.refresh(course)
        
        course_id = course.id
        
        
        db_session.delete(course)
        db_session.commit()
        
        
        deleted_course = db_session.query(Course).filter_by(id=course_id).first()
        assert deleted_course is None

def test_unique_constraint_violation(self, db_session):
    """Тест нарушения ограничения уникальности"""
    
    student1 = Student(
        name="Иван Иванов",
        email="ivan@example.com"
    )
    db_session.add(student1)
    db_session.commit()
    
    
    student2 = Student(
        name="Петр Петров",
        email="ivan@example.com"  
    )
    db_session.add(student2)
    
    with pytest.raises(IntegrityError):
        db_session.commit()
    
    
    db_session.rollback()
    
   
    db_session.delete(student1)
    db_session.commit()