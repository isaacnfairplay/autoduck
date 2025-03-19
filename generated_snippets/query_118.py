# Generated: 2025-03-19 16:21:33.292216
# Result: [4, 9, 16, 25]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table for student grades
conn.execute('''
    CREATE TABLE student_grades (
        student_id INT,
        subject TEXT,
        grade DECIMAL(4,2)
    );

    INSERT INTO student_grades VALUES
        (1, 'Math', 85.50),
        (1, 'Science', 92.25),
        (2, 'Math', 78.00),
        (2, 'Science', 88.75);

    WITH subject_stats AS (
        SELECT 
            subject, 
            AVG(grade) as avg_grade,
            MAX(grade) as max_grade,
            MIN(grade) as min_grade
        FROM student_grades
        GROUP BY subject
    )
    SELECT * FROM subject_stats;
''').fetchall()