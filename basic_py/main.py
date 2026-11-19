from fastapi import FastAPI

app = FastAPI()

@app.get("/")       # route decorator
def hello():        # function
    return {'message':'Hello my name is ANSHUL'}    # logic inside function


@app.get("/about")
def about():
    return {'message':'Welcome to my worlds where I have started learning fastapi'}