# Generated: 2025-03-19 18:23:49.343747
# Result: [11, 12, 13, 14, 15]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

query = '''
SELECT array_transform([1, 2, 3, 4, 5], x -> x + 10) AS transformed_array;
'''

result = conn.execute(query).fetchone()[0]
print(result)  # Should output: [11, 12, 13, 14, 15]