from sqlmodel import Session

from database.model import User, engine

def user():
    user = User(
        email="gumelar@dev.id",
        username="gumelar",
        password="secret123"
    )
    
    with Session(engine) as session:
        session.add(user)
        session.commit()

def main():
    user()

if __name__ == "__main__" :
    main()