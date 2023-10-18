"""Schemas for Stock API"""
from pydantic import BaseModel,Field



class StockSchema(BaseModel):
    name: str = Field(max_length=20)
    price: int = Field(gt=0) #Greater than
    code: str = Field(max_length=7)