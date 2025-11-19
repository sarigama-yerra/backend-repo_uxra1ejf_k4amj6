"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List
from datetime import date

# Existing example schemas remain for reference
class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# DePIN Projects schema (primary for this app)
class DePINProject(BaseModel):
    """
    Decentralized Physical Infrastructure (DePIN) projects
    Collection name: "depinproject"
    """
    name: str = Field(..., description="Project name")
    description: Optional[str] = Field(None, description="Short description of the project")
    category: str = Field(..., description="Category e.g., Compute, Storage, Wireless, Mapping, Sensors, Bandwidth")
    network: Optional[str] = Field(None, description="Primary blockchain/network used")
    token: Optional[str] = Field(None, description="Token symbol if applicable")
    status: Optional[str] = Field("live", description="live | testnet | building | paused")
    website: Optional[HttpUrl] = Field(None, description="Official website")
    twitter: Optional[HttpUrl] = Field(None, description="Twitter/X URL")
    github: Optional[HttpUrl] = Field(None, description="GitHub URL")
    image_url: Optional[HttpUrl] = Field(None, description="Logo or cover image URL")
    launch_date: Optional[date] = Field(None, description="Launch or genesis date")
    region: Optional[str] = Field(None, description="Primary region or global")
    tags: List[str] = Field(default_factory=list, description="Additional tags/attributes")
    tvl_usd: Optional[float] = Field(None, ge=0, description="Total value locked or similar metric in USD")
    market_cap_usd: Optional[float] = Field(None, ge=0, description="Market capitalization in USD")
