# Generated: 2025-03-19 09:33:03.260841
# Result: [('GOOGL', datetime.date(2023, 1, 1), Decimal('100.25'), 100.25, Decimal('0.00')), ('GOOGL', datetime.date(2023, 1, 2), Decimal('102.50'), 101.375, Decimal('2.25')), ('GOOGL', datetime.date(2023, 1, 3), Decimal('101.75'), 102.125, Decimal('1.50')), ('AAPL', datetime.date(2023, 1, 1), Decimal('150.50'), 150.5, Decimal('0.00')), ('AAPL', datetime.date(2023, 1, 2), Decimal('152.25'), 151.375, Decimal('1.75')), ('AAPL', datetime.date(2023, 1, 3), Decimal('149.75'), 151.0, Decimal('-0.75'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create time series data with complex window function
conn.sql("""
CREATE TABLE stock_prices (
    date DATE,
    stock VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO stock_prices VALUES
    ('2023-01-01', 'AAPL', 150.50),
    ('2023-01-02', 'AAPL', 152.25),
    ('2023-01-03', 'AAPL', 149.75),
    ('2023-01-01', 'GOOGL', 100.25),
    ('2023-01-02', 'GOOGL', 102.50),
    ('2023-01-03', 'GOOGL', 101.75)
""")

# Calculate rolling 2-day average and total price change
result = conn.sql("""
SELECT 
    stock, 
    date, 
    price,
    AVG(price) OVER (PARTITION BY stock ORDER BY date ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg,
    price - FIRST_VALUE(price) OVER (PARTITION BY stock ORDER BY date) as price_change
FROM stock_prices
""").fetchall()

print(result)