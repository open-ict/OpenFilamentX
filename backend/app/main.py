from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="OpenFilamentX API", version="0.1.0")
app.include_router(router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "OpenFilamentX API running"}
