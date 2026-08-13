import sqlite3
import ollama

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS payments (
    user TEXT,
    amount REAL
)
""")

cursor.executemany("""
INSERT INTO payments (user, amount) VALUES (?, ?)
""", [
    ("Nico", 1500.0),
    ("Sofia", 3200.0),
    ("Martin", 800.0),
    ("Nico", 2100.0)
])
conn.commit()

db_squeme = """
Table: payments
Columns:
- user (TEXT)
- amount (REAL)
"""

question = "Insert a new user, user: 'John', amount: 1500.0"

prompt = f"""
You are an assistant of data bases of sqlite
{db_squeme}

Only respond with the sql code of the given order: "{question}".
Dont give any text that isn't the sql code, and dont use the markdown used with sql code
"""

response = ollama.chat(
    model="qwen2.5:1.5b",
    messages=[{"role": "user", "content": prompt}]
)

sql_generated = response["message"]["content"].strip().replace("```sql", "").replace("```", "")

cursor.execute(sql_generated)
conn.commit()
print(sql_generated)

conn.close()