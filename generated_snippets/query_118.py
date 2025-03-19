# Generated: 2025-03-19 11:29:21.626240
# Result: [(2, 'Math', Decimal('78.20'), 0.0), (1, 'Math', Decimal('85.50'), 1.0), (2, 'Science', Decimal('88.70'), 0.0), (1, 'Science', Decimal('92.30'), 1.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table tracking student grades
conn.execute('''
CREATE TABLE student_grades (
    student_id INTEGER,
    subject VARCHAR,
    grade DECIMAL(5,2)
);

INSERT INTO student_grades VALUES
(1, 'Math', 85.5),
(1, 'Science', 92.3),
(2, 'Math', 78.2),
(2, 'Science', 88.7);
''')

# Use window functions to calculate grade percentiles
result = conn.execute('''
SELECT 
    student_id, 
    subject, 
    grade,
    PERCENT_RANK() OVER (PARTITION BY subject ORDER BY grade) as percentile
FROM student_grades
''').fetchall()

for row in result:
    print(f"Student {row[0]} in {row[1]}: Grade {row[2]} (Percentile: {row[3]:.2%})")