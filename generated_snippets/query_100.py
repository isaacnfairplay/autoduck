# Generated: 2025-03-17 19:49:49.648617
# Result: [(1, datetime.date(2023, 1, 15), 10, Decimal('50.00'), 10, 50.0), (1, datetime.date(2023, 2, 20), 15, Decimal('55.00'), 25, 52.5), (2, datetime.date(2023, 1, 10), 5, Decimal('100.00'), 5, 100.0), (2, datetime.date(2023, 2, 25), 8, Decimal('110.00'), 13, 105.0)]
# Valid: True
# Variable query: Type: str
# Attributes/Methods: capitalize, casefold, center, count, encode, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, removeprefix, removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill
# Variable row: Type: tuple
# Attributes/Methods: count, index
# Variable result: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

# Create in-memory database connection
con = duckdb.connect(':memory:')

# Create sample sales table
con.execute('''
CREATE TABLE sales (
    product_id INT,
    sale_date DATE,
    quantity INT,
    price DECIMAL(10,2)
)''')

# Insert sample sales data
con.executemany('INSERT INTO sales VALUES (?, ?, ?, ?)', [
    (1, '2023-01-15', 10, 50.00),
    (1, '2023-02-20', 15, 55.00),
    (2, '2023-01-10', 5, 100.00),
    (2, '2023-02-25', 8, 110.00)
])

# Advanced analytical query with window functions
query = '''
SELECT 
    product_id, 
    sale_date, 
    quantity, 
    price,
    SUM(quantity) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_quantity,
    AVG(price) OVER (PARTITION BY product_id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as rolling_avg_price
FROM sales
'''

result = con.execute(query).fetchall()
for row in result:
    print(row)