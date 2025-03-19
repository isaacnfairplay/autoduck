# Generated: 2025-03-19 14:46:39.574341
# Result: [1.0, 4.0, 9.0, 16.0, 25.0]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

result = conn.execute("""
    SELECT array_transform([1, 2, 3, 4, 5], x -> POWER(x, 2)) AS squared_array
""").fetchone()[0]

print(result)  # Expected: [1, 4, 9, 16, 25]