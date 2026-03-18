from pymongo import MongoClient
from datetime import datetime

class UniversitySystem:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client.university_db

    def add_lecturer(self):
        data = {
            "lecturer_id": input("ID преподавателя: "),
            "first_name": input("Имя: "),
            "last_name": input("Фамилия: "),
            "department": input("Кафедра: "),
            "email": input("Email: ")
        }
        self.db.Lectures.insert_one(data)

    def add_student(self):
        data = {
            "student_id": input("ID студента: "),
            "first_name": input("Имя: "),
            "last_name": input("Фамилия: "),
            "group_code": input("Код группы: "),
            "email": input("Email: "),
            "phone": input("Телефон: "),
            "enrollment_year": int(input("Год поступления: "))
        }
        self.db.students.insert_one(data)

    def add_group(self):
        data = {
            "group_code": input("Код группы: "),
            "faculty": input("Факультет: "),
            "students": [], # Массив ссылок
            "curator_id": input("ID куратора: "),
            "start_year": int(input("Год начала: "))
        }
        self.db.groups.insert_one(data)

    def add_course(self):
        data = {
            "course_code": input("Код курса: "),
            "title": input("Название: "),
            "credits": int(input("Кредиты: ")),
            "lecturer_id": input("ID преподавателя: "),
            "semester": int(input("Семестр: ")),
            "description": input("Описание: ")
        }
        self.db.courses.insert_one(data)

    def add_grade(self):
        data = {
            "student_id": input("ID студента: "),
            "course_code": input("Код курса: "),
            "grade": int(input("Оценка: ")),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "type": input("Тип (Экзамен/Зачет): "),
            "lecturer_id": input("ID преподавателя: ")
        }
        self.db.grades.insert_one(data)

    def add_attendance(self):
        data = {
            "student_id": input("ID студента: "),
            "course_code": input("Код курса: "),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "status": input("Статус (присутствует/отсутствует): "),
            "lecturer_id": input("ID преподавателя: "),
            "notes": input("Примечания: ")
        }
        self.db.attendances.insert_one(data)

    def menu(self):
        actions = {
            "1": self.add_student, "2": self.add_group,
            "3": self.add_course, "4": self.add_lecturer,
            "5": self.add_grade, "6": self.add_attendance
        }
        while True:
            print("\n1. Студент 2. Группа 3. Курс 4. Преподаватель 5. Оценка 6. Посещаемость 0. Выход")
            choice = input("Выбор: ")
            if choice == "0":
                break
            if choice in actions:
                actions[choice]()

if __name__ == "__main__":
     app = UniversitySystem()
     app.menu()