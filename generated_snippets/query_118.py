# Generated: 2025-03-19 12:56:20.936161
# Result: [(1, 'Laptop', 2), (2, 'Monitor', 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create JSON-like nested data example
conn.execute('''
CREATE TABLE customer_orders (
    customer_id INT,
    orders STRUCT(product VARCHAR, quantity INT, price DECIMAL(10,2))[]
);

INSERT INTO customer_orders VALUES
    (1, [{'product': 'Laptop', 'quantity': 1, 'price': 1200.50}, {'product': 'Mouse', 'quantity': 2, 'price': 50.00}]),
    (2, [{'product': 'Monitor', 'quantity': 1, 'price': 300.75}]);
'''
)

# Query nested array data
result = conn.execute('''
SELECT 
    customer_id, 
    orders[1].product as first_product,
    ARRAY_LENGTH(orders) as total_orders
FROM customer_orders
''').fetchall()

for row in result:
    print(row)