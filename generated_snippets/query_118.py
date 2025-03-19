# Generated: 2025-03-19 10:14:08.437155
# Result: [(datetime.date(2023, 1, 1), Decimal('100.000'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with single date column
conn.execute('''
    CREATE TABLE sales (date DATE, amount DECIMAL);
    INSERT INTO sales VALUES
        ('2023-01-01', 100),
        ('2023-01-02', 150),
        ('2023-01-03', 200)
''')

# Calculate total sales for January 1st
result = conn.execute('''
    SELECT date, SUM(amount) as total_sales
    FROM sales
    WHERE date = '2023-01-01'
    GROUP BY date
''').fetchall()

for row in result:
    print(row)