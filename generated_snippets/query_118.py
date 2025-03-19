# Generated: 2025-03-19 16:26:52.357585
# Result: [(datetime.date(2023, 1, 1), 'GOOGL', Decimal('100.50'), 100.5), (datetime.date(2023, 1, 2), 'GOOGL', Decimal('102.25'), 101.375), (datetime.date(2023, 1, 1), 'AAPL', Decimal('150.25'), 150.25), (datetime.date(2023, 1, 2), 'AAPL', Decimal('152.50'), 151.375), (datetime.date(2023, 1, 3), 'AAPL', Decimal('149.75'), 151.125)]
# Valid: True
import duckdb

# Create an in-memory connection
conn = duckdb.connect(':memory:')

# Create a table with time series data
conn.execute('''
CREATE TABLE stock_prices (
    date DATE,
    symbol VARCHAR,
    price DECIMAL(10,2),
    volume INTEGER
);

INSERT INTO stock_prices VALUES
    ('2023-01-01', 'AAPL', 150.25, 1000000),
    ('2023-01-02', 'AAPL', 152.50, 1200000),
    ('2023-01-03', 'AAPL', 149.75, 900000),
    ('2023-01-01', 'GOOGL', 100.50, 500000),
    ('2023-01-02', 'GOOGL', 102.25, 550000);
'''
)

# Calculate 2-day moving average of stock prices
result = conn.execute('''
SELECT 
    date, 
    symbol, 
    price,
    AVG(price) OVER (PARTITION BY symbol ORDER BY date ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg
FROM stock_prices
''').fetchall()

for row in result:
    print(row)