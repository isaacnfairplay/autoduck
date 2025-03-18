# Generated: 2025-03-18 05:43:05.449029
# Result: [('Electronics', 1500, 1500), ('Electronics', 2300, 3800), ('Clothing', 1200, 1200), ('Clothing', 1800, 3000)]
# Valid: True
# Variable con: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
import duckdb

con = duckdb.connect(':memory:')

# Create sales data
con.sql("""
CREATE TABLE sales AS
SELECT 'Electronics' as category, 1500 as amount
UNION ALL
SELECT 'Electronics', 2300
UNION ALL
SELECT 'Clothing', 1200
UNION ALL
SELECT 'Clothing', 1800
""")

# Compute cumulative sales with window function
result = con.sql("""
SELECT 
    category, 
    amount,
    SUM(amount) OVER (PARTITION BY category ORDER BY amount) as cumulative_category_sales
FROM sales
""").fetchall()

print(result)