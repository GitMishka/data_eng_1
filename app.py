import sqlite3

conn = sqlite3.connect('ecommerce.db')

create_table_query = '''
CREATE TABLE IF NOT EXISTS transactions (
    InvoiceNo TEXT,
    StockCode TEXT,
    Description TEXT,
    Quantity INTEGER,
    InvoiceDate TEXT,
    UnitPrice REAL,
    CustomerID INTEGER,
    Country TEXT
);
'''
conn.execute(create_table_query)


