from sqlmodel import Session, select

from database.model import engine, User

def get_user():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        print(users)

def main():
    get_user()
    
if __name__ == "__main__" :
    main()