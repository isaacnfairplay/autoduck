# Generated: 2025-03-19 11:00:21.304230
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create time series data for stock price analysis
conn.execute('''
    CREATE TABLE stock_prices (
        stock_symbol TEXT,
        trading_date DATE,
        closing_price DECIMAL(10,2)
    );

    INSERT INTO stock_prices VALUES
        ('AAPL', '2023-01-01', 145.50),
        ('AAPL', '2023-01-02', 146.75),
        ('AAPL', '2023-01-03', 144.25);

    SELECT 
        stock_symbol,
        trading_date,
        closing_price,
        AVG(closing_price) OVER (PARTITION BY stock_symbol ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg
    FROM stock_prices
''').fetchall()