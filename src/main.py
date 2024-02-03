from typing import Union
from fastapi import FastAPI, status

app = FastAPI()

@app.get('/')
def generate_secret():
    return { 'secret': 'skfjsknfkdsjfknsdkfksdnfskdfnsd' }

@app.get('/healthz', status_code=status.HTTP_200_OK)
def healthz():
    return { 'status': status.HTTP_200_OK  , 'message': 'OK' }