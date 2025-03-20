# Generated: 2025-03-19 21:20:55.852224
# Result: [('GOOGL', Decimal('100.750'), datetime.date(2024, 1, 1), None, Decimal('102.300')), ('GOOGL', Decimal('102.300'), datetime.date(2024, 1, 2), Decimal('100.750'), None), ('AAPL', Decimal('150.250'), datetime.date(2024, 1, 1), None, Decimal('152.500')), ('AAPL', Decimal('152.500'), datetime.date(2024, 1, 2), Decimal('150.250'), None)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate a time series table
conn.execute('CREATE TABLE stock_prices (symbol VARCHAR, price DECIMAL, trade_date DATE)')
conn.execute("""INSERT INTO stock_prices VALUES
    ('AAPL', 150.25, '2024-01-01'),
    ('AAPL', 152.50, '2024-01-02'),
    ('GOOGL', 100.75, '2024-01-01'),
    ('GOOGL', 102.30, '2024-01-02')
""")

# Demonstrate time series window function with lead/lag
result = conn.execute("""SELECT
    symbol, 
    price,
    trade_date,
    LAG(price) OVER (PARTITION BY symbol ORDER BY trade_date) as previous_price,
    LEAD(price) OVER (PARTITION BY symbol ORDER BY trade_date) as next_price
    FROM stock_prices""").fetchall()

print(result)