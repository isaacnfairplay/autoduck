# Generated: 2025-03-19 13:24:32.243225
# Result: [3, 4, 5]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate array filter with predicate
result = conn.execute(
    'SELECT array_filter([1, 2, 3, 4, 5], x -> x > 2) AS filtered_list'
).fetchone()[0]

print(result)  # Output: [3, 4, 5]