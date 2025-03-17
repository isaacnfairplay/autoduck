# Generated: 2025-03-16 22:47:26.716545
# Result: [('Junior Engineer', 0), ('Senior Engineer', 1), ('CTO', 2), ('CEO', 3)]
# Valid: True
# Variable transformed_data: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

con = duckdb.connect(':memory:')

# Create source data
con.execute('''
    CREATE TABLE raw_transactions (
        transaction_id INT,
        amount DECIMAL(10,2),
        category VARCHAR,
        timestamp TIMESTAMP
    );

    INSERT INTO raw_transactions VALUES
    (1, 100.50, 'Groceries', '2023-01-15 10:30:00'),
    (2, 250.75, 'Electronics', '2023-02-20 14:45:00'),
    (3, 50.25, 'Groceries', '2023-03-10 09:15:00');
''')

# Data transformation query
transformed_data = con.execute('''
    SELECT 
        transaction_id,
        amount,
        category,
        DATE_TRUNC('month', timestamp) as month,
        CASE 
            WHEN amount < 100 THEN 'Low'
            WHEN amount BETWEEN 100 AND 200 THEN 'Medium'
            ELSE 'High'
        END as spend_category
    FROM raw_transactions
''').fetchall()

for row in transformed_data:
    print(f'Transaction: {row[0]}, Amount: ${row[1]}, Category: {row[2]}, Month: {row[3]}, Spend Level: {row[4]}')