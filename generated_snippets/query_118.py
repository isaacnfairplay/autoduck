# Generated: 2025-03-19 19:21:15.223075
# Result: [('Real Estate', Decimal('10000.00'), Decimal('10512.00')), ('Bond B', Decimal('5000.00'), Decimal('5172.50')), ('Stock A', Decimal('1000.00'), Decimal('1072.50'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with decimal precision and perform precise financial calculation
conn.execute('''CREATE TABLE investments (
    asset_name VARCHAR,
    investment_amount DECIMAL(10,2),
    growth_rate DECIMAL(5,4)
)''')

conn.execute('''INSERT INTO investments VALUES
    ('Stock A', 1000.00, 0.0725),
    ('Bond B', 5000.00, 0.0345),
    ('Real Estate', 10000.00, 0.0512)''')

# Calculate precise investment growth with high decimal precision
result = conn.execute('''SELECT 
    asset_name, 
    investment_amount, 
    ROUND(investment_amount * (1 + growth_rate), 2) as projected_value
FROM investments
ORDER BY projected_value DESC''').fetchall()

for row in result:
    print(f"{row[0]}: ${row[1]} -> ${row[2]}")