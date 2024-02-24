from sqlmodel import Session, select
from fastapi import HTTPException

from database.model import engine, User
from database.schemas import UserUpdate

def get_user(username : str):
    with Session(engine) as session:
        users = session.exec(
            select(User).where(User.username == username)
            ).first()
        print(users)
        return users

def update_user(username: str, userSchema: UserUpdate):
    with Session(engine) as session:
        users = session.exec(
            select(User).where(User.username == username)
        ).one()
        
        if users is None:
            raise HTTPException(status_code=404, detail="Can't update data")
        
        users.username = userSchema.username
        users.email = userSchema.email
        users.token = userSchema.token
        users.modified_at = userSchema.modified_at
        users.status = userSchema.status
        
        session.add(users)
        session.commit()
        session.refresh(users)

def delete_user(username: str):
    with Session(engine) as session:
        users = session.exec(
            select(User).where(User.username == username)
        ).one()
        
        session.delete(users)
        session.commit()

def main():
    # # get_user("agam")
    # update_user("gumelar")
    delete_user("gumelar")
    
if __name__ == "__main__" :
    main()