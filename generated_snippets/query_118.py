# Generated: 2025-03-19 21:05:15.887380
# Result: [(1, 'Alice', 'alice@example.com'), (2, 'Bob', 'bob@example.com')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample table with nested JSON data
conn.sql("""
CREATE TABLE nested_orders (
    order_id INTEGER,
    customer_details JSON
);

INSERT INTO nested_orders VALUES
    (1, '{ "name": "Alice", "contact": { "email": "alice@example.com", "phone": "555-1234" } }'),
    (2, '{ "name": "Bob", "contact": { "email": "bob@example.com", "phone": "555-5678" } }');
""")

# Extract nested JSON fields using JSON path
result = conn.sql("""
SELECT 
    order_id, 
    customer_details->>'name' AS customer_name,
    customer_details->>'contact'->>'email' AS customer_email
FROM nested_orders
""").fetchall()

print(result)