# Generated: 2025-03-19 15:26:27.167030
# Result: [('Laptop', 'Electronics', Decimal('1200.50'), 1), ('Tablet', 'Electronics', Decimal('950.75'), 2), ('Phone', 'Electronics', Decimal('800.25'), 3), ('Book', 'Literature', Decimal('25.00'), 1), ('Magazine', 'Literature', Decimal('15.50'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample product sales data
conn.execute('''
    CREATE TABLE product_sales (
        product TEXT,
        category TEXT,
        sales DECIMAL(10,2)
    );

    INSERT INTO product_sales VALUES
        ('Laptop', 'Electronics', 1200.50),
        ('Phone', 'Electronics', 800.25),
        ('Tablet', 'Electronics', 950.75),
        ('Book', 'Literature', 25.00),
        ('Magazine', 'Literature', 15.50)
''');

# Calculate sales rank within each category
result = conn.execute('''
    SELECT 
        product, 
        category, 
        sales,
        RANK() OVER (PARTITION BY category ORDER BY sales DESC) as sales_rank
    FROM product_sales
''').fetchall()

for row in result:
    print(f'Product: {row[0]}, Category: {row[1]}, Sales: ${row[2]}, Rank: {row[3]}')