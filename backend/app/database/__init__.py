import sqlite3
from flask import g

DATABASE_URL = "user_crud.db"

def get_db():
  db = getattr(g, "_database", None)
  if not db:
    db = g._database = sqlite3.connect(DATABASE_URL)
  return db