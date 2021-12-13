from fastapi import APIRouter

from app.api.api_v1.endpoints import grocery_stores, invoice

api_router = APIRouter()
api_router.include_router(
    grocery_stores.router, prefix="/grocery-stores", tags=["grocery-stores"]
)
api_router.include_router(invoice.router, prefix="/invoice", tags=["invoice"])
