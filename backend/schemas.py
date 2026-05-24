from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    rating: Optional[float] = None
    review: Optional[str] = None

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    rating: Optional[float]
    review: Optional[str]
    
    class Config:
        from_attributes = True