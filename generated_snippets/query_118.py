# Generated: 2025-03-19 10:12:26.655737
# Result: [(datetime.date(2023, 7, 1), 'Laptop', 10, Decimal('999.99'), Decimal('9999.90'), 'North'), (datetime.date(2023, 7, 1), 'Smartphone', 15, Decimal('599.50'), Decimal('8992.50'), 'South'), (datetime.date(2023, 7, 2), 'Laptop', 8, Decimal('999.99'), Decimal('7999.92'), 'East'), (datetime.date(2023, 7, 2), 'Tablet', 5, Decimal('399.75'), Decimal('1998.75'), 'West')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create daily sales table with comprehensive schema
conn.execute('''
    CREATE TABLE daily_sales (
        sale_date DATE,
        product_name VARCHAR,
        quantity INTEGER,
        unit_price DECIMAL(10,2),
        total_revenue DECIMAL(12,2),
        region VARCHAR
    );

    INSERT INTO daily_sales VALUES
        ('2023-07-01', 'Laptop', 10, 999.99, 9999.90, 'North'),
        ('2023-07-01', 'Smartphone', 15, 599.50, 8992.50, 'South'),
        ('2023-07-02', 'Laptop', 8, 999.99, 7999.92, 'East'),
        ('2023-07-02', 'Tablet', 5, 399.75, 1998.75, 'West')
''');

# Optional: Verify table creation
result = conn.execute('SELECT * FROM daily_sales').fetchall()
for row in result:
    print(row)