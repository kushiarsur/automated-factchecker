"""
Mock authentication utilities for prototype
"""
import uuid
from datetime import datetime
from typing import Optional
from ..models.user import User

# In-memory user storage for prototype
_users_db = {}

def create_mock_user(username: str, email: Optional[str] = None) -> User:
    """Create a mock user for prototype authentication"""
    user_id = str(uuid.uuid4())
    avatar_url = f"https://ui-avatars.com/api/?name={username}&background=9333ea&color=fff"
    user = User(
        id=user_id,
        username=username,
        email=email or f"{username}@example.com",
        avatar_url=avatar_url,
        created_at=datetime.now()
    )
    _users_db[user_id] = user
    return user

def get_user_by_id(user_id: str) -> Optional[User]:
    """Get user by ID"""
    return _users_db.get(user_id)

def create_mock_token(user_id: str) -> str:
    """Create a mock authentication token"""
    return f"mock_token_{user_id}_{uuid.uuid4().hex[:8]}"

def validate_mock_token(token: str) -> Optional[str]:
    """Validate mock token and return user_id"""
    if token and token.startswith("mock_token_"):
        parts = token.split("_")
        if len(parts) >= 3:
            return parts[2]
    return None
