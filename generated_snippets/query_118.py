# Generated: 2025-03-19 16:25:00.086784
# Result: [([1, 4, 9, 16],), ([25, 36, 49, 64],)]
# Valid: True
import duckdb

# Create a connection
conn = duckdb.connect(':memory:')

# Create table with list column
conn.execute('CREATE TABLE numbers (values INTEGER[])')
conn.execute("INSERT INTO numbers VALUES ([1,2,3,4]), ([5,6,7,8])")

# Use array_transform to square each list element
result = conn.execute("SELECT array_transform(values, x -> x * x) as squared_values FROM numbers").fetchall()

print(result)