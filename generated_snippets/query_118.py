# Generated: 2025-03-19 17:32:34.418365
# Result: [(datetime.date(2023, 1, 1), 'AAPL', Decimal('150.50'), None, Decimal('152.25'), None), (datetime.date(2023, 1, 2), 'AAPL', Decimal('152.25'), Decimal('150.50'), Decimal('149.75'), Decimal('1.75')), (datetime.date(2023, 1, 3), 'AAPL', Decimal('149.75'), Decimal('152.25'), Decimal('153.00'), Decimal('-2.50')), (datetime.date(2023, 1, 4), 'AAPL', Decimal('153.00'), Decimal('149.75'), None, Decimal('3.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and analyze time series data with lead/lag functions
conn.execute('''
CREATE TABLE stock_prices (
    date DATE,
    stock TEXT,
    price DECIMAL(10,2)
);

INSERT INTO stock_prices VALUES
    ('2023-01-01', 'AAPL', 150.50),
    ('2023-01-02', 'AAPL', 152.25),
    ('2023-01-03', 'AAPL', 149.75),
    ('2023-01-04', 'AAPL', 153.00);

SELECT 
    date, 
    stock, 
    price,
    LAG(price) OVER (PARTITION BY stock ORDER BY date) as previous_price,
    LEAD(price) OVER (PARTITION BY stock ORDER BY date) as next_price,
    price - LAG(price) OVER (PARTITION BY stock ORDER BY date) as price_change
FROM stock_prices
''')

result = conn.fetchall()
for row in result:
    print(row)