from typing import Union
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from string import ascii_letters, digits
from random import choice

MAX_SECRET_LENGTH=10000
app = FastAPI()

@app.get('/')
def generate_secret(length: int = 32):
    result = ''.join(choice(f'{ascii_letters}{digits}') for i in range(length))
    if length >= MAX_SECRET_LENGTH:
        return JSONResponse(content={ 'status': status.HTTP_400_BAD_REQUEST, 'message': f'Maximum secret length is {MAX_SECRET_LENGTH}' })
    return JSONResponse(content={ 'secret': result.lower() })

@app.get('/healthz', status_code=status.HTTP_200_OK)
def healthz():
    return JSONResponse(content={ 'status': status.HTTP_200_OK  , 'message': 'OK' })