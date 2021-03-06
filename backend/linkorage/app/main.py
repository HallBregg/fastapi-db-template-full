import uvicorn
from fastapi import FastAPI

from linkorage.app.api.v1.api import api_router


app = FastAPI()
app.include_router(api_router, prefix='/api/v1')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
