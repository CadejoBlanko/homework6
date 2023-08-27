import sqlite3
from faker import Faker
import random

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

create_tables_query = """
CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY,
  name TEXT,
  group_id INTEGER,
  FOREIGN KEY (group_id) REFERENCES groups(id)
);

CREATE TABLE IF NOT EXISTS groups (
  id INTEGER PRIMARY KEY,
  group_name TEXT,
  subjects TEXT
);

CREATE TABLE IF NOT EXISTS teachers (
  id INTEGER PRIMARY KEY,
  name TEXT
);

CREATE TABLE IF NOT EXISTS subjects (
  id INTEGER PRIMARY KEY,
  subject_name TEXT,
  teacher_id INTEGER,
  FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

CREATE TABLE IF NOT EXISTS evaluations (
  student_id INTEGER,
  subject_id INTEGER,
  grade INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (subject_id) REFERENCES subjects(id)
);
"""

cursor.executescript(create_tables_query)
conn.commit()

fake = Faker()

NUM_STUDENTS = 30
NUM_GROUPS = 3
NUM_SUBJECTS = 8
NUM_TEACHERS = 5
MAX_EVALUATIONS_PER_STUDENT = 20

groups = []
for _ in range(1, NUM_GROUPS+1):
    group_name = fake.word().upper()
    subjects = ", ".join([fake.word() for _ in range(random.randint(3, 6))])
    groups.append((None, group_name, subjects))

cursor.executemany("INSERT INTO groups VALUES (?, ?, ?)", groups)
conn.commit()

teachers = []
for _ in range(1, NUM_TEACHERS+1):
    teacher_name = fake.name()
    teachers.append((None, teacher_name))

cursor.executemany("INSERT INTO teachers VALUES (?, ?)", teachers)
conn.commit()

subjects = []
for _ in range(1, NUM_SUBJECTS+1):
    subject_name = fake.word().capitalize()
    teacher_id = random.randint(1, NUM_TEACHERS)
    subjects.append((None, subject_name, teacher_id))

cursor.executemany("INSERT INTO subjects VALUES (?, ?, ?)", subjects)
conn.commit()

students = []
evaluations = []
for _ in range(1, NUM_STUDENTS+1):
    student_name = fake.name()
    group_id = random.randint(1, NUM_GROUPS)
    students.append((None, student_name, group_id))
    
    for subject_id in range(1, NUM_SUBJECTS+1):
        for _ in range(random.randint(1, MAX_EVALUATIONS_PER_STUDENT)):
            evaluation = random.randint(1, 12)
            evaluations.append((student_name, subject_id, evaluation))

cursor.executemany("INSERT INTO students VALUES (?, ?, ?)", students)
cursor.executemany("INSERT INTO evaluations (student_id, subject_id, grade) VALUES (?, ?, ?)", evaluations)
conn.commit()
conn.commit()

queries = [
    "query_1.sql",
    "query_2.sql",
    "query_3.sql",
    "query_4.sql",
    "query_5.sql",
    "query_6.sql",
    "query_7.sql",
    "query_8.sql",
    "query_9.sql",
    "query_10.sql"
]

for query_file in queries:
    with open(query_file, "r") as f:
        query = f.read()
        cursor.execute(query)
        result = cursor.fetchall()
        print(f"Query from {query_file}:")
        print(result)
        print("~~" * 50)

conn.close()