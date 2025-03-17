# Generated: 2025-03-16 22:44:56.626572
# Result: [(['name', 'price'],), (['name', 'price'],)]
# Valid: True
# Variable multi_join_result: Type: DuckDBPyRelation
# Attributes/Methods: _pybind11_conduit_v1_(), aggregate(), alias, any_value(), apply(), arg_max(), arg_min(), arrow(), avg(), bit_and(), bit_or(), bit_xor(), bitstring_agg(), bool_and(), bool_or(), close(), columns, count(), create(), create_view(), cross(), cume_dist(), dense_rank(), describe(), description, df(), distinct(), dtypes, except_(), execute(), explain(), favg(), fetch_arrow_reader(), fetch_arrow_table(), fetch_df_chunk(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filter(), first(), first_value(), fsum(), geomean(), histogram(), insert(), insert_into(), intersect(), join(), lag(), last(), last_value(), lead(), limit(), list(), map(), max(), mean(), median(), min(), mode(), n_tile(), nth_value(), order(), percent_rank(), pl(), product(), project(), quantile(), quantile_cont(), quantile_disc(), query(), rank(), rank_dense(), record_batch(), row_number(), select(), select_dtypes(), select_types(), set_alias(), shape, show(), sort(), sql_query(), std(), stddev(), stddev_pop(), stddev_samp(), string_agg(), sum(), tf(), to_arrow_table(), to_csv(), to_df(), to_parquet(), to_table(), to_view(), torch(), type, types, union(), unique(), update(), value_counts(), var(), var_pop(), var_samp(), variance(), write_csv(), write_parquet()
import duckdb

# Advanced Multi-Table Join Example
con = duckdb.connect(':memory:')

# Create sample tables with more complex relationships
con.execute('''
    CREATE TABLE employees (emp_id INT, name VARCHAR, dept_id INT);
    CREATE TABLE departments (dept_id INT, dept_name VARCHAR);
    CREATE TABLE salaries (emp_id INT, salary DECIMAL);

    INSERT INTO employees VALUES 
        (1, 'Alice', 10), (2, 'Bob', 20), (3, 'Charlie', 10), (4, 'David', 30);
    INSERT INTO departments VALUES 
        (10, 'Sales'), (20, 'Marketing'), (30, 'Engineering');
    INSERT INTO salaries VALUES 
        (1, 50000), (2, 60000), (3, 55000), (4, 75000);
''')

# Complex multi-table join with filtering and aggregation
multi_join_result = (
    con.table('employees')
    .join(con.table('departments'), 'employees.dept_id = departments.dept_id')
    .join(con.table('salaries'), 'employees.emp_id = salaries.emp_id')
    .filter('salary > 52000')
    .aggregate('dept_name, AVG(salary) as avg_dept_salary, COUNT(*) as employee_count')
)

print(multi_join_result.execute().fetchall())