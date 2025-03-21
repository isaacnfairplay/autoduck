# Task: I'm ready to generate a precise, targeted DuckDB example. Would you prefer an exploration of a specific feature like array manipulation, custom window function, recursive query, or advanced join technique? I'll craft a small, illustrative implementation highlighting a unique DuckDB relational API capability.

## Step 1: I'm ready to generate a precise, targeted DuckDB example. Would you prefer an exploration of a specific feature like array manipulation, custom window function, recursive query, or advanced join technique? I'll craft a small, illustrative implementation highlighting a unique DuckDB relational API capability.

**Generated by**: Anthropic

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create sample tables for demonstrating window functions
conn.execute("""
CREATE TABLE sales (
    product_category VARCHAR,
    sale_date DATE,
    amount DECIMAL(10,2)
);

INSERT INTO sales VALUES
    ('Electronics', '2023-01-15', 1000.50),
    ('Electronics', '2023-02-20', 1500.75),
    ('Clothing', '2023-01-10', 500.25),
    ('Clothing', '2023-02-25', 750.80),
    ('Electronics', '2023-03-05', 1200.30);
""")

# Demonstrate rolling window calculation with cumulative sum
result = conn.execute("""
SELECT 
    product_category, 
    sale_date, 
    amount,
    SUM(amount) OVER (
        PARTITION BY product_category 
        ORDER BY sale_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) as cumulative_sales
FROM sales
ORDER BY product_category, sale_date
""").fetchall()

# Print results
for row in result:
    print(f"Category: {row[0]}, Date: {row[1]}, Sale: ${row[2]}, Cumulative: ${row[3]}")
```

**Result**: [('Clothing', datetime.date(2023, 1, 10), Decimal('500.25'), Decimal('500.25')), ('Clothing', datetime.date(2023, 2, 25), Decimal('750.80'), Decimal('1251.05')), ('Electronics', datetime.date(2023, 1, 15), Decimal('1000.50'), Decimal('1000.50')), ('Electronics', datetime.date(2023, 2, 20), Decimal('1500.75'), Decimal('2501.25')), ('Electronics', datetime.date(2023, 3, 5), Decimal('1200.30'), Decimal('3701.55'))]

**Explanation**: This example demonstrates DuckDB's window function capabilities by performing a cumulative sales calculation partitioned by product category. It shows how to use OVER clause with PARTITION BY and ORDER BY to create rolling window calculations across different product groups.
