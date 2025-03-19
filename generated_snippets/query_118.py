# Generated: 2025-03-19 11:19:35.044960
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create time series table tracking inventory changes
conn.sql('''
CREATE TABLE inventory_log (
    product_id INTEGER,
    change_time TIMESTAMP,
    quantity_change INTEGER
);

INSERT INTO inventory_log VALUES
    (1, '2023-07-01 10:00:00', 50),
    (1, '2023-07-01 11:00:00', -10),
    (1, '2023-07-01 12:00:00', 20);

-- Calculate cumulative inventory and rate of change
SELECT
    product_id,
    change_time,
    quantity_change,
    SUM(quantity_change) OVER (PARTITION BY product_id ORDER BY change_time) as cumulative_inventory,
    quantity_change - LAG(quantity_change) OVER (PARTITION BY product_id ORDER BY change_time) as inventory_delta
FROM inventory_log
''').show()