# Generated: 2025-03-19 18:08:17.776693
# Result: [([20, 40, 60, 80],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

result = conn.execute('''
    SELECT array_transform([10, 20, 30, 40], x -> x * 2) AS doubled_array
''').fetchall()

print(result[0][0])  # Outputs: [20, 40, 60, 80]