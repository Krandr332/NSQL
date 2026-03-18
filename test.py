import time
import random
from pymongo import MongoClient


def stress_test(n=10000):
    client = MongoClient("mongodb://localhost:27017/")
    db = client.university_db
    print(f"Запуск теста: вставка {n} записей...")

    start = time.time()
    for i in range(n):
        db.grades.insert_one({
            "student_id": f"ST-{random.randint(1000, 9999)}",
            "course_code": f"C-{random.randint(1, 50)}",
            "grade": random.randint(2, 5),
            "date": "2026-03-16"
        })
    end = time.time()

    total_time = end - start
    print(f"Результат: {n} записей за {total_time:.2f} сек.")
    print(f"Производительность: {n / total_time:.2f} оп/сек")


if __name__ == "__main__":
    stress_test(5000)