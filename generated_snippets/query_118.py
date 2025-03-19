# Generated: 2025-03-19 08:54:53.826885
# Result: [('Electronics', Decimal('2000.75'), 97.52620034121374), ('Literature', Decimal('50.75'), 2.4737996587862536)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate table for calculating sales percentages
conn.execute('CREATE TABLE sales (product TEXT, category TEXT, amount DECIMAL(10,2))')
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('Laptop', 'Electronics', 1200.50),
    ('Phone', 'Electronics', 800.25),
    ('Book', 'Literature', 50.75)
])

# Calculate total sales and percentage contribution per category
result = conn.execute('''
    SELECT 
        category, 
        SUM(amount) as total_sales,
        SUM(amount) / (SELECT SUM(amount) FROM sales) * 100 as sales_percentage
    FROM sales
    GROUP BY category
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Total Sales: ${row[1]:.2f}, Sales Percentage: {row[2]:.2f}%")