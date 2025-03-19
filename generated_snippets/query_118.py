# Generated: 2025-03-19 18:31:24.526512
# Result: [15, 25, 35, 45]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

query = '''
SELECT array_transform([10, 20, 30, 40], x -> x + 5) as incremented_array
'''

result = conn.execute(query).fetchone()[0]
print(result)  # Output: [15, 25, 35, 45]