# Generated: 2025-03-19 20:21:49.647844
# Result: ([1, 4, 9, 16, 25], [2, 4])
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate advanced array manipulation and transformation
result = conn.execute('''
    SELECT 
        array_transform([1, 2, 3, 4, 5], x -> x * x) AS squared_list,
        array_filter([1, 2, 3, 4, 5], x -> x % 2 = 0) AS even_numbers
''').fetchone()

print("Squared List:", result[0])  # [1, 4, 9, 16, 25]
print("Even Numbers:", result[1])  # [2, 4]