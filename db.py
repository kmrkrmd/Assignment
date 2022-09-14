import sqlite3

conn = sqlite3.connect("data.db")
#conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, mob TEXT,mail TEXT,psw TEXT)")
conn.execute("CREATE TABLE address(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, mob TEXT,mail TEXT,psw TEXT,addr TEXT)")
