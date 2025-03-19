# Generated: 2025-03-19 16:02:48.801751
# Result: [([2, 4, 6],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate array_filter to extract even numbers
result = conn.execute("""
    SELECT array_filter([1, 2, 3, 4, 5, 6], x -> x % 2 = 0) AS even_numbers
""").fetchall()

print(result)  # Expected: [[2, 4, 6]]