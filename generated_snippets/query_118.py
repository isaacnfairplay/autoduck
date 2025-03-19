# Generated: 2025-03-19 10:25:19.901779
# Result: [(datetime.date(2023, 7, 1), Decimal('150.500'), 150.5), (datetime.date(2023, 7, 2), Decimal('200.750'), 175.625), (datetime.date(2023, 7, 3), Decimal('180.250'), 177.16666666666666), (datetime.date(2023, 7, 4), Decimal('220.000'), 200.33333333333334), (datetime.date(2023, 7, 5), Decimal('190.500'), 196.91666666666666)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
    CREATE TABLE sales (sale_date DATE, amount DECIMAL);
    INSERT INTO sales VALUES
        ('2023-07-01', 150.50),
        ('2023-07-02', 200.75),
        ('2023-07-03', 180.25),
        ('2023-07-04', 220.00),
        ('2023-07-05', 190.50)
''');

result = conn.execute('''
    SELECT 
        sale_date, 
        amount,
        AVG(amount) OVER (ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as rolling_avg
    FROM sales
''').fetchall()

for row in result:
    print(row)