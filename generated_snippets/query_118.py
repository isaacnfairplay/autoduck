# Generated: 2025-03-19 14:20:56.108400
# Result: [('Tablet', 'Electronics', Decimal('500.00'), Decimal('500.00')), ('Phone', 'Electronics', Decimal('800.00'), Decimal('1300.00')), ('Laptop', 'Electronics', Decimal('1200.00'), Decimal('2500.00')), ('Book', 'Literature', Decimal('50.00'), Decimal('50.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with product sales and calculate cumulative sales by category
conn.execute('CREATE TABLE sales (product STRING, category STRING, sale_amount DECIMAL(10,2))')
conn.execute("INSERT INTO sales VALUES ('Laptop', 'Electronics', 1200), ('Phone', 'Electronics', 800), ('Book', 'Literature', 50), ('Tablet', 'Electronics', 500)")

result = conn.execute('''
    SELECT 
        product, 
        category, 
        sale_amount, 
        SUM(sale_amount) OVER (PARTITION BY category ORDER BY sale_amount) as cumulative_category_sales
    FROM sales
''').fetchall()

for row in result:
    print(row)