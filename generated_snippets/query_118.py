# Generated: 2025-03-19 11:38:59.765644
# Result: [(1, 'Calculus', 4), (4, 'Statistics', 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample courses table
conn.execute('''
CREATE TABLE courses (
    course_id INTEGER,
    name VARCHAR,
    department VARCHAR,
    credits INTEGER
);

INSERT INTO courses VALUES
(1, 'Calculus', 'Mathematics', 4),
(2, 'Computer Science', 'CS', 3),
(3, 'Physics', 'Science', 4),
(4, 'Statistics', 'Mathematics', 3);
''')

# Select courses by department with advanced filtering
result = conn.execute('''
SELECT 
    course_id, 
    name, 
    credits
FROM courses
WHERE department = 'Mathematics'
ORDER BY credits DESC
''').fetchall()

for row in result:
    print(f"Course {row[0]}: {row[1]} ({row[2]} credits)")