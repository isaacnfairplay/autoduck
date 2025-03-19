# Generated: 2025-03-19 19:22:08.531330
# Result: [('AAPL', datetime.date(2023, 1, 1), Decimal('145.50'), 145.5), ('AAPL', datetime.date(2023, 1, 2), Decimal('146.75'), 146.125), ('AAPL', datetime.date(2023, 1, 3), Decimal('144.25'), 145.5), ('GOOG', datetime.date(2023, 1, 1), Decimal('90.10'), 90.1), ('GOOG', datetime.date(2023, 1, 2), Decimal('91.45'), 90.775), ('GOOG', datetime.date(2023, 1, 3), Decimal('89.90'), 90.675)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create time series data with window function
conn.execute('''CREATE TABLE stock_prices (
    symbol VARCHAR,
    trade_date DATE,
    closing_price DECIMAL(10,2)
)''')

conn.execute('''INSERT INTO stock_prices VALUES
    ('AAPL', '2023-01-01', 145.50),
    ('AAPL', '2023-01-02', 146.75),
    ('AAPL', '2023-01-03', 144.25),
    ('GOOG', '2023-01-01', 90.10),
    ('GOOG', '2023-01-02', 91.45),
    ('GOOG', '2023-01-03', 89.90)''')

# Calculate rolling 2-day moving average for each stock
result = conn.execute('''SELECT 
    symbol, 
    trade_date, 
    closing_price,
    AVG(closing_price) OVER (
        PARTITION BY symbol 
        ORDER BY trade_date 
        ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
    ) as moving_avg
FROM stock_prices
ORDER BY symbol, trade_date''').fetchall()

for row in result:
    print(f'{row[0]} on {row[1]}: Price={row[2]}, Moving Avg={row[3]}')