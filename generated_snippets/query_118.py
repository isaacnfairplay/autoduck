# Generated: 2025-03-19 16:13:45.994501
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Square list elements using array_transform
result = conn.execute("""
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) AS squared_values
""").fetchall()

print(result)  # Outputs: [[1, 4, 9, 16, 25]]