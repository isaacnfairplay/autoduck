# Generated: 2025-03-19 20:51:11.423280
# Result: [('Widget', 'South', Decimal('1250.75'), 1), ('Gadget', 'South', Decimal('750.25'), 2), ('Widget', 'North', Decimal('1000.50'), 1), ('Gadget', 'North', Decimal('850.60'), 2)]
# Valid: True
import duckdb

# Create an in-memory connection
conn = duckdb.connect(':memory:')

# Create sample table with sales data
conn.execute('''
    CREATE TABLE sales (
        product TEXT,
        region TEXT,
        amount DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
        ('Widget', 'North', 1000.50),
        ('Gadget', 'South', 750.25),
        ('Widget', 'South', 1250.75),
        ('Gadget', 'North', 850.60);
''')

# Perform window ranking of sales by region
result = conn.execute('''
    SELECT 
        product, 
        region, 
        amount,
        RANK() OVER (PARTITION BY region ORDER BY amount DESC) as regional_rank
    FROM sales
''').fetchall()

print(result)