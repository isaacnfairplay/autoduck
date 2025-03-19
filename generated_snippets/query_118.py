# Generated: 2025-03-19 15:32:25.102621
# Result: [('GOOGL', datetime.date(2023, 1, 1), Decimal('100.00'), None), ('GOOGL', datetime.date(2023, 1, 2), Decimal('102.50'), Decimal('2.50')), ('AAPL', datetime.date(2023, 1, 1), Decimal('150.25'), None), ('AAPL', datetime.date(2023, 1, 2), Decimal('152.50'), Decimal('2.25')), ('AAPL', datetime.date(2023, 1, 3), Decimal('149.75'), Decimal('-2.75'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create time series data for stock prices
conn.execute('''
    CREATE TABLE stock_prices (
        date DATE,
        symbol TEXT,
        price DECIMAL(10,2)
    );

    INSERT INTO stock_prices VALUES
        ('2023-01-01', 'AAPL', 150.25),
        ('2023-01-02', 'AAPL', 152.50),
        ('2023-01-03', 'AAPL', 149.75),
        ('2023-01-01', 'GOOGL', 100.00),
        ('2023-01-02', 'GOOGL', 102.50);
''')

# Calculate price changes using window functions
result = conn.execute('''
    SELECT 
        symbol, 
        date, 
        price,
        price - LAG(price) OVER (PARTITION BY symbol ORDER BY date) as price_change
    FROM stock_prices
''').fetchall()

for row in result:
    print(f'Symbol: {row[0]}, Date: {row[1]}, Price: ${row[2]}, Price Change: ${row[3] or 0}')