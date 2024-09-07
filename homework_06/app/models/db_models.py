from sqlalchemy import Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
import datetime

from main import db


class EducationProductModel(db.Model):
    __tablename__ = 'e_products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ep_name: Mapped[str] = mapped_column(String(150), nullable=False)
    ep_duration: Mapped[int] = mapped_column(Integer, nullable=False)
    ep_price: Mapped[int] = mapped_column(Integer)
    ep_createDate: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, ep_name, ep_duration, ep_price):
        self.ep_name = ep_name
        self.ep_duration = ep_duration
        self.ep_price = ep_price

    def __str__(self):
        return self.ep_name

    def __repr__(self):
        return self.__str__()