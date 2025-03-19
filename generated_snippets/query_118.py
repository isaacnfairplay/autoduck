# Generated: 2025-03-19 11:16:58.663452
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and analyze international sales data
conn.sql('''
CREATE TABLE sales (
    region VARCHAR,
    product VARCHAR,
    revenue DECIMAL(10,2),
    sales_quarter VARCHAR
);

INSERT INTO sales VALUES
    ('Europe', 'Laptop', 500000.50, 'Q1'),
    ('North America', 'Smartphone', 750000.75, 'Q1'),
    ('Asia', 'Tablet', 350000.25, 'Q2');

-- Perform multi-dimensional rollup of global sales
SELECT 
    COALESCE(region, 'Total') AS sales_region,
    COALESCE(product, 'All Products') AS product_category,
    COALESCE(sales_quarter, 'Yearly') AS time_period,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY ROLLUP(region, product, sales_quarter)
ORDER BY total_revenue DESC;
''').show()