# Generated: 2025-03-17 21:25:05.250132
# Result: None
# Valid: True
# Variable results: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
# Variable query: Type: str
# Attributes/Methods: capitalize, casefold, center, count, encode, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, removeprefix, removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill
# Variable con: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
# Variable row: Type: tuple
# Attributes/Methods: count, index
import duckdb

# Establish an in-memory DuckDB connection
con = duckdb.connect(':memory:')

# Create sample relations
con.execute('''
    CREATE TABLE customers (id INT, name VARCHAR, city VARCHAR);
    CREATE TABLE orders (order_id INT, customer_id INT, total DECIMAL(10,2));

    INSERT INTO customers VALUES 
        (1, 'Alice', 'New York'),
        (2, 'Bob', 'San Francisco'),
        (3, 'Charlie', 'Chicago');

    INSERT INTO orders VALUES 
        (101, 1, 250.50),
        (102, 1, 150.75),
        (103, 2, 325.00);
''')

# Demonstrate complex join with window function
query = '''
    SELECT 
        c.name, 
        c.city, 
        o.order_id, 
        o.total,
        SUM(o.total) OVER (PARTITION BY c.id) as customer_total_spend,
        RANK() OVER (ORDER BY o.total DESC) as order_rank
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
'''

# Execute query and display results
results = con.execute(query).fetchall()
for row in results:
    print(row)
