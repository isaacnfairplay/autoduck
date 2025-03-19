# Generated: 2025-03-19 15:24:43.357244
# Result: [('Headphones', 'Electronics', Decimal('150.75'), Decimal('150.75')), ('Phone', 'Electronics', Decimal('800.25'), Decimal('951.00')), ('Laptop', 'Electronics', Decimal('1200.50'), Decimal('2151.50')), ('Book', 'Literature', Decimal('25.00'), Decimal('25.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with sample sales data
conn.execute('''
    CREATE TABLE sales (
        product TEXT,
        category TEXT,
        revenue DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
        ('Laptop', 'Electronics', 1200.50),
        ('Phone', 'Electronics', 800.25),
        ('Headphones', 'Electronics', 150.75),
        ('Book', 'Literature', 25.00);
''')

# Window function to calculate running total of revenue by category
result = conn.execute('''
    SELECT 
        product, 
        category, 
        revenue,
        SUM(revenue) OVER (PARTITION BY category ORDER BY revenue) as running_total
    FROM sales
''').fetchall()

for row in result:
    print(f'{row[0]} - Category: {row[1]}, Revenue: ${row[2]}, Running Total: ${row[3]}')