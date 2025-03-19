# Generated: 2025-03-19 13:32:05.238891
# Result: [11, 4, 13, 16, 15]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Advanced array transformation with conditional mapping
result = conn.execute(
    'SELECT array_transform([1, 2, 3, 4, 5], x -> CASE WHEN x % 2 = 0 THEN x * x ELSE x + 10 END) AS transformed_list'
).fetchone()[0]

print(result)  # Output: [11, 4, 13, 16, 15]