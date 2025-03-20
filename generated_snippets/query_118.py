# Generated: 2025-03-19 21:42:44.391066
# Result: [('AAPL', datetime.date(2023, 1, 15), Decimal('150.25'), 150.25), ('AAPL', datetime.date(2023, 1, 16), Decimal('155.75'), 153.0), ('AAPL', datetime.date(2023, 1, 17), Decimal('152.50'), 154.125)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create temporal data with time series analysis
conn.execute("""CREATE TABLE stock_prices (
    symbol VARCHAR,
    price DECIMAL(10,2),
    trading_date DATE
)""")

conn.execute("""INSERT INTO stock_prices VALUES
    ('AAPL', 150.25, '2023-01-15'),
    ('AAPL', 155.75, '2023-01-16'),
    ('AAPL', 152.50, '2023-01-17')
""")

# Compute moving average with window function
result = conn.execute("""
SELECT 
    symbol, 
    trading_date, 
    price,
    AVG(price) OVER (PARTITION BY symbol ORDER BY trading_date ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg
FROM stock_prices
""").fetchall()

for row in result:
    print(f"Date: {row[1]}, Price: {row[2]}, Moving Avg: {row[3]}")