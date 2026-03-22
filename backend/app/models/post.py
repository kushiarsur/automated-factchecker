"""
Post and Comment models
"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Comment(BaseModel):
    id: str
    post_id: str
    user_id: str
    username: str
    avatar_url: Optional[str] = None
    content: str
    created_at: datetime = datetime.now()
    likes: int = 0

class Post(BaseModel):
    id: str
    user_id: str
    username: str
    avatar_url: Optional[str] = None
    caption: str
    image_url: Optional[str] = None
    created_at: datetime = datetime.now()
    likes: int = 0
    comments_count: int = 0
    shares: int = 0
    saves: int = 0
    comments: List[Comment] = []

class CreatePostRequest(BaseModel):
    caption: str
    image_url: Optional[str] = None

class CreateCommentRequest(BaseModel):
    content: str
