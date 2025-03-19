# Generated: 2025-03-19 14:15:38.921365
# Result: [1, 0, 2, 1]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

result = conn.execute('''
    SELECT array_transform([10, 15, 20, 25], x -> x % 3) as remainder_array
''').fetchone()[0]

print(result)