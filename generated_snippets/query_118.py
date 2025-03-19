# Generated: 2025-03-19 16:41:50.880886
# Result: [(1, 10.5), (2, 20.100000381469727)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample table
conn.execute('''CREATE TABLE measurements (
    group_id INTEGER,
    value FLOAT
)''')

# Insert sample data
conn.executemany('INSERT INTO measurements VALUES (?, ?)', [
    (1, 10.5), (1, 15.2), (1, 8.7),
    (2, 20.1), (2, 22.3), (2, 18.9)
])

# Custom aggregation using percentile_cont
result = conn.execute('''SELECT 
    group_id, 
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY value) as median_value
FROM measurements
GROUP BY group_id
''').fetchall()

print(result)