from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, order_detail: schemas.OrderDetailCreate):
    #Create a new instance of the Order Details model
    try:

        db_detail = models.OrderDetail(**order_detail.model_dump())
        db.add(db_detail)
        db.commit()
        db.refresh(db_detail)
        return db_detail
    except ValueError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid order_id or sandwich_id")


def read_all(db: Session):
    data = db.query(models.OrderDetail).all()
    return [
        {
            "order_id": item.order_id,
            "ingredient_name": item.ingredient_name,
            "quantity": item.quantity
        }
        for item in data
    ]


def read_one(db: Session, order_detail_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()


def update(db: Session, order_detail_id, order_details):
    db_order_details = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    if not db_order_details.first():
        raise HTTPException(status_code=404, detail="Order Details not found")
    update_data = order_details.model_dump(exclude_unset=True)
    db_order_details.update(update_data, synchronize_session=False)
    db.commit()
    return db_order_details.first()


def delete(db: Session, order_detail_id):
    db_order_details = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    if not db_order_details.first():
        raise HTTPException(status_code=404, detail="Order Details not found")
    db_order_details.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)