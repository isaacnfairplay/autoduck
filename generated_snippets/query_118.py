# Generated: 2025-03-19 12:40:40.202764
# Result: [(1, 'Design', datetime.date(2023, 6, 1), datetime.date(2023, 6, 10), 9, 9), (1, 'Development', datetime.date(2023, 6, 11), datetime.date(2023, 6, 25), 14, 23), (2, 'Planning', datetime.date(2023, 6, 5), datetime.date(2023, 6, 15), 10, 10)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create time-tracking project management table
conn.execute('''
CREATE TABLE project_tasks (
    project_id INT,
    task_name VARCHAR,
    start_date DATE,
    end_date DATE,
    duration_days INTEGER
);

INSERT INTO project_tasks VALUES
    (1, 'Design', '2023-06-01', '2023-06-10', 9),
    (1, 'Development', '2023-06-11', '2023-06-25', 14),
    (2, 'Planning', '2023-06-05', '2023-06-15', 10);
'''
)

# Calculate cumulative project task duration
result = conn.execute('''
SELECT
    project_id,
    task_name,
    start_date,
    end_date,
    duration_days,
    SUM(duration_days) OVER (PARTITION BY project_id ORDER BY start_date) as cumulative_project_duration
FROM project_tasks
''').fetchall()

for row in result:
    print(row)