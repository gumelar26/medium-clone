from fastapi import FastAPI, HTTPException

from user import get_user
from database.schemas import UserGet, UserUpdate

app = FastAPI()

@app.get("/api/user", response_model=UserGet)
async def get_current_user():
  user = get_user("agam")
  if user is None :
    raise HTTPException(status_code=404, detail="User not found")
  return user

# @app.put("/api/user", response_model=UserUpdate)
# async def update_user():
  