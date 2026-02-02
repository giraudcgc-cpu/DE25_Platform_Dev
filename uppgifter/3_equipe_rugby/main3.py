from fastapi import FastAPI

app = FastAPI("equipe_rugby")

@app.get("/")
def equipe_rugby():
    return {"equipe":"France"}