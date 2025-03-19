# Generated: 2025-03-19 17:52:10.721603
# Result: [([11, 12, 13, 14, 15],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

result = conn.execute('''
    SELECT array_transform([1, 2, 3, 4, 5], x -> x + 10) AS increased_array
''').fetchall()

print(result)  # Expected output: [[11, 12, 13, 14, 15]]