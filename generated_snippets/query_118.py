# Generated: 2025-03-19 10:24:26.059963
# Result: [(datetime.date(2023, 7, 1), Decimal('150.500')), (datetime.date(2023, 7, 2), Decimal('200.750'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate sales table
conn.execute('''
    CREATE TABLE sales (sale_date DATE, amount DECIMAL);
    INSERT INTO sales VALUES
        ('2023-07-01', 150.50),
        ('2023-07-02', 200.75),
        ('2023-07-03', 180.25)
''');

# Retrieve sales amounts between two dates
result = conn.execute('''
    SELECT sale_date, amount
    FROM sales
    WHERE sale_date BETWEEN '2023-07-01' AND '2023-07-02'
    ORDER BY sale_date
''').fetchall()

for row in result:
    print(row)