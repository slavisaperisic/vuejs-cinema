import psycopg2 as p

con = p.connect("dbname='test' user='postgres' host='localhost' password='elefant11'")
cur = con.cursor()
cur.execute("SELECT p.ime, count(*) FROM profesor p JOIN student s ON p.id = s.profesor_id GROUP BY p.ime HAVING COUNT(*) > 1")

rows = cur.fetchall()

---print(rows)---

for x in range(0, 3):

cur.execute(sql, (value1, value2))