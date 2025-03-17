# Generated: 2025-03-16 22:10:45.870330
# Result: [(1, 'Laptop', Decimal('500.00'), '2023-01-15'), (2, 'Smartphone', Decimal('350.00'), '2023-02-20')]
# Valid: True
# Variable product_sales: Type: DuckDBPyRelation
# Attributes/Methods: _pybind11_conduit_v1_(), aggregate(), alias, any_value(), apply(), arg_max(), arg_min(), arrow(), avg(), bit_and(), bit_or(), bit_xor(), bitstring_agg(), bool_and(), bool_or(), close(), columns, count(), create(), create_view(), cross(), cume_dist(), dense_rank(), describe(), description, df(), distinct(), dtypes, except_(), execute(), explain(), favg(), fetch_arrow_reader(), fetch_arrow_table(), fetch_df_chunk(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filter(), first(), first_value(), fsum(), geomean(), histogram(), insert(), insert_into(), intersect(), join(), lag(), last(), last_value(), lead(), limit(), list(), map(), max(), mean(), median(), min(), mode(), n_tile(), nth_value(), order(), percent_rank(), pl(), product(), project(), quantile(), quantile_cont(), quantile_disc(), query(), rank(), rank_dense(), record_batch(), row_number(), select(), select_dtypes(), select_types(), set_alias(), shape, show(), sort(), sql_query(), std(), stddev(), stddev_pop(), stddev_samp(), string_agg(), sum(), tf(), to_arrow_table(), to_csv(), to_df(), to_parquet(), to_table(), to_view(), torch(), type, types, union(), unique(), update(), value_counts(), var(), var_pop(), var_samp(), variance(), write_csv(), write_parquet()
import duckdb

# Connect to an in-memory database
con = duckdb.connect(':memory:')

# Create a sample relation with product sales data
product_sales = con.sql('''
    SELECT * FROM (
        VALUES 
        (1, 'Laptop', 500.00, '2023-01-15'),
        (2, 'Smartphone', 350.00, '2023-02-20'),
        (3, 'Tablet', 250.00, '2023-03-10')
    ) AS t(product_id, product_name, price, sale_date)
''')

# Demonstrate relation methods
result = product_sales.filter('price > 300').execute().fetchall()
print(result)