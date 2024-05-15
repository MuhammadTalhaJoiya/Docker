from fastapi import FastAPI

app=FastAPI()
@app.get("/")
def Hello():
    return {"ALI":"Talha"}