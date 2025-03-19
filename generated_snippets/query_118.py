# Generated: 2025-03-19 19:42:49.954122
# Result: [(1, 'Alice', Decimal('25.5')), (2, 'Bob', Decimal('30.2')), (3, 'Charlie', Decimal('35.7'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Use VALUES to create inline table with multiple data types
result = conn.execute("""
SELECT * FROM (VALUES
    (1, 'Alice', 25.5),
    (2, 'Bob', 30.2),
    (3, 'Charlie', 35.7)
) AS people(id, name, score)
""").fetchall()

print(result)