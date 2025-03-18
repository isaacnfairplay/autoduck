# Generated: 2025-03-16 22:44:48.339025
# Result: [(['name', 'price'],), (['name', 'price'],)]
# Valid: True
# Variable customer_orders: Type: DuckDBPyRelation
# Attributes/Methods: _pybind11_conduit_v1_(), aggregate(), alias, any_value(), apply(), arg_max(), arg_min(), arrow(), avg(), bit_and(), bit_or(), bit_xor(), bitstring_agg(), bool_and(), bool_or(), close(), columns, count(), create(), create_view(), cross(), cume_dist(), dense_rank(), describe(), description, df(), distinct(), dtypes, except_(), execute(), explain(), favg(), fetch_arrow_reader(), fetch_arrow_table(), fetch_df_chunk(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filter(), first(), first_value(), fsum(), geomean(), histogram(), insert(), insert_into(), intersect(), join(), lag(), last(), last_value(), lead(), limit(), list(), map(), max(), mean(), median(), min(), mode(), n_tile(), nth_value(), order(), percent_rank(), pl(), product(), project(), quantile(), quantile_cont(), quantile_disc(), query(), rank(), rank_dense(), record_batch(), row_number(), select(), select_dtypes(), select_types(), set_alias(), shape, show(), sort(), sql_query(), std(), stddev(), stddev_pop(), stddev_samp(), string_agg(), sum(), tf(), to_arrow_table(), to_csv(), to_df(), to_parquet(), to_table(), to_view(), torch(), type, types, union(), unique(), update(), value_counts(), var(), var_pop(), var_samp(), variance(), write_csv(), write_parquet()
import duckdb

# Advanced DuckDB Relational API Example
con = duckdb.connect(':memory:')

# Create sample tables
con.execute('''
    CREATE TABLE customers (id INT, name VARCHAR);
    CREATE TABLE orders (order_id INT, customer_id INT, amount DECIMAL);

    INSERT INTO customers VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie');
    INSERT INTO orders VALUES (101, 1, 250.50), (102, 1, 350.75), (103, 2, 125.25);
''')

# Complex query using relational API
customer_orders = (con.table('customers')
    .join(con.table('orders'), 'customers.id = orders.customer_id')
    .filter('amount > 200')
    .aggregate('customer_id, SUM(amount) as total_spend')
)

print(customer_orders.execute().fetchall())