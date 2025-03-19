# Generated: 2025-03-19 16:17:15.666973
# Result: [(1, Decimal('100.50'), datetime.date(2023, 1, 15), Decimal('100.50')), (1, Decimal('250.75'), datetime.date(2023, 2, 20), Decimal('351.25')), (2, Decimal('75.25'), datetime.date(2023, 3, 10), Decimal('75.25')), (2, Decimal('125.00'), datetime.date(2023, 4, 5), Decimal('200.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Perform cross tabulation using PIVOT
conn.execute('''
    CREATE TABLE sales (
        product TEXT,
        region TEXT,
        amount DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
        ('Laptop', 'North', 1000),
        ('Laptop', 'South', 1500),
        ('Phone', 'North', 750),
        ('Phone', 'South', 900);

    SELECT * FROM sales
    PIVOT (
        SUM(amount) AS total_sales
        FOR region IN ('North', 'South')
    ) AS pivot_result;
''').fetchall()