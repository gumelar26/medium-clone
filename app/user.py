from sqlmodel import Session, select

from database.model import engine, User

def get_user(username : str):
    with Session(engine) as session:
        users = session.exec(
            select(User).where(User.username == username)
            ).first()
        print(users)
        return users

def update_user(username: str):
    with Session(engine) as session:
        users = session.exec(
            select(User).where(User.username == username)
        ).one()
        
        users.password= "secret"
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