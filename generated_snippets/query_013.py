# Generated: 2025-03-16 22:10:05.480097
# Result: [(1, datetime.date(2023, 1, 15), 10, Decimal('500.00'), Decimal('500.00'), 12.5), (1, datetime.date(2023, 2, 20), 15, Decimal('750.00'), Decimal('1250.00'), 12.5), (2, datetime.date(2023, 1, 10), 5, Decimal('250.00'), Decimal('250.00'), 6.5), (2, datetime.date(2023, 2, 25), 8, Decimal('400.00'), Decimal('650.00'), 6.5)]
# Valid: True
# Variable employees_rel: Type: DuckDBPyRelation
# Attributes/Methods: _pybind11_conduit_v1_(), aggregate(), alias, any_value(), apply(), arg_max(), arg_min(), arrow(), avg(), bit_and(), bit_or(), bit_xor(), bitstring_agg(), bool_and(), bool_or(), close(), columns, count(), create(), create_view(), cross(), cume_dist(), dense_rank(), describe(), description, df(), distinct(), dtypes, except_(), execute(), explain(), favg(), fetch_arrow_reader(), fetch_arrow_table(), fetch_df_chunk(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filter(), first(), first_value(), fsum(), geomean(), histogram(), insert(), insert_into(), intersect(), join(), lag(), last(), last_value(), lead(), limit(), list(), map(), max(), mean(), median(), min(), mode(), n_tile(), nth_value(), order(), percent_rank(), pl(), product(), project(), quantile(), quantile_cont(), quantile_disc(), query(), rank(), rank_dense(), record_batch(), row_number(), select(), select_dtypes(), select_types(), set_alias(), shape, show(), sort(), sql_query(), std(), stddev(), stddev_pop(), stddev_samp(), string_agg(), sum(), tf(), to_arrow_table(), to_csv(), to_df(), to_parquet(), to_table(), to_view(), torch(), type, types, union(), unique(), update(), value_counts(), var(), var_pop(), var_samp(), variance(), write_csv(), write_parquet()
# Variable conn: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
import duckdb

# Connect to an in-memory database
con = duckdb.connect(':memory:')

# Create a sample table
con.sql('''
    CREATE TABLE sales (
        product_id INTEGER,
        sale_date DATE,
        quantity INTEGER,
        revenue DECIMAL(10,2)
    );
''')

# Insert sample data
con.sql('''
    INSERT INTO sales VALUES
    (1, '2023-01-15', 10, 500.00),
    (1, '2023-02-20', 15, 750.00),
    (2, '2023-01-10', 5, 250.00),
    (2, '2023-02-25', 8, 400.00)
''')

# Complex analytical query with window functions
result = con.sql('''
    SELECT 
        product_id, 
        sale_date, 
        quantity,
        revenue,
        SUM(revenue) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_revenue,
        AVG(quantity) OVER (PARTITION BY product_id) as avg_product_quantity
    FROM sales
    ORDER BY product_id, sale_date
''').fetchall()

for row in result:
    print(row)