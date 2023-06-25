from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Request, Path, Query, status, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# app = FastAPI()
#
# template_instance = Jinja2Templates('templates')
#
#
# @app.get('/index/{username}', response_class=HTMLResponse)
# async def index(request: Request, username: str):
#     # print('='*10)
#     # print(list(request))  # inside in request for jinja
#     context = {
#         'request': request,
#         'username': username
#     }
#     return template_instance.TemplateResponse('test.html', context)

# Response models ,Handling Error, Status codes,
# class user_in(BaseModel):
#     title: str
#     email: str
#     password: str = Path(min_length=8, max_length=18)
#
#
# class user_out(BaseModel):
#     title: str
#     email: str
#
#
# @app.post('/res', response_model=user_out, status_code=status.HTTP_200_OK)
# async def response(user: user_in):
#     if user.title == 'admin':
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='title is cant be admin.'
#         ,headers={"X-Error": "title is cant be admin."})
#     return user

# @app.get('/')
# async def read_root():
#     return str('Hello Mahdi')
#
#
# user_names = ['mahdi ', 'ali', 'hassan']
#
#
# # path parameters
#
# @app.get('/user')
# async def show_members():
#     return user_names
#
#
# # query parameters
# @app.get('/age')
# async def user_age(item: int = 22):
#     return {'age is:': item}


# request body and optional filed and Path , Query

# class Request_class(BaseModel):
#     name: str
#     age: int = Path(ge=0, le=99, title='user age')
#     city: str
#     uni: str | None = None
#
#
# @app.post('/req')
# async def request_body(request: Request_class, car: str = Query('Default', min_length=2, max_length=20)):
#     # return request
#     return {'user is : ': request, 'and his car :': car}
