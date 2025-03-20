# Generated: 2025-03-19 21:44:28.957807
# Result: [(102, 'Python Programming'), (103, 'Data Science'), (101, 'Python Programming')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a student enrollment tracking system with range joins
conn.execute('''CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name VARCHAR,
    start_date DATE,
    end_date DATE
)''')

conn.execute('''CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date DATE
)''')

conn.execute('''INSERT INTO courses VALUES
    (1, 'Python Programming', '2023-09-01', '2023-12-15'),
    (2, 'Data Science', '2023-10-01', '2024-01-30')''')

conn.execute('''INSERT INTO enrollments VALUES
    (101, 1, '2023-09-05'),
    (102, 1, '2023-09-10'),
    (103, 2, '2023-10-15')''')

# Use range join to find students enrolled in active courses
result = conn.execute('''SELECT 
    e.student_id, 
    c.course_name
FROM enrollments e
JOIN courses c ON 
    e.course_id = c.course_id AND 
    e.enrollment_date BETWEEN c.start_date AND c.end_date
''').fetchall()

for row in result:
    print(f'Student {row[0]} enrolled in {row[1]}')