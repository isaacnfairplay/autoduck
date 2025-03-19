# Generated: 2025-03-19 13:05:51.271032
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample array of numbers
conn.execute('CREATE TABLE numbers (arr INTEGER[])')
conn.execute('INSERT INTO numbers VALUES ([1, 2, 3, 4, 5])')

# Use array_transform to square each element
result = conn.execute('SELECT array_transform(arr, x -> x * x) as squared_arr FROM numbers').fetchall()

print(result)  # Expected: [[1, 4, 9, 16, 25]]