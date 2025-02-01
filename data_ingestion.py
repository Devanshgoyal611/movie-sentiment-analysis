import sqlite3
import pandas as pd

# Load the dataset
df = pd.read_csv('data/IMDB Dataset.csv')

# Connect to SQLite database (or create it)
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Movie_reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    review TEXT,
    sentiment TEXT
)
''')

# Insert data into the table
for index, row in df.iterrows():
    cursor.execute('''
    INSERT INTO Movie_reviews (review, sentiment)
    VALUES (?, ?)
    ''', (row['review'], row['sentiment']))

# Commit the transaction and close the connection
conn.commit()
conn.close()
print('Done')