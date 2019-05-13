import sqlite3

def connect():
    conn=sqlite3.connect("polio.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs polio (id INTEGER PRIMARY KEY , name TEXT , address TEXT , phone_number INTEGER, Age INTEGER , Dose TEXT , V_id INTEGER)")
    conn.commit()
    conn.close()
def insert(name,address,phone_number,Age,Dose,V_id):
    from back import calculation
    conn=sqlite3.connect("polio.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO polio VALUES (NULL, ?,?,?,?,?,?)",(name,address,phone_number,Age,Dose,V_id))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("polio.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM polio")
    row=cur.fetchall()
    conn.close()
    return row

def search(name="",address="",phone_number="",Dose="",Age="",V_id=""):
    conn=sqlite3.connect("polio.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM polio WHERE name=? OR address=? OR phone_number=?  OR  Dose=?  OR  Age=?  OR  V_id=?",(name,address,phone_number,Dose,Age,V_id))
    row=cur.fetchall()
    conn.close()
    return row

def delete(id):
    conn=sqlite3.connect("polio.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM polio  where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,address,phone_number,Dose,Age,V_id):
    from back import calculation
    conn=sqlite3.connect("polio.db")
    cur=conn.cursor()
    cur.execute("UPDATE polio SET name=? ,address=? , phone_number=? ,  Dose=? , Age=? , V_id=? where id=?",(name,address,phone_number,Dose,Age,calculation(Age,Dose),id))
    conn.commit()
    conn.close()


def calculation(Age,Dose):
    if Dose==("normal" or "NORMAL"):
        V_id=int(Age)*1500
        return V_id
    elif Dose==("POLIO" or "polio"):
        V_id=int(Age)*1800
        return V_id
    elif Dose==("HEPATITIES" or "hepstities"):
        V_id=int(Age)*2000
        return V_id
connect()
