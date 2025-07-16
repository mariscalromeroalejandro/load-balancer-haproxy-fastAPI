from fastapi import FastAPI
import os

app = FastAPI()
instance = os.getenv("INSTANCE_ID", "1")

@app.get("/")
def read_root():
    return {"message": f"Hello from FastAPI instance {instance}"}
