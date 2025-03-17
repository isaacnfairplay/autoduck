# Generated: 2025-03-16 22:17:38.721675
# Result: [('Alice', 'New York', Decimal('1200.75'), Decimal('1701.25'), 1), ('Bob', 'San Francisco', Decimal('750.25'), Decimal('750.25'), 2), ('Alice', 'New York', Decimal('500.50'), Decimal('1701.25'), 3)]
# Valid: True
# Variable employees_rel: Type: DuckDBPyRelation
# Attributes/Methods: _pybind11_conduit_v1_(), aggregate(), alias, any_value(), apply(), arg_max(), arg_min(), arrow(), avg(), bit_and(), bit_or(), bit_xor(), bitstring_agg(), bool_and(), bool_or(), close(), columns, count(), create(), create_view(), cross(), cume_dist(), dense_rank(), describe(), description, df(), distinct(), dtypes, except_(), execute(), explain(), favg(), fetch_arrow_reader(), fetch_arrow_table(), fetch_df_chunk(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filter(), first(), first_value(), fsum(), geomean(), histogram(), insert(), insert_into(), intersect(), join(), lag(), last(), last_value(), lead(), limit(), list(), map(), max(), mean(), median(), min(), mode(), n_tile(), nth_value(), order(), percent_rank(), pl(), product(), project(), quantile(), quantile_cont(), quantile_disc(), query(), rank(), rank_dense(), record_batch(), row_number(), select(), select_dtypes(), select_types(), set_alias(), shape, show(), sort(), sql_query(), std(), stddev(), stddev_pop(), stddev_samp(), string_agg(), sum(), tf(), to_arrow_table(), to_csv(), to_df(), to_parquet(), to_table(), to_view(), torch(), type, types, union(), unique(), update(), value_counts(), var(), var_pop(), var_samp(), variance(), write_csv(), write_parquet()
import duckdb

# Establish in-memory database connection
con = duckdb.connect(':memory:')

# Create employees relation with advanced analytics
employees_rel = con.query('''
SELECT 
    id, 
    name, 
    department, 
    salary,
    AVG(salary) OVER (PARTITION BY department) AS dept_avg_salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM (
    VALUES 
    (1, 'Alice', 'Sales', 75000),
    (2, 'Bob', 'Engineering', 85000),
    (3, 'Charlie', 'Marketing', 65000),
    (4, 'David', 'Sales', 72000)
) t(id, name, department, salary)
''')

# Display results
for row in employees_rel.fetchall():
    print(row)