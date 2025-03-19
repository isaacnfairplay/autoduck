# Generated: 2025-03-19 14:06:05.094856
# Result: [('London', datetime.date(2023, 6, 1), Decimal('22.10'), 22.75), ('London', datetime.date(2023, 6, 2), Decimal('23.40'), 22.466666666666665), ('London', datetime.date(2023, 6, 3), Decimal('21.90'), 22.65), ('New York', datetime.date(2023, 6, 1), Decimal('28.50'), 29.35), ('New York', datetime.date(2023, 6, 2), Decimal('30.20'), 29.466666666666665), ('New York', datetime.date(2023, 6, 3), Decimal('29.70'), 29.95)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table
conn.execute('CREATE TABLE numbers (value INTEGER)')
conn.execute('INSERT INTO numbers VALUES (1), (2), (3), (4), (5)')

# Create a relation and execute
rel = conn.table('numbers').filter('value > 2')
print(rel.execute().fetchall())