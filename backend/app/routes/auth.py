"""
Authentication routes
"""
from fastapi import APIRouter
from ..models.user import LoginRequest, LoginResponse
from ..utils.mock_auth import create_mock_user, create_mock_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    if not request.username.strip() or not request.password.strip():
        return LoginResponse(success=False, message="Username and password are required")
    user = create_mock_user(username=request.username.strip(), email=f"{request.username.strip()}@example.com")
    token = create_mock_token(user.id)
    return LoginResponse(success=True, user=user, token=token, message="Login successful")

@router.post("/logout")
async def logout():
    return {"success": True, "message": "Logged out successfully"}
