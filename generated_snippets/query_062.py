# Generated: 2025-03-16 22:47:50.550459
# Result: None
# Valid: True
import duckdb

# Performance-optimized analytical query with indexing
con = duckdb.connect(':memory:')

# Create large transaction table
con.execute('''
    CREATE TABLE large_transactions (
        transaction_id BIGINT,
        amount DECIMAL(15,2),
        category VARCHAR,
        timestamp TIMESTAMP
    );

    -- Create index for faster filtering
    CREATE INDEX category_idx ON large_transactions(category);
''')

# Complex analytical query demonstrating performance optimization
result = con.execute('''
    SELECT 
        category, 
        COUNT(*) as transaction_count,
        SUM(amount) as total_amount,
        AVG(amount) as avg_transaction
    FROM large_transactions
    WHERE timestamp BETWEEN '2023-01-01' AND '2023-12-31'
    GROUP BY category
    ORDER BY total_amount DESC
    LIMIT 5
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Transactions: {row[1]}, Total: ${row[2]}, Avg: ${row[3]:.2f}")