# Generated: 2025-03-19 08:02:06.239426
# Result: [('Electronics', 'Laptop', 1200, 2000, 1), ('Electronics', 'Smartphone', 800, 800, 2), ('Clothing', 'Jeans', 100, 150, 1), ('Clothing', 'Shirt', 50, 50, 2)]
# Valid: True
# Variable row: Type: tuple
# Attributes/Methods: count, index
# Variable conn: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
# Variable result: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales data
conn.sql("""
CREATE TABLE sales AS
SELECT 'Electronics' as category, 'Laptop' as product, 1200 as price
UNION ALL
SELECT 'Electronics', 'Smartphone', 800
UNION ALL
SELECT 'Clothing', 'Shirt', 50
UNION ALL
SELECT 'Clothing', 'Jeans', 100
""")

# Calculate cumulative sales and product rank within category
result = conn.sql("""
SELECT 
    category, 
    product, 
    price,
    SUM(price) OVER (PARTITION BY category ORDER BY price) as cumulative_category_sales,
    RANK() OVER (PARTITION BY category ORDER BY price DESC) as product_rank
FROM sales
""").fetchall()

for row in result:
    print(row)