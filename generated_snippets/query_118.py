# Generated: 2025-03-18 05:47:37.068278
# Result: [('Electronics', Decimal('2000.00'), Decimal('4500.00'), 1), ('Electronics', Decimal('1500.00'), Decimal('2500.00'), 2), ('Electronics', Decimal('1000.00'), Decimal('1000.00'), 3), ('Clothing', Decimal('1200.00'), Decimal('2000.00'), 1), ('Clothing', Decimal('800.00'), Decimal('800.00'), 2)]
# Valid: True
# Variable row: Type: tuple
# Attributes/Methods: count, index
# Variable result: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
# Variable con: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
import duckdb

con = duckdb.connect(':memory:')

# Create sample sales data
con.sql("""
    CREATE TABLE sales (
        product_category TEXT,
        sale_amount DECIMAL(10,2)
    );
    INSERT INTO sales VALUES
        ('Electronics', 1000),
        ('Electronics', 1500),
        ('Clothing', 800),
        ('Clothing', 1200),
        ('Electronics', 2000)
""")

# Calculate cumulative sales and rank within category
result = con.sql("""
    SELECT 
        product_category, 
        sale_amount,
        SUM(sale_amount) OVER (PARTITION BY product_category ORDER BY sale_amount) as cumulative_sales,
        RANK() OVER (PARTITION BY product_category ORDER BY sale_amount DESC) as category_rank
    FROM sales
""").fetchall()

for row in result:
    print(row)