# Generated: 2025-03-19 15:23:39.812796
# Result: [1, 8, 27, 64, 125]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Transform numeric array by applying cube operation
result = conn.execute("""SELECT array_transform([1, 2, 3, 4, 5], x -> x * x * x) AS cubed_array""").fetchone()[0]

print(result)  # Output: [1, 8, 27, 64, 125]