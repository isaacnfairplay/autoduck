# Generated: 2025-03-18 05:42:04.532297
# Result: [('Electronics', Decimal('1200.00'), Decimal('2450.50'), 1), ('Electronics', Decimal('750.50'), Decimal('1250.50'), 2), ('Electronics', Decimal('500.00'), Decimal('500.00'), 3), ('Clothing', Decimal('300.75'), Decimal('551.00'), 1), ('Clothing', Decimal('250.25'), Decimal('250.25'), 2)]
# Valid: True
# Variable conn: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
# Variable result: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
# Variable row: Type: tuple
# Attributes/Methods: count, index
import duckdb

# Create an in-memory database
conn = duckdb.connect(':memory:')

# Create sales table with product and sales data
conn.execute('''
    CREATE TABLE sales (
        product_category VARCHAR,
        sale_amount DECIMAL(10,2)
    );
''')

# Insert sample sales data
conn.executemany('INSERT INTO sales VALUES (?, ?)', [
    ('Electronics', 500.00),
    ('Electronics', 750.50),
    ('Clothing', 250.25),
    ('Clothing', 300.75),
    ('Electronics', 1200.00)
])

# Calculate cumulative sales and rank within product categories
result = conn.execute('''
    SELECT 
        product_category, 
        sale_amount,
        SUM(sale_amount) OVER (PARTITION BY product_category ORDER BY sale_amount) as cumulative_sales,
        RANK() OVER (PARTITION BY product_category ORDER BY sale_amount DESC) as sales_rank
    FROM sales
''').fetchall()

for row in result:
    print(row)