from src.models.database import database
from src.models.cookie import Cookie
import streamlit as st
from hashlib import sha256

def login(email, mdp):
    db = database()
    mdp = sha256(mdp.encode(encoding="utf-32")).hexdigest()

    res = db.execute(f"SELECT * FROM users WHERE password='{mdp}'AND email='{email}'").fetchone()

    if res != None:
        c = Cookie("data.json")
        c.update({"email": res[1], "uid": res[0]})
        return True
    else:
        return False

def logout():
    c=Cookie("data.json")
    c.clean()

def signin(email, mdp):
    db = database()
    mdp = sha256(mdp.encode(encoding="utf-32")).hexdigest()
    db.execute(f"INSERT INTO users (email, password) VALUES ({email, mdp})")
    db.commit()