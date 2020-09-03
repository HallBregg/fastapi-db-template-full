from fastapi import APIRouter

from linkorage.app.api.v1.endpoints import one


api_router = APIRouter()
api_router.include_router(one.router, prefix='/one', tags=['one'])
