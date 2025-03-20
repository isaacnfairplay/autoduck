# Generated: 2025-03-19 20:24:20.680904
# Result: [('Triangle', 3, Decimal('10.500'), 1), ('Square', 4, Decimal('25.000'), 2), ('Pentagon', 5, Decimal('15.750'), 3), ('Hexagon', 6, Decimal('20.250'), 4)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Creating sample data
conn.execute('CREATE TABLE numbers (value INTEGER)')
conn.execute('INSERT INTO numbers VALUES (1), (2), (3), (4), (5)')

# Using window function to calculate running total
rel = conn.sql('SELECT value, SUM(value) OVER (ORDER BY value) as running_total FROM numbers')
print(rel.execute().fetchall())