# Generated: 2025-03-19 08:51:28.922321
# Result: [('Electronics', Decimal('1500.75'), 52.62465811066694), ('Clothing', Decimal('1351.05'), 47.37534188933305)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate category sales table
conn.execute('CREATE TABLE category_sales (category TEXT, sale_amount DECIMAL(10,2))')
conn.executemany('INSERT INTO category_sales VALUES (?, ?)', [
    ('Electronics', 1000.50),
    ('Electronics', 500.25),
    ('Clothing', 750.75),
    ('Clothing', 600.30)
])

# Calculate total sales and percentage contribution per category
result = conn.execute('''
    SELECT 
        category, 
        SUM(sale_amount) as total_sales,
        SUM(sale_amount) / (SELECT SUM(sale_amount) FROM category_sales) * 100 as sales_percentage
    FROM category_sales
    GROUP BY category
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Total Sales: ${row[1]:.2f}, Sales Percentage: {row[2]:.2f}%")