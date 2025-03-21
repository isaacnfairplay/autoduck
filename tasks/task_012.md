# Task: I've prepared a concise DuckDB window function example demonstrating cumulative sales and product ranking using the relational API. The code shows how to calculate cumulative sales within categories and rank products by sales amount. Would you like me to elaborate on any specific aspect of the implementation or explore another DuckDB feature?

## Step 1: I've prepared a concise DuckDB window function example demonstrating cumulative sales and product ranking using the relational API. The code shows how to calculate cumulative sales within categories and rank products by sales amount. Would you like me to elaborate on any specific aspect of the implementation or explore another DuckDB feature?

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with product categories
conn.execute("""
    CREATE TABLE sales (
        product_id INT,
        category TEXT,
        sale_amount DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
    (1, 'Electronics', 500.00),
    (2, 'Electronics', 750.50),
    (3, 'Clothing', 250.75),
    (4, 'Clothing', 300.25);
""")

# Window function: cumulative sales per category with ranking
result = conn.execute("""
    SELECT 
        product_id, 
        category, 
        sale_amount,
        SUM(sale_amount) OVER (PARTITION BY category ORDER BY product_id) as cumulative_sales,
        RANK() OVER (PARTITION BY category ORDER BY sale_amount DESC) as sales_rank
    FROM sales
""").fetchall()

for row in result:
    print(row)
```

**Result**: [(2, 'Electronics', Decimal('750.50'), Decimal('1250.50'), 1), (1, 'Electronics', Decimal('500.00'), Decimal('500.00'), 2), (4, 'Clothing', Decimal('300.25'), Decimal('551.00'), 1), (3, 'Clothing', Decimal('250.75'), Decimal('250.75'), 2)]

**Explanation**: Demonstrates DuckDB window functions by calculating cumulative sales and ranking products within categories, showcasing partitioning and ranking capabilities in a single query.
