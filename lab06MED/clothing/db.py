import psycopg2

def save_to_db(item, size, fabric, cost):
    conn = psycopg2.connect("dbname=clothing_db user=user password=pass host=localhost port=5432")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS calc (item TEXT, size INT, fabric REAL, cost REAL)")
    cur.execute("INSERT INTO calc VALUES (%s, %s, %s, %s)", (item, size, fabric, cost))
    conn.commit()
    cur.close()
    conn.close()