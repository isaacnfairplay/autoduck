# Generated: 2025-03-19 21:26:55.527824
# Result: [([2, 3, 4, 5, 6],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("""
    SELECT array_transform([1, 2, 3, 4, 5], x -> x + 1) AS incremented_array
""").fetchall()

print(result)