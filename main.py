from fastapi import FastAPI, Request
import random
import string

app = FastAPI()

@app.middleware('http')
async def request_id_logging(request: Request, call_next):
    response = await call_next(request)
    request_id = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    print(f'Log {request_id}')
    response.headers['X-Request-ID'] = request_id
    return response

@app.get('/')
async def root():
    return {'Hello': 'World'}