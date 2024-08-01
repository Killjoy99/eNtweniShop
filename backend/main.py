from fastapi_offline import FastAPIOffline
from src.api import api_router

app = FastAPIOffline()


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
