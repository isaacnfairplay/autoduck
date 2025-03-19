# Generated: 2025-03-19 13:46:48.100494
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

# Create connection and memory table with numeric list
conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE numbers (values_list INTEGER[])')
conn.execute('INSERT INTO numbers VALUES ([1, 2, 3, 4, 5])')

# Transform array by squaring each element
result = conn.execute('SELECT array_transform(values_list, x -> x * x) as squared_values FROM numbers').fetchall()
print(result)