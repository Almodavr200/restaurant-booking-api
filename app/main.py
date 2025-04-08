from fastapi import FastAPI
from app.routers import table_router, reservation_router

app = FastAPI()

app.include_router(table_router.router, prefix="/tables", tags=["Tables"])
app.include_router(reservation_router.router, prefix="/reservations", tags=["Reservations"])
