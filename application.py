from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define a route
@app.get("/")
def home():
    return {"message": "Hello, World!"}
