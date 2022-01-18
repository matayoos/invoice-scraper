from fastapi import APIRouter

from app.api.api_v1.endpoints import grocery_stores, invoice, category

api_router = APIRouter()
api_router.include_router(
    grocery_stores.router, prefix="/grocery-stores", tags=["Grocery Stores"]
)
api_router.include_router(invoice.router, prefix="/invoice", tags=["Invoice"])
api_router.include_router(category.router, prefix="/category", tags=["Category"])
