# Generated: 2025-03-19 10:15:49.237292
# Result: [(datetime.date(2023, 1, 3), Decimal('200.000'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with missing date
conn.execute('''
    CREATE TABLE sales (date DATE, amount DECIMAL);
    INSERT INTO sales VALUES
        ('2023-01-02', 150),
        ('2023-01-03', 200),
        ('2023-01-04', 180)
''');

# Handle non-existent date scenario
result = conn.execute('''
    SELECT date, amount
    FROM sales
    WHERE date = '2023-01-03'
''').fetchall()

for row in result:
    print(row)