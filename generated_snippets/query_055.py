# Generated: 2025-03-16 22:45:12.771471
# Result: [('North', 'B', Decimal('1500.000'), Decimal('2500.000'), 1), ('East', 'A', Decimal('1300.000'), Decimal('2400.000'), 2), ('South', 'B', Decimal('1200.000'), Decimal('2000.000'), 3), ('East', 'B', Decimal('1100.000'), Decimal('2400.000'), 4), ('North', 'A', Decimal('1000.000'), Decimal('2500.000'), 5), ('South', 'A', Decimal('800.000'), Decimal('2000.000'), 6)]
# Valid: True
# Variable filtered_products: Type: DuckDBPyRelation
# Attributes/Methods: _pybind11_conduit_v1_(), aggregate(), alias, any_value(), apply(), arg_max(), arg_min(), arrow(), avg(), bit_and(), bit_or(), bit_xor(), bitstring_agg(), bool_and(), bool_or(), close(), columns, count(), create(), create_view(), cross(), cume_dist(), dense_rank(), describe(), description, df(), distinct(), dtypes, except_(), execute(), explain(), favg(), fetch_arrow_reader(), fetch_arrow_table(), fetch_df_chunk(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filter(), first(), first_value(), fsum(), geomean(), histogram(), insert(), insert_into(), intersect(), join(), lag(), last(), last_value(), lead(), limit(), list(), map(), max(), mean(), median(), min(), mode(), n_tile(), nth_value(), order(), percent_rank(), pl(), product(), project(), quantile(), quantile_cont(), quantile_disc(), query(), rank(), rank_dense(), record_batch(), row_number(), select(), select_dtypes(), select_types(), set_alias(), shape, show(), sort(), sql_query(), std(), stddev(), stddev_pop(), stddev_samp(), string_agg(), sum(), tf(), to_arrow_table(), to_csv(), to_df(), to_parquet(), to_table(), to_view(), torch(), type, types, union(), unique(), update(), value_counts(), var(), var_pop(), var_samp(), variance(), write_csv(), write_parquet()
import duckdb

# Advanced Filtering and Transformation with DuckDB
con = duckdb.connect(':memory:')

# Create sample data
con.execute('''CREATE TABLE products (
    id INT,
    name VARCHAR,
    category VARCHAR,
    price DECIMAL,
    stock INT
)''')

con.execute('''INSERT INTO products VALUES
    (1, 'Laptop', 'Electronics', 1200.50, 50),
    (2, 'Phone', 'Electronics', 800.25, 75),
    (3, 'Tablet', 'Electronics', 500.00, 100),
    (4, 'Headphones', 'Accessories', 150.75, 200)''')

# Advanced filtering with complex conditions
filtered_products = con.query('''
    SELECT 
        name, 
        category, 
        price,
        CASE 
            WHEN price > 1000 THEN 'High-End'
            WHEN price BETWEEN 500 AND 1000 THEN 'Mid-Range'
            ELSE 'Budget'
        END as price_tier,
        stock * price as total_inventory_value
    FROM products
    WHERE category = 'Electronics' AND stock > 25
    ORDER BY total_inventory_value DESC
''')

print(filtered_products.fetchall())