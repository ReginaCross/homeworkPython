from typing import Optional, List
from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    """Модель для создания проекта."""
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    is_active: Optional[bool] = True
    
    class Config:
        extra = "forbid"  


class ProjectUpdate(BaseModel):
    """Модель для обновления проекта."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    is_active: Optional[bool] = None
    
    class Config:
        extra = "forbid"  


class ProjectResponse(BaseModel):
    """Модель ответа проекта."""
    id: int
    name: str
    description: Optional[str]
    is_active: bool
    created_at: str
    updated_at: str