# Generated: 2025-03-19 13:45:53.611560
# Result: [([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [False, True, False, True, False])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate array_transform to convert list and apply mathematical operations
result = conn.execute("""
    SELECT 
        [1, 2, 3, 4, 5] as original_list,
        array_transform([1, 2, 3, 4, 5], x -> x * 2) as doubled_list,
        array_transform([1, 2, 3, 4, 5], x -> x % 2 = 0) as is_even_list
""").fetchall()

print(result)