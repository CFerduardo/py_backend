from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():               #Siempre que llamamos al servidor la operacion que se ejecuta tiene que ser asyncrona 
    return "Hello World"

@app.get("/url")
async def url():
    return {"message": "Hello World"}

#Documentación interactiva de la API (URL/docs)
#Documentación interactiva de la API (URL/redoc)