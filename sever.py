from fastapi import FastAPI
import sqlite3
from uvicorn import run
from pydantic import BaseModel



class user(BaseModel):
    name:str
    mobile:str
    mail:str
    psw:str
    addr:str

app = FastAPI()

@app.get('/')
def index():
    return {'msg':'Hello'}



@app.get('/address/{id}')
async def read_id(id:int):
    conn = sqlite3.connect("data.db")
    cur = conn.execute("SELECT * FROM address WHERE id=?",(id,))
    row = cur.fetchone()
    user_data = {"id":row[0],
                 "name":row[1],
                 "mobile":row[2],
                 "mail":row[3],
                 "psw": row[4],
                 "address":row[5]
                 }

    return {"user_data":user_data}

@app.put('/user/')
async def create_user(user_data:user):
    conn = sqlite3.connect("data.db")
    conn.execute("INSERT INTO address(name,mob,mail,psw,addr)VALUES(?,?,?,?,?)",(user_data.name,user_data.mobile,user_data.mail,user_data.psw,user_data.addr))
    conn.commit()
    msg={"msg":"Address Added!"}
    return {"user_data":user_data,"msg":msg}
@app.get('/all')
async def view_all():
    conn=sqlite3.connect("data.db")
    cur = conn.execute("SELECT * FROM address")
    rows=cur.fetchall()
    return rows

@app.post('/edit_address/{id}')
async def edit_user(id,user_data:user):
    conn = sqlite3.connect("data.db")
    conn.execute("UPDATE address SET name=?,mob=?,mail=?,psw=?,addr=? WHERE id=?",(user_data.name, user_data.mobile, user_data.mail, user_data.psw,user_data.addr,id))
    conn.commit()
    msg = {"msg": "Address Updated!"}
    return {"user_data": user_data, "msg": msg}

@app.get('/search/{address}')
async def search(address):
    conn = sqlite3.connect("data.db")
    cur=conn.execute("SELECT * FROM address WHERE addr LIKE ?",('%'+address+'%',))
    rows = cur.fetchall()
    return rows

if __name__ == '__main__':
    run(app)

