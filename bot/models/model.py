from sqlalchemy import BigInteger, String, Integer, Date, Time
from sqlalchemy.orm import Mapped
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

class Service(Base):
    """
    Таблица services содержит информацию об услугах,
    """
    __tablename__ = 'service'

    service_id : Mapped[int] = mapped_column(Integer,primary_kay = True,autoincrement=True)
    service_name: Mapped[str] = mapped_column(String(40),nullable = False)

class Master(Base):
    __tablename__ = 'masters'
    master_id:Mapped[int] = mapped_column(Integer,primary_kay = True,autoincrement=True)
    master_name: Mapped[str] = mapped_column(String(50),nullable = False)


class Application(Base):
    __tablename__ = 'applications'
    id: Mapped[int] = mapped_column(Integer,primary_kay = True,autoincrement=True)
    client_name: Mapped[str] = mapped_column(String(40),nullable = False)
    appointment_date: Mapped[Date] = mapped_column(Date, nullable=False)
    appointment_time: Mapped[Time] = mapped_column(Time, nullable=False)