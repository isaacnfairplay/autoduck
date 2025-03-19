# Generated: 2025-03-19 10:18:20.047018
# Result: (Decimal('0.000'),)
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

# Handle scenario of non-existent date
result = conn.execute('''
    SELECT COALESCE(
        (SELECT amount FROM sales WHERE date = '2023-01-05'), 
        0
    ) AS sales_amount
''').fetchone()

print(f'Sales for non-existent date: {result[0]}')