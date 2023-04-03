"""Pydantic Schemas for Urls"""
from pydantic import BaseModel, AnyUrl, Field


class UrlData(BaseModel):
    """Pydantic class for Url data"""
    url: AnyUrl = Field(..., example="https://docs.pydantic.dev/")
