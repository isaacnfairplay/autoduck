# Generated: 2025-03-19 14:45:49.882552
# Result: [('Paris', 'France', 2161000, 1), ('Berlin', 'Germany', 3669000, 1), ('London', 'UK', 8982000, 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample table with geographic data
conn.execute("CREATE TABLE cities (name VARCHAR, country VARCHAR, population INTEGER)")
conn.execute("INSERT INTO cities VALUES ('Paris', 'France', 2161000), ('London', 'UK', 8982000), ('Berlin', 'Germany', 3669000)")

# Use window function to rank cities by population within their country
result = conn.execute("""
    SELECT 
        name, 
        country, 
        population, 
        RANK() OVER (PARTITION BY country ORDER BY population DESC) as population_rank
    FROM cities
""").fetchall()

for row in result:
    print(f"{row[0]} ({row[1]}): Population {row[2]}, Rank {row[3]}")