# Generated: 2025-03-19 18:54:43.321071
# Result: [('East', 1, Decimal('48000.00'), Decimal('48000.00')), ('East', 2, Decimal('53000.00'), Decimal('101000.00')), ('North', 1, Decimal('50000.00'), Decimal('50000.00')), ('North', 2, Decimal('55000.00'), Decimal('105000.00')), ('South', 1, Decimal('45000.00'), Decimal('45000.00')), ('South', 2, Decimal('52000.00'), Decimal('97000.00'))]
# Valid: True
import duckdb

# Create an in-memory database and load sample sales data
conn = duckdb.connect(':memory:')

# Create a sales table with region and quarterly revenue
conn.sql("""
    CREATE TABLE sales (
        region VARCHAR,
        quarter INTEGER,
        revenue DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
        ('North', 1, 50000.00),
        ('North', 2, 55000.00),
        ('South', 1, 45000.00),
        ('South', 2, 52000.00),
        ('East', 1, 48000.00),
        ('East', 2, 53000.00);
""")

# Use window function to calculate running total by region
result = conn.sql("""
    SELECT 
        region, 
        quarter, 
        revenue,
        SUM(revenue) OVER (PARTITION BY region ORDER BY quarter) as cumulative_revenue
    FROM sales
    ORDER BY region, quarter
""").fetchall()

# Print results
for row in result:
    print(f"Region: {row[0]}, Quarter: {row[1]}, Revenue: ${row[2]}, Cumulative Revenue: ${row[3]}")