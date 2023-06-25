from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from depends import get_db
from schemas import users as schemas
from models import users as mymodels

router = APIRouter()


@router.post('/users/', response_model=schemas.User)  # create data in DB
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):  # Depends on select session
    db_user = db.query(mymodels.User).filter(mymodels.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail='Email already exists')
    user = mymodels.User(email=user.email, username=user.username, password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get('/users/{user_id}', response_model=schemas.User)  # read data from DB
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(mymodels.User).filter(mymodels.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='user not found')
    return db_user
