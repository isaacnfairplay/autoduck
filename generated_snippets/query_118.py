# Generated: 2025-03-19 15:25:34.203138
# Result: [2, 4, 6, 8]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and transform an array using array_transform
result = conn.execute("""
    SELECT array_transform([1, 2, 3, 4], x -> x * 2) as doubled_array
""").fetchone()[0]

print(f'Original: [1, 2, 3, 4], Transformed: {result}')