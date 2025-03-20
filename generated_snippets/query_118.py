# Generated: 2025-03-19 20:31:23.919064
# Result: [(datetime.date(2023, 1, 3), 'GOOG', Decimal('90.75'), None), (datetime.date(2023, 1, 1), 'AAPL', Decimal('145.50'), None), (datetime.date(2023, 1, 2), 'AAPL', Decimal('147.25'), Decimal('1.75'))]
# Valid: True
import duckdb

# Create an in-memory connection
conn = duckdb.connect(':memory:')

# Create a sample time series table
conn.execute('''
    CREATE TABLE stock_prices (
        date DATE,
        symbol VARCHAR,
        price DECIMAL(10,2),
        volume INTEGER
    );
''')

# Insert sample stock price data
conn.executemany('INSERT INTO stock_prices VALUES (?, ?, ?, ?)', [
    ('2023-01-01', 'AAPL', 145.50, 1000000),
    ('2023-01-02', 'AAPL', 147.25, 1200000),
    ('2023-01-03', 'GOOG', 90.75, 800000)
])

# Use window function to calculate price change
result = conn.execute('''
    SELECT 
        date, 
        symbol, 
        price,
        price - LAG(price) OVER (PARTITION BY symbol ORDER BY date) as price_change
    FROM stock_prices
''').fetchall()

print(result)