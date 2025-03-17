# Generated: 2025-03-17 19:59:27.621464
# Result: [('David', 'Engineering', Decimal('75000.000'), 75000.0, Decimal('500000.000'), 1), ('Bob', 'Marketing', Decimal('60000.000'), 60000.0, Decimal('200000.000'), 2), ('Charlie', 'Sales', Decimal('55000.000'), 52500.0, Decimal('250000.000'), 3), ('Alice', 'Sales', Decimal('50000.000'), 52500.0, Decimal('250000.000'), 4)]
# Valid: True
import duckdb

# Create an in-memory DuckDB connection
conn = duckdb.connect(':memory:')

# Create a recursive common table expression (CTE) to generate a sequence
query = '''
WITH RECURSIVE
  number_sequence(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM number_sequence WHERE n < 10
  )
SELECT n FROM number_sequence
'''

# Execute the recursive query
results = conn.execute(query).fetchall()
for row in results:
    print(row[0])

conn.close()