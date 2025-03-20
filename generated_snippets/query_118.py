# Generated: 2025-03-19 21:38:08.880067
# Result: [([20, 40, 60],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Transform array elements using a lambda function
result = conn.sql('''
    SELECT array_transform([10, 20, 30], x -> x * 2) as doubled_array
''').fetchall()

print(result)