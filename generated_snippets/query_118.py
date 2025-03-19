# Generated: 2025-03-19 08:39:24.843271
# Result: [('GOOGL', datetime.date(2023, 1, 1), Decimal('90.50'), 90.5), ('GOOGL', datetime.date(2023, 1, 2), Decimal('92.10'), 91.3), ('GOOGL', datetime.date(2023, 1, 3), Decimal('91.80'), 91.46666666666667), ('AAPL', datetime.date(2023, 1, 1), Decimal('150.25'), 150.25), ('AAPL', datetime.date(2023, 1, 2), Decimal('152.40'), 151.325), ('AAPL', datetime.date(2023, 1, 3), Decimal('149.75'), 150.8)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate time series data
conn.execute('CREATE TABLE stock_prices (symbol TEXT, date DATE, price DECIMAL(10,2))')
conn.executemany('INSERT INTO stock_prices VALUES (?, ?, ?)', [
    ('AAPL', '2023-01-01', 150.25),
    ('AAPL', '2023-01-02', 152.40),
    ('AAPL', '2023-01-03', 149.75),
    ('GOOGL', '2023-01-01', 90.50),
    ('GOOGL', '2023-01-02', 92.10),
    ('GOOGL', '2023-01-03', 91.80)
])

# Calculate moving average using window function
result = conn.execute('''
    SELECT 
        symbol, 
        date, 
        price,
        AVG(price) OVER (PARTITION BY symbol ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg
    FROM stock_prices
''').fetchall()

for row in result:
    print(f"Symbol: {row[0]}, Date: {row[1]}, Price: {row[2]}, Moving Avg: {row[3]:.2f}")