# Generated: 2025-03-19 18:41:03.153780
# Result: 5.0
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a custom probability function
conn.create_function('prob_calc', lambda x: x * 0.5, [duckdb.type('FLOAT')], duckdb.type('FLOAT'))

# Use the custom function in a query
result = conn.execute('SELECT prob_calc(10.0) as probability').fetchone()[0]

print(f'Probability: {result}')