from fastapi import FastAPI, HTTPException

from user import get_user, update_user as crud_update_user, delete_user as crud_delete_user
from database.schemas import UserGet, UserUpdate

app = FastAPI()

@app.get("/api/user", response_model=UserGet)
async def get_current_user():
  user = get_user("agam")
  if user is None :
    raise HTTPException(status_code=404, detail="User not found")
  return user

@app.put("/api/user")
async def update_user(
  userSchema: UserUpdate
):
  crud_update_user(username="andiuntung", userSchema=userSchema)
  return {"status": 200}

@app.delete("/api/user")
async def delete_user():
  crud_delete_user(username="andiuntung")
  return {"status": 200}