# Generated: 2025-03-19 13:57:11.363439
# Result: [(datetime.date(2023, 1, 1), 'Electronics', Decimal('5000.50'), Decimal('5000.50')), (datetime.date(2023, 1, 8), 'Electronics', Decimal('5500.75'), Decimal('10501.25')), (datetime.date(2023, 1, 15), 'Electronics', Decimal('5200.25'), Decimal('15701.50')), (datetime.date(2023, 1, 22), 'Electronics', Decimal('5800.00'), Decimal('21501.50'))]
# Valid: True
import duckdb

# Connect to memory database
conn = duckdb.connect(':memory:')

# Create time series table with weekly sales data
conn.execute('''CREATE TABLE weekly_sales (
    week_start DATE,
    product VARCHAR,
    revenue DECIMAL(10,2)
)''')

# Insert sample sales data
conn.execute('''INSERT INTO weekly_sales VALUES
    ('2023-01-01', 'Electronics', 5000.50),
    ('2023-01-08', 'Electronics', 5500.75),
    ('2023-01-15', 'Electronics', 5200.25),
    ('2023-01-22', 'Electronics', 5800.00)''')

# Calculate cumulative sales with window function
result = conn.execute('''SELECT 
    week_start, 
    product, 
    revenue,
    SUM(revenue) OVER (PARTITION BY product ORDER BY week_start) as cumulative_sales
FROM weekly_sales
''').fetchall()

print(result)