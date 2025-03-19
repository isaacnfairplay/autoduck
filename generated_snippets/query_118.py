# Generated: 2025-03-19 14:13:55.584839
# Result: [1, 2, 0, 1, 2]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Transform numeric array using modulo 3 operation
result = conn.execute("""
    SELECT array_transform([10, 20, 30, 40, 50], x -> x % 3) AS modulo_result
""").fetchone()[0]

print(result)  # Output: [1, 2, 0, 1, 2]