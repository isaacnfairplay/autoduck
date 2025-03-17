# Generated: 2025-03-16 22:07:53.683678
# Result: [(1, datetime.date(2023, 1, 15), 10, Decimal('50.00'), 10, 50.0), (1, datetime.date(2023, 2, 20), 15, Decimal('52.50'), 25, 51.25), (2, datetime.date(2023, 1, 10), 5, Decimal('75.00'), 5, 75.0), (2, datetime.date(2023, 3, 5), 8, Decimal('77.25'), 13, 76.125)]
# Valid: True
# Variable filtered_rel: Type: DuckDBPyRelation
# Attributes/Methods: _pybind11_conduit_v1_(), aggregate(), alias, any_value(), apply(), arg_max(), arg_min(), arrow(), avg(), bit_and(), bit_or(), bit_xor(), bitstring_agg(), bool_and(), bool_or(), close(), columns, count(), create(), create_view(), cross(), cume_dist(), dense_rank(), describe(), description, df(), distinct(), dtypes, except_(), execute(), explain(), favg(), fetch_arrow_reader(), fetch_arrow_table(), fetch_df_chunk(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filter(), first(), first_value(), fsum(), geomean(), histogram(), insert(), insert_into(), intersect(), join(), lag(), last(), last_value(), lead(), limit(), list(), map(), max(), mean(), median(), min(), mode(), n_tile(), nth_value(), order(), percent_rank(), pl(), product(), project(), quantile(), quantile_cont(), quantile_disc(), query(), rank(), rank_dense(), record_batch(), row_number(), select(), select_dtypes(), select_types(), set_alias(), shape, show(), sort(), sql_query(), std(), stddev(), stddev_pop(), stddev_samp(), string_agg(), sum(), tf(), to_arrow_table(), to_csv(), to_df(), to_parquet(), to_table(), to_view(), torch(), type, types, union(), unique(), update(), value_counts(), var(), var_pop(), var_samp(), variance(), write_csv(), write_parquet()
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a sample table with products
con.execute('''
CREATE TABLE products (
    product_id INT,
    category VARCHAR,
    revenue DECIMAL(10,2)
);

INSERT INTO products VALUES
    (1, 'Electronics', 500.50),
    (2, 'Clothing', 250.75),
    (3, 'Books', 100.25);
''')

# Filter relation and display results
filtered_rel = con.query('SELECT * FROM products WHERE revenue > 200').execute()
print('Filtered Relation:\n', filtered_rel.fetchall())