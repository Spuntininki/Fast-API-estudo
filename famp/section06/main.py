from fastapi import FastAPI

from core.configs import settings
from api.V1.api import api_router

app = FastAPI(title='Curso API - Segurança')

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)


'''
  "access_token": eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE3MDIxNzA5NzgsImlhdCI6MTcwMTU2NjE3OCwic3ViIjoiMiJ9.priUQnC6swEjtQjP871ytPAYocqrJC5TDeAz9qxj8yU
  "token_type": bearer
'''