# Generated: 2025-03-17 19:59:48.923062
# Result: [('David', 'Engineering', Decimal('75000.000'), 75000.0, Decimal('500000.000'), 1), ('Bob', 'Marketing', Decimal('60000.000'), 60000.0, Decimal('200000.000'), 2), ('Charlie', 'Sales', Decimal('55000.000'), 52500.0, Decimal('250000.000'), 3), ('Alice', 'Sales', Decimal('50000.000'), 52500.0, Decimal('250000.000'), 4)]
# Valid: True
# Variable employees_rel: Type: DuckDBPyRelation
# Attributes/Methods: _pybind11_conduit_v1_(), aggregate(), alias, any_value(), apply(), arg_max(), arg_min(), arrow(), avg(), bit_and(), bit_or(), bit_xor(), bitstring_agg(), bool_and(), bool_or(), close(), columns, count(), create(), create_view(), cross(), cume_dist(), dense_rank(), describe(), description, df(), distinct(), dtypes, except_(), execute(), explain(), favg(), fetch_arrow_reader(), fetch_arrow_table(), fetch_df_chunk(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filter(), first(), first_value(), fsum(), geomean(), histogram(), insert(), insert_into(), intersect(), join(), lag(), last(), last_value(), lead(), limit(), list(), map(), max(), mean(), median(), min(), mode(), n_tile(), nth_value(), order(), percent_rank(), pl(), product(), project(), quantile(), quantile_cont(), quantile_disc(), query(), rank(), rank_dense(), record_batch(), row_number(), select(), select_dtypes(), select_types(), set_alias(), show(), sort(), sql_query(), std(), stddev(), stddev_pop(), stddev_samp(), string_agg(), sum(), tf(), to_arrow_table(), to_csv(), to_df(), to_parquet(), to_table(), to_view(), torch(), type, types, union(), unique(), update(), value_counts(), var(), var_pop(), var_samp(), variance(), write_csv(), write_parquet()
# Variable con: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
import duckdb

# Create an in-memory DuckDB connection
con = duckdb.connect(':memory:')

# Create employees table
con.execute('CREATE TABLE employees (id INT, name VARCHAR, department VARCHAR, salary DECIMAL)')

# Insert sample data
con.execute("""INSERT INTO employees VALUES
    (1, 'Alice', 'Sales', 50000.00),
    (2, 'Bob', 'Marketing', 60000.00),
    (3, 'Charlie', 'Engineering', 75000.00)
""")

# Create a relation from the employees table
employees_rel = con.table('employees')

# Print relation details
print('Columns:', employees_rel.columns)
print('Column Types:', employees_rel.types)

# Execute and fetch relation data
results = employees_rel.execute().fetchall()
for row in results:
    print(row)

con.close()