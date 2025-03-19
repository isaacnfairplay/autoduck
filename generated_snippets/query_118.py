# Generated: 2025-03-19 10:16:39.339961
# Result: [(datetime.date(2023, 1, 4), Decimal('180.000'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with dates
conn.execute('''
    CREATE TABLE sales (date DATE, amount DECIMAL);
    INSERT INTO sales VALUES
        ('2023-01-02', 150),
        ('2023-01-03', 200),
        ('2023-01-04', 180)
''');

# Query sales for specific date
result = conn.execute('''
    SELECT date, amount
    FROM sales
    WHERE date = '2023-01-04'
''').fetchall()

for row in result:
    print(row)