# Generated: 2025-03-19 14:13:05.854932
# Result: ('David', Decimal('88.70'), None)
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with employee performance data
conn.execute('CREATE TABLE performance (employee TEXT, department TEXT, score DECIMAL(5,2))')
conn.execute("""INSERT INTO performance VALUES
    ('Alice', 'Sales', 87.5),
    ('Bob', 'Marketing', 92.3),
    ('Charlie', 'Sales', 95.1),
    ('David', 'Marketing', 88.7)
""")

# Use PIVOT to transform department performance into columns
result = conn.execute('''
    PIVOT performance
    ON department
    USING MAX(score)
''').fetchone()

print(f"Sales Max Score: {result[0]}, Marketing Max Score: {result[1]})")