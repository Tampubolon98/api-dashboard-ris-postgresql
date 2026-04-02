# app/main.py
import json
import hmac
import hashlib
import asyncio
from fastapi import FastAPI, Request, Depends, Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db, engine, Base
from app.config import settings
from routes import tax, employee, supplier
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables if they don't exist
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        pass

@app.get("/")
async def root():
    return {"message": "API Dashboard is running"}

app.include_router(tax.router)
app.include_router(employee.router, tags=["employee"])
app.include_router(supplier.router, tags=["supplier"])