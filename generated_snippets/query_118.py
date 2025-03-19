# Generated: 2025-03-19 18:01:39.695258
# Result: [([15, 25, 35, 45],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

result = conn.execute('''
    SELECT array_transform([5, 15, 25, 35], x -> x + 10) AS transformed_array
''').fetchall()

print(result[0][0])  # Outputs: [15, 25, 35, 45]