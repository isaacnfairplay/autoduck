# Generated: 2025-03-19 16:33:50.487683
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("SELECT array_transform([1,2,3,4,5], x -> x * x) as squared_values").fetchall()
print(result)