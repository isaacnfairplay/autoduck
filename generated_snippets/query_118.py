# Generated: 2025-03-19 14:08:41.593405
# Result: [1, 2, 0, 1]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create an array and transform elements using modulo
result = conn.execute('''
    SELECT array_transform([10, 20, 30, 40], x -> x % 3) AS modulo_result
''').fetchone()[0]

print(result)  # Expected output: [1, 2, 0, 1]