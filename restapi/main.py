from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schema
from .db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/", response_model=schema.User)
async def create_user(user: schema.UserBase, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, user_name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already exist in database")
    return crud.create_user(db, user=user)

@app.get("/api/{user_id}", response_model=schema.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User with that ID does not exist")
    return db_user

@app.put("/api/{user_id}", response_model=schema.User)
def update_user(user_id: int, user: schema.UserBase, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    db_query = db.query(models.User).filter(models.User.id == user_id)
    try:
        if db_query:
            updated_data = user.model_dump()
            db_query.update(updated_data)
            db.commit()
            db.refresh(db_user)
            return db_user
    except Exception as e:
        raise HTTPException(status_code=404, detail="User with Id does not exist")

@app.delete("/api/{user_id}", response_model=schema.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        id_ = db_user.id
        db.delete(db_user)
        db.commit()
        raise HTTPException(status_code=200, detail=f"User with ID {id_} successfully deleted")
    else:
        raise HTTPException(status_code=400, detail="User with Id does not exist")