# Generated: 2025-03-19 20:15:47.992856
# Result: [2, 4, 6, 8, 10]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a list of numbers and transform each element
result = conn.execute("""
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * 2) AS doubled_list
""").fetchone()[0]

print(result)  # Outputs: [2, 4, 6, 8, 10]