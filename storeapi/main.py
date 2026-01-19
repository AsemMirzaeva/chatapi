from fastapi import FastAPI

from storeapi.routers.post import router as post_router

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello, world!"}

app.include_router(post_router)

