# Generated: 2025-03-19 09:43:21.193567
# Result: [('Electronics', 1, 500.0), ('Clothing', 1, 250.75), ('Books', 1, 100.5)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.sql("""
CREATE TABLE transactions (
    transaction_id INTEGER,
    product_category VARCHAR,
    amount DECIMAL(10,2),
    transaction_date DATE
);

INSERT INTO transactions VALUES
    (1, 'Electronics', 500.00, '2023-06-01'),
    (2, 'Clothing', 250.75, '2023-06-02'),
    (3, 'Books', 100.50, '2023-06-03')
""")

result = conn.sql("""
SELECT 
    product_category, 
    COUNT(*) as transaction_count,
    AVG(amount) as avg_transaction_value
FROM transactions
GROUP BY product_category
""").fetchall()

print(result)