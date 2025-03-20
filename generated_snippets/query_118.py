# Generated: 2025-03-19 21:17:23.739721
# Result: [([2, 4, 6, 8, 10],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create array and transform values
result = conn.execute("""
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * 2) AS doubled_array
""").fetchall()

print(result)  # Should output: [[2, 4, 6, 8, 10]]