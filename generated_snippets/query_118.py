# Generated: 2025-03-19 10:19:11.669850
# Result: [(datetime.date(2023, 1, 2), Decimal('150.000')), (datetime.date(2023, 1, 3), Decimal('200.000'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate sales table with single date column
conn.execute('''
    CREATE TABLE sales (date DATE, amount DECIMAL);
    INSERT INTO sales VALUES
        ('2023-01-01', 100),
        ('2023-01-02', 150),
        ('2023-01-03', 200)
''')

# Demonstrate simple date-based filtering and aggregation
result = conn.execute('''
    SELECT date, SUM(amount) as total_sales
    FROM sales
    WHERE date >= '2023-01-02'
    GROUP BY date
''').fetchall()

for row in result:
    print(row)