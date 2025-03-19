# Generated: 2025-03-19 19:23:52.475877
# Result: [([11, 12, 13, 14, 15],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

result = conn.execute('''
    SELECT array_transform([1, 2, 3, 4, 5], x -> x + 10) as transformed_array
''').fetchall()

print(result[0][0])  # Output: [11, 12, 13, 14, 15]