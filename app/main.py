from fastapi import FastAPI
from .library import Book

app = FastAPI(title="FastAPI by Cruella_De_Vil")


@app.get ('/')
def home():
    return {'Ура':'Мы работаем'}


@app.get('/{pk}')
def get_item(pk: int, q: int = None):
    return {'key': pk, 'q': q}

#/"число целое"?q= "строка"

@app.get ('/user/{pk}/items/{item}')
def get_user_item(pk: int, item: str):
    return {'user':pk, 'item': item }


@app.post('/book')
def createbook(item: Book):
    return item