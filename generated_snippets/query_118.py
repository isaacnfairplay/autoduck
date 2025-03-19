# Generated: 2025-03-19 11:24:09.748242
# Result: [(3, 'USPS', Decimal('8.25'), Decimal('125.75'), 6.560636182902585), (1, 'FedEx', Decimal('15.50'), Decimal('250.00'), 6.2), (2, 'UPS', Decimal('22.75'), Decimal('525.50'), 4.329210275927688)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create shipping and orders tables
conn.execute('''
CREATE TABLE shipping (
    order_id INTEGER,
    carrier VARCHAR,
    shipping_cost DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id INTEGER,
    total_amount DECIMAL(10,2)
);

INSERT INTO shipping VALUES
(1, 'FedEx', 15.50),
(2, 'UPS', 22.75),
(3, 'USPS', 8.25);

INSERT INTO orders VALUES
(1, 250.00),
(2, 525.50),
(3, 125.75);
'''
)

# Calculate shipping cost percentage relative to order total
result = conn.execute('''
SELECT 
    o.order_id, 
    s.carrier, 
    s.shipping_cost, 
    o.total_amount,
    (s.shipping_cost / o.total_amount * 100) AS shipping_percentage
FROM orders o
JOIN shipping s ON o.order_id = s.order_id
ORDER BY shipping_percentage DESC
''').fetchall()

for row in result:
    print(f"Order {row[0]} via {row[1]}: ${row[2]} shipping on ${row[3]} order ({row[4]:.2f}% of total)")