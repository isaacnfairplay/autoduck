# Generated: 2025-03-19 11:03:09.249648
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Creating sales tracking with quarterly window function analysis
conn.execute('''
CREATE TABLE sales (
    product_id INTEGER,
    quarter VARCHAR,
    total_revenue DECIMAL(10,2)
);

INSERT INTO sales VALUES
    (1, 'Q1', 1000.00),
    (1, 'Q2', 1200.00),
    (1, 'Q3', 1500.00),
    (1, 'Q4', 1800.00);

-- Calculate cumulative and percent change across quarters
SELECT 
    product_id, 
    quarter, 
    total_revenue,
    SUM(total_revenue) OVER (PARTITION BY product_id ORDER BY quarter) as cumulative_revenue,
    (total_revenue - LAG(total_revenue) OVER (PARTITION BY product_id ORDER BY quarter)) / 
        LAG(total_revenue) OVER (PARTITION BY product_id ORDER BY quarter) * 100 as revenue_percent_change
FROM sales
''').fetchall()