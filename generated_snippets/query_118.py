# Generated: 2025-03-18 18:43:59.300678
# Result: [('Electronics', 'Laptop', Decimal('500.0'), Decimal('800.0'), 1), ('Electronics', 'Phone', Decimal('300.0'), Decimal('300.0'), 2), ('Clothing', 'Pants', Decimal('100.0'), Decimal('150.0'), 3), ('Clothing', 'Shirt', Decimal('50.0'), Decimal('50.0'), 4)]
# Valid: True
# Variable conn: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
# Variable result: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
# Variable row: Type: tuple
# Attributes/Methods: count, index
import duckdb

conn = duckdb.connect(':memory:')

# Create sales data
conn.sql("""
CREATE TABLE sales AS
SELECT 'Electronics' AS category, 'Laptop' AS product, 500.0 AS sale_amount
UNION ALL
SELECT 'Electronics', 'Phone', 300.0
UNION ALL
SELECT 'Clothing', 'Shirt', 50.0
UNION ALL
SELECT 'Clothing', 'Pants', 100.0
""")

# Cumulative sales with window function
result = conn.sql("""
SELECT 
    category, 
    product, 
    sale_amount,
    SUM(sale_amount) OVER (PARTITION BY category ORDER BY sale_amount) as cumulative_category_sales,
    RANK() OVER (ORDER BY sale_amount DESC) as overall_sales_rank
FROM sales
""").fetchall()

for row in result:
    print(row)