from fastapi import FastAPI
from pydantic import BaseModel                  #Definir modelos de datos que serán utilizados para validar y serializar datos en tu aplicación

app = FastAPI()

#Entidad user                   (Se toma como plantilla para crear los usuarios)
class User(BaseModel):
    id: int
    name:str
    lastName: str
    age: int

#Si se posee un obj que implemente el comportamiento de BaseModel, podemos manejarlo como si fuera un json 
users_list = [User(id=1, name="carlos", lastName="silva",age=25),
        User(id=2, name="camila", lastName="silva", age=4),
        User(id=3, name="mariolga", lastName="blanco", age=31),
        User(id=4, name="kembert", lastName="nieves", age=30)]

@app.get("/user")
async def usersJSON():
    return [{"name":"carlos", "lastName":"silva", "age":25},
            {"name":"camila", "lastName":"silva", "age":4},
            {"name":"mariolga", "lastName":"blanco", "age":31}]


@app.get("/userclass")
async def users():
    return User(id=5, name="jorge", lastName="ferreira", age=30)


@app.get("/userlist")
async def users():
    return users_list


#PATH
@app.get("/userpath/{id}")          #Para capturar parametros {}
async def users(id:int):              #Nombre del parametro : el tipado del tipo de dato
    return searc_user(id)


#QUERY          LLamar a un parametro por query, podemos empezar a igualar una clave a un valor dentro de la url        Sintaxis(http://url/?id=1.2.3...si quisieramos concatenar con str u otro parametro usamos & http://url/?id=1&name=carlos) 
@app.get("/userquery/")
async def users(id:int):
    return searc_user(id)

def searc_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No Se Ha Encontrado Usuario"}         #Capturar un error en un json                    

