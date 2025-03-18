# Generated: 2025-03-16 22:45:04.342490
# Result: [('North', 'B', Decimal('1500.000'), Decimal('2500.000'), 1), ('East', 'A', Decimal('1300.000'), Decimal('2400.000'), 2), ('South', 'B', Decimal('1200.000'), Decimal('2000.000'), 3), ('East', 'B', Decimal('1100.000'), Decimal('2400.000'), 4), ('North', 'A', Decimal('1000.000'), Decimal('2500.000'), 5), ('South', 'A', Decimal('800.000'), Decimal('2000.000'), 6)]
# Valid: True
# Variable window_query: Type: str
# Attributes/Methods: capitalize, casefold, center, count, encode, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, removeprefix, removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill
import duckdb

# Window Function Demonstration
con = duckdb.connect(':memory:')

# Create and populate sample sales table
con.execute('''CREATE TABLE sales (region VARCHAR, product VARCHAR, sale_amount DECIMAL)''')
con.execute('''INSERT INTO sales VALUES 
    ('North', 'A', 1000), 
    ('North', 'B', 1500), 
    ('South', 'A', 800), 
    ('South', 'B', 1200), 
    ('East', 'A', 1300), 
    ('East', 'B', 1100)''')

# Demonstrate window functions
window_query = '''
SELECT 
    region, 
    product, 
    sale_amount,
    SUM(sale_amount) OVER (PARTITION BY region) as region_total,
    RANK() OVER (ORDER BY sale_amount DESC) as sales_rank
FROM sales
'''

result = con.execute(window_query).fetchall()
for row in result:
    print(row)