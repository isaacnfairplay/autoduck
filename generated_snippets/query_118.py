# Generated: 2025-03-19 10:54:53.060179
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
    CREATE TABLE product_inventory (
        product_id INT,
        warehouse TEXT,
        stock_quantity INT,
        restock_date DATE
    );

    INSERT INTO product_inventory VALUES
        (1, 'A', 100, '2023-01-15'),
        (1, 'B', 50, '2023-02-20'),
        (2, 'A', 75, '2023-01-10'),
        (2, 'B', 125, '2023-03-05');

    SELECT 
        product_id, 
        warehouse,
        stock_quantity,
        FIRST_VALUE(stock_quantity) OVER (PARTITION BY product_id ORDER BY restock_date) as initial_stock,
        LAST_VALUE(stock_quantity) OVER (PARTITION BY product_id ORDER BY restock_date
            RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as final_stock,
        stock_quantity - FIRST_VALUE(stock_quantity) OVER (PARTITION BY product_id ORDER BY restock_date) as stock_change
    FROM product_inventory
''').fetchall()