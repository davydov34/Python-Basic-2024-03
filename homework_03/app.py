from fastapi import FastAPI
from view.ping import router as ping_router

app = FastAPI()
app.include_router(ping_router)

@app.get("/")
def root_page():
    return {"message": "OTUS HomeWork 19!"}

