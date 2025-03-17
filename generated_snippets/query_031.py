# Generated: 2025-03-16 22:39:34.139291
# Result: [(1, datetime.date(2023, 1, 15), 10, Decimal('25.50'), 10, 25.5), (1, datetime.date(2023, 3, 10), 8, Decimal('25.50'), 18, 25.5), (2, datetime.date(2023, 2, 20), 5, Decimal('30.75'), 5, 30.75)]
# Valid: True
# Variable conn: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
# Variable result: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
# Variable con: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
# Variable row: Type: tuple
# Attributes/Methods: count, index
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample sales table
conn.execute('''
CREATE TABLE sales (
    product_id INTEGER,
    sale_date DATE,
    quantity INTEGER,
    price DECIMAL(10,2)
)''')

# Insert sample data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?)', [
    (1, '2023-01-15', 10, 25.50),
    (2, '2023-02-20', 5, 30.75),
    (1, '2023-03-10', 8, 25.50)
])

# Complex analytical query with window functions
result = conn.execute('''
SELECT 
    product_id, 
    sale_date, 
    quantity, 
    price,
    SUM(quantity) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_sales,
    AVG(price) OVER (PARTITION BY product_id) as avg_product_price
FROM sales
''').fetchall()

for row in result:
    print(row)