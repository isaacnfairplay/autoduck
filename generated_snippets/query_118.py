# Generated: 2025-03-19 14:24:16.831950
# Result: [([2.0, 3.0, 4.0, 5.0],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute('SELECT array_transform([4, 9, 16, 25], x -> SQRT(x)) as sqrt_array').fetchall()
print(result[0][0])