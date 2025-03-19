# Generated: 2025-03-19 11:28:30.043811
# Result: [('Laptop', Decimal('97000.25'), 48500.125), ('Smartphone', Decimal('65001.25'), 32500.625)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create monthly sales data
conn.execute('''
CREATE TABLE monthly_sales (
    month VARCHAR,
    product VARCHAR,
    revenue DECIMAL(10,2)
);

INSERT INTO monthly_sales VALUES
('January', 'Laptop', 45000.00),
('January', 'Smartphone', 30000.50),
('February', 'Laptop', 52000.25),
('February', 'Smartphone', 35000.75);
'''
)

# Calculate total revenue per product
result = conn.execute('''
SELECT 
    product, 
    SUM(revenue) as total_revenue,
    AVG(revenue) as avg_monthly_revenue
FROM monthly_sales
GROUP BY product
ORDER BY total_revenue DESC
''').fetchall()

for row in result:
    print(f"{row[0]}: Total Revenue ${row[1]}, Avg Monthly ${row[2]:.2f}")