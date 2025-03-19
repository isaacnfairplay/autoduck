# Generated: 2025-03-19 17:57:18.537494
# Result: [([2, 3, 4, 5, 6],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

result = conn.execute('''
    SELECT array_transform([1, 2, 3, 4, 5], x -> x + 1) AS incremented_array
''').fetchall()

print(result)  # Expected output: [[2, 3, 4, 5, 6]]