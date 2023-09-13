from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"msg": "Hello Wolrd!"}


@app.get('/msg')
async def msg(msg ):
    return {"msg": f"{msg}"}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level='info', reload=True)