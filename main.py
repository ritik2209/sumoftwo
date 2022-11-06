# Importing Necessary modules
from fastapi import FastAPI
import uvicorn
# Declaring our FastAPI instance
app = FastAPI()
 
# Defining path operation for root endpoint
@app.post('/')
def sum(number1:int, number2:int):
    return {'Sum': number1+number2}
 
