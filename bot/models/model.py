from typing import List

from sqlalchemy import BigInteger, String, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from Basemodel import Base

class User(Base):
    """
    Таблица users хранит данные о пользователях Telegram
    """
    __tablename__ = 'users'
    telegram_id : Mapped[int] = mapped_column(BigInteger,primary_kay = True )
    first_name: Mapped[str] = mapped_column(String(50),nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    username: Mapped[str] = mapped_column(String(50),nullable=False)
    # один юз имеет несклько связь с заявками
    applications: Mapped[List['Application']] = relationship(back_populates='user')

class Service(Base):
    """
    Таблица services содержит информацию об услугах,
    """
    __tablename__ = 'service'

    service_id : Mapped[int] = mapped_column(Integer,primary_kay = True,autoincrement=True)
    service_name: Mapped[str] = mapped_column(String(40),nullable = False)

    applications: Mapped[list["Application"]] = relationship(back_populates="service")

class Master(Base):
    __tablename__ = 'masters'
    master_id:Mapped[int] = mapped_column(Integer,primary_kay = True,autoincrement=True)
    master_name: Mapped[str] = mapped_column(String(50),nullable = False)
    # один мастер может иметь несколько заявок
    applications: Mapped[List['Application']] = relationship(back_populates='master')



class Application(Base):
    __tablename__ = 'applications'
    id: Mapped[int] = mapped_column(Integer,primary_kay = True,autoincrement=True)
    client_name: Mapped[str] = mapped_column(String(40),nullable = False)
    appointment_date: Mapped[Date] = mapped_column(Date, nullable=False)
    appointment_time: Mapped[Time] = mapped_column(Time, nullable=False)
    # связи
    user_id: Mapped[int] = mapped_column(BigInteger,ForeignKey('users.telegram_id'))
    master_id: Mapped[int] = mapped_column(Integer, ForeignKey('masters.master_id'))  # Внешний ключ на мастера
    service_id: Mapped[int] = mapped_column(Integer, ForeignKey('services.service_id'))  # Внешний ключ на услугу

    user: Mapped["User"] = relationship(back_populates="applications")
    master: Mapped["Master"] = relationship(back_populates="applications")
    service: Mapped["Service"] = relationship(back_populates="applications")