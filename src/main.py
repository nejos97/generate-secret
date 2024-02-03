from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def generate_secret():
    return { 'secret': 'skfjsknfkdsjfknsdkfksdnfskdfnsd' }