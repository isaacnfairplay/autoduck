# Generated: 2025-03-19 21:08:49.290724
# Result: [(datetime.date(2023, 1, 1), Decimal('100.00'), 100.0), (datetime.date(2023, 1, 2), Decimal('102.50'), 101.25), (datetime.date(2023, 1, 3), Decimal('101.75'), 101.41666666666667), (datetime.date(2023, 1, 4), Decimal('103.25'), 102.5), (datetime.date(2023, 1, 5), Decimal('105.00'), 103.33333333333333)]
# Valid: True
import duckdb

# Temporal window function with moving average
conn = duckdb.connect(':memory:')

conn.sql("""
CREATE TABLE stock_prices (
    date DATE,
    price DECIMAL(10,2)
);

INSERT INTO stock_prices VALUES
    ('2023-01-01', 100.00),
    ('2023-01-02', 102.50),
    ('2023-01-03', 101.75),
    ('2023-01-04', 103.25),
    ('2023-01-05', 105.00);
""")

result = conn.sql("""
SELECT 
    date, 
    price,
    AVG(price) OVER (ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg
FROM stock_prices
""").fetchall()

print(result)