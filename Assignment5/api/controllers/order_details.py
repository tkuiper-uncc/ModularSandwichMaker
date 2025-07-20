from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import models, schemas


def create(db: Session, order_detail: schemas.OrderDetailCreate):
    db_order_details = models.OrderDetail(**order_detail.dict())
    db.add(db_order_details)
    db.commit()
    db.refresh(db_order_details)
    return db_order_details


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, order_detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail_id == order_detail_id).first()


def update(db: Session, order_detail_id: int, order_detail: schemas.OrderDetailUpdate):
    db_order_details = db.query(models.OrderDetail).filter(models.OrderDetail_id == order_detail_id)
    if not db_order_details.first():
        raise HTTPException(status_code=404, detail="Order Details not found")
    db_order_details.update(order_detail.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return db_order_details.first()


def delete(db: Session, order_detail_id: int):
    db_order_details = db.query(models.OrderDetail).filter(models.OrderDetail_id == order_detail_id)
    if not db_order_details.first():
        raise HTTPException(status_code=404, detail="Order Details not found")
    db_order_details.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)