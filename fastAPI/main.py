from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():               #Siempre que llamamos al servidor la operacion que se ejecuta tiene que ser asyncrona 
    return "Hello World"

@app.get("/url")
async def url():
    return {"message": "Hello World"}

#Iniciar el server = uvicorn main:app --reload 
#Detener el server CTRL + c

#Documentación interactiva de la API (URL/docs)
#Documentación interactiva de la API (URL/redoc)


#POST: crear datos
#GET: leer datos
#PUT: actualizar datos
#DELETE: borrar datos


#@app.post()
#@app.put()
#@app.delete()
#@app.options()
#@app.head()
#@app.patch()
#@app.trace()