import psycopg2
from datetime import datetime

def save_score(score):
    conn = psycopg2.connect("dbname=snake_db user=user password=pass host=localhost port=5432")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS snake_stats (id SERIAL PRIMARY KEY, score INT, date TIMESTAMP)")
    cur.execute("INSERT INTO snake_stats (score, date) VALUES (%s, %s)", (score, datetime.now()))
    conn.commit()
    cur.close()
    conn.close()

def get_scores():
    conn = psycopg2.connect("dbname=snake_db user=user password=pass host=localhost port=5432")
    cur = conn.cursor()
    cur.execute("SELECT score, date FROM snake_stats ORDER BY score DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows