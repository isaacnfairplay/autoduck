# Generated: 2025-03-19 16:19:52.272741
# Result: [('West', 'Electronics', Decimal('55000.00'), 3), ('South', 'Clothing', Decimal('65000.00'), 1), ('South', 'Electronics', Decimal('75000.00'), 1), ('East', 'Electronics', Decimal('60000.00'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and load data for geographic sales analysis
conn.execute('''
    CREATE TABLE sales (
        region TEXT,
        product TEXT,
        revenue DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
        ('North', 'Electronics', 50000),
        ('South', 'Electronics', 75000),
        ('East', 'Electronics', 60000),
        ('West', 'Electronics', 55000),
        ('North', 'Clothing', 40000),
        ('South', 'Clothing', 65000);
''')

# Perform multi-dimensional analysis with complex aggregation
result = conn.execute('''
    SELECT 
        region, 
        product, 
        SUM(revenue) as total_revenue,
        RANK() OVER (PARTITION BY product ORDER BY SUM(revenue) DESC) as revenue_rank
    FROM sales
    GROUP BY region, product
    HAVING SUM(revenue) > 50000
''').fetchall()

for row in result:
    print(f"Region: {row[0]}, Product: {row[1]}, Revenue: ${row[2]}, Rank: {row[3]}")