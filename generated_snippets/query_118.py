# Generated: 2025-03-19 08:10:11.242273
# Result: [(1, Decimal('85.50'), Decimal('92.00')), (2, Decimal('78.50'), Decimal('88.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table of student test scores
conn.execute('''
CREATE TABLE student_scores (
    student_id INT,
    subject VARCHAR,
    score DECIMAL(5,2)
);

INSERT INTO student_scores VALUES
    (1, 'Math', 85.5),
    (1, 'Science', 92.0),
    (2, 'Math', 78.5),
    (2, 'Science', 88.0);
''')

# Use PIVOT to transform subject scores into columns
result = conn.execute('''
SELECT 
    student_id,
    MAX(CASE WHEN subject = 'Math' THEN score END) as math_score,
    MAX(CASE WHEN subject = 'Science' THEN score END) as science_score
FROM student_scores
GROUP BY student_id
''').fetchall()

for row in result:
    print(row)