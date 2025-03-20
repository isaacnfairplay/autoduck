# Generated: 2025-03-19 20:17:34.639103
# Result: [(datetime.date(2023, 1, 15), 'Widget', Decimal('500.000'), 500.0), (datetime.date(2023, 1, 17), 'Widget', Decimal('625.250'), 562.625), (datetime.date(2023, 1, 16), 'Gadget', Decimal('750.500'), 750.5), (datetime.date(2023, 1, 18), 'Gadget', Decimal('480.750'), 615.625)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and query a temporal table with time-based window function
conn.execute('''CREATE TABLE sales (
    sale_date DATE,
    product VARCHAR,
    amount DECIMAL
)''')

conn.execute('''INSERT INTO sales VALUES
    ('2023-01-15', 'Widget', 500.00),
    ('2023-01-16', 'Gadget', 750.50),
    ('2023-01-17', 'Widget', 625.25),
    ('2023-01-18', 'Gadget', 480.75)''')

# Calculate 3-day moving average of sales
result = conn.execute('''
    SELECT 
        sale_date, 
        product, 
        amount,
        AVG(amount) OVER (PARTITION BY product ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg
    FROM sales
''').fetchall()

for row in result:
    print(f"Date: {row[0]}, Product: {row[1]}, Amount: ${row[2]}, Moving Avg: ${row[3]:.2f}")