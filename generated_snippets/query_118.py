# Generated: 2025-03-19 10:14:58.590553
# Result: [(datetime.date(2023, 1, 2), Decimal('150.000'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate sample sales table
conn.execute('''
    CREATE TABLE sales (date DATE, amount DECIMAL);
    INSERT INTO sales VALUES
        ('2023-01-02', 150),
        ('2023-01-03', 200),
        ('2023-01-04', 180)
''')

# Query specific date's sales
result = conn.execute('''
    SELECT date, amount
    FROM sales
    WHERE date = '2023-01-02'
''').fetchall()

for row in result:
    print(row)