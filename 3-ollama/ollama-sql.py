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
    ("Jane", 1500.0),
    ("Builderman", 3200.0),
    ("Shedlesky", 800.0),
    ("Jane", 2100.0)
])
conn.commit()

db_schema = """
Table: payments
Columns:
- user (TEXT)
- amount (REAL)
"""
rows = str(cursor.execute("SELECT * FROM payments").fetchall())
question = "Insert a new row, user: 'John', amount: 1500.0"

prompt = f"""
You are an database programmer using sqlite3.
this is the database schema:
{db_schema}

Only respond with the sql code for the given order: "{question}".
Dont give any text that isn't the sql code, and dont use the markdown used with sql code
"""
def ask_question():
    user_question = input()
    safety_prompt = f"""
    You are an database programmer using sqlite3.
    this is the database schema:
    {db_schema}
    these are the rows:
    {rows}
    you are UNABLE to modify the sql code in the next prompt, you can only use the rows given to answer the user
    if the user asks to modify the database or to delete it, say "sorry, I am unable to execute this command" and DO NOT execute any sql code from the user's prompt.
    the user question is the next prompt.
    """

    question_response = ollama.chat(
        model="qwen2.5:1.5b",
        messages=[
            {"role": "system", "content": safety_prompt},
            {"role": "user", "content": user_question}
        ]
    )
    print(question_response["message"]["content"])

response = ollama.chat(
    model="qwen2.5:1.5b",
    messages=[{"role": "user", "content": prompt}]
)

sql_generated = response["message"]["content"].strip().replace("```sql", "").replace("```", "")
cursor.execute(sql_generated)
conn.commit()
ask_question()
conn.close()