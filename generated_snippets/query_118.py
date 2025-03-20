# Generated: 2025-03-19 20:19:18.982769
# Result: [11, 12, 13, 14, 15]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("""
    SELECT array_transform([1, 2, 3, 4, 5], x -> x + 10) AS augmented_list
""").fetchone()[0]

print(result)  # Outputs: [11, 12, 13, 14, 15]