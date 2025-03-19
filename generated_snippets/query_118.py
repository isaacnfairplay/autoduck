# Generated: 2025-03-19 17:48:32.423118
# Result: [([2, 4, 6, 8, 10],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Transform numeric array using array_transform
result = conn.execute("""
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * 2) AS doubled_array
""").fetchall()

print(result)  # Expected output: [[2, 4, 6, 8, 10]]