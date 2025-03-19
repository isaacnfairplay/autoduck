# Generated: 2025-03-19 12:32:56.870576
# Result: [('GOOGL', datetime.date(2023, 6, 1), Decimal('120.25'), None), ('GOOGL', datetime.date(2023, 6, 2), Decimal('122.40'), Decimal('2.15')), ('AAPL', datetime.date(2023, 6, 1), Decimal('180.50'), None), ('AAPL', datetime.date(2023, 6, 2), Decimal('182.75'), Decimal('2.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate a time series stock price table
conn.execute('''CREATE TABLE stock_prices (
    symbol VARCHAR,
    trade_date DATE,
    closing_price DECIMAL(10,2)
);''')

conn.execute('''INSERT INTO stock_prices VALUES
    ('AAPL', '2023-06-01', 180.50),
    ('AAPL', '2023-06-02', 182.75),
    ('GOOGL', '2023-06-01', 120.25),
    ('GOOGL', '2023-06-02', 122.40)
''')

# Calculate daily price change using window functions
result = conn.execute('''SELECT
    symbol,
    trade_date,
    closing_price,
    closing_price - LAG(closing_price, 1) OVER (PARTITION BY symbol ORDER BY trade_date) as price_change
FROM stock_prices
''').fetchall()

for row in result:
    print(row)