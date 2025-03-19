# Generated: 2025-03-19 14:54:24.555295
# Result: [('Electronics', Decimal('6000.000'), 1, 1), ('Electronics', Decimal('5500.000'), 2, 2), ('Electronics', Decimal('5000.000'), 3, 3), ('Clothing', Decimal('4000.000'), 1, 1), ('Clothing', Decimal('3500.000'), 2, 2), ('Clothing', Decimal('3000.000'), 3, 3)]
# Valid: True
import duckdb

# Demonstrate window functions with rank and dense_rank
conn = duckdb.connect(':memory:')

# Create sample sales data
conn.execute('''
    CREATE TABLE sales (department STRING, sales_amount DECIMAL);
    INSERT INTO sales VALUES
        ('Electronics', 5000), ('Clothing', 3000), 
        ('Electronics', 6000), ('Clothing', 4000),
        ('Electronics', 5500), ('Clothing', 3500);
''')

# Rank sales within each department
result = conn.execute('''
    SELECT 
        department, 
        sales_amount, 
        RANK() OVER (PARTITION BY department ORDER BY sales_amount DESC) as sales_rank,
        DENSE_RANK() OVER (PARTITION BY department ORDER BY sales_amount DESC) as dense_sales_rank
    FROM sales
''').fetchall()

print(result)