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

import pandas as pd

data = pd.read_csv('online_retail_ii.csv')
data.dropna(inplace=True) 


data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
data.to_sql('transactions', conn, if_exists='replace', index=False)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
data['InvoiceDate'].value_counts().plot(kind='line')
plt.title('Number of Transactions Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Transactions')
plt.show()
