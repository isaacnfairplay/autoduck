# Generated: 2025-03-19 15:58:36.699743
# Result: [('temperature', 98.9, 2), ('pH', 6.9, 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table of scientific measurements
conn.execute('''CREATE TABLE experiments (
    experiment_id INTEGER,
    measurement_type VARCHAR,
    value DOUBLE,
    significant BOOLEAN
)''')

conn.execute('''INSERT INTO experiments VALUES
    (1, 'temperature', 98.6, TRUE),
    (2, 'temperature', 99.2, TRUE),
    (3, 'pH', 7.0, FALSE),
    (4, 'pH', 6.8, TRUE)''')

# Demonstrate conditional aggregation with complex filtering
result = conn.execute('''
SELECT 
    measurement_type, 
    AVG(value) as avg_value,
    SUM(CASE WHEN significant THEN 1 ELSE 0 END) as significant_count
FROM experiments
GROUP BY measurement_type
''').fetchall()

for row in result:
    print(f"Type: {row[0]}, Average: {row[1]}, Significant Measurements: {row[2]}")