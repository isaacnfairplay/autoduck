# Generated: 2025-03-19 18:26:21.131990
# Result: [11, 12, 13, 14]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
query = '''
SELECT array_transform([1, 2, 3, 4], x -> x + 10) as incremented_array
'''

result = conn.execute(query).fetchone()[0]
print(result)