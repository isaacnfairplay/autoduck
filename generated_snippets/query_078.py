# Generated: 2025-03-16 22:51:27.464141
# Result: [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
# Valid: True
# Variable join_result: Type: DuckDBPyRelation
# Attributes/Methods: _pybind11_conduit_v1_(), aggregate(), alias, any_value(), apply(), arg_max(), arg_min(), arrow(), avg(), bit_and(), bit_or(), bit_xor(), bitstring_agg(), bool_and(), bool_or(), close(), columns, count(), create(), create_view(), cross(), cume_dist(), dense_rank(), describe(), description, df(), distinct(), dtypes, except_(), execute(), explain(), favg(), fetch_arrow_reader(), fetch_arrow_table(), fetch_df_chunk(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filter(), first(), first_value(), fsum(), geomean(), histogram(), insert(), insert_into(), intersect(), join(), lag(), last(), last_value(), lead(), limit(), list(), map(), max(), mean(), median(), min(), mode(), n_tile(), nth_value(), order(), percent_rank(), pl(), product(), project(), quantile(), quantile_cont(), quantile_disc(), query(), rank(), rank_dense(), record_batch(), row_number(), select(), select_dtypes(), select_types(), set_alias(), shape, show(), sort(), sql_query(), std(), stddev(), stddev_pop(), stddev_samp(), string_agg(), sum(), tf(), to_arrow_table(), to_csv(), to_df(), to_parquet(), to_table(), to_view(), torch(), type, types, union(), unique(), update(), value_counts(), var(), var_pop(), var_samp(), variance(), write_csv(), write_parquet()
import duckdb

con = duckdb.connect(':memory:')
con.execute('CREATE TABLE employees (id INT, name VARCHAR, department VARCHAR)')
con.execute('CREATE TABLE departments (id INT, dept_name VARCHAR)')

con.execute("INSERT INTO employees VALUES (1, 'Alice', 'Sales'), (2, 'Bob', 'Marketing'), (3, 'Charlie', 'Sales')")
con.execute("INSERT INTO departments VALUES (1, 'Sales'), (2, 'Marketing'), (3, 'Engineering')")

employees_rel = con.query('SELECT * FROM employees')
departments_rel = con.query('SELECT * FROM departments')

join_result = employees_rel.join(departments_rel, 'department = dept_name')
print(join_result.execute().fetchall())