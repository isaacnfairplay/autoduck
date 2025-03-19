# Generated: 2025-03-19 15:05:40.792831
# Result: ([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 4, 5])
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create array of numbers and transform using DuckDB functions
result = conn.execute('''
    SELECT 
        [1, 2, 3, 4, 5] as original_array,
        array_transform([1, 2, 3, 4, 5], x -> x * 2) as doubled_array,
        array_filter([1, 2, 3, 4, 5], x -> x > 2) as filtered_array
''').fetchone()

print(f'Original: {result[0]}')
print(f'Doubled:  {result[1]}')
print(f'Filtered: {result[2]}')