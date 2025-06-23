from typing import List

from sqlalchemy import BigInteger, String, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from bot.models.Basemodel import Base


class User(Base):
    __tablename__ = 'users'
    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    applications: Mapped['Application'] = relationship(back_populates='user')
    # profile = relationship("Profile", back_populates="user", uselist=False)

# class Profile(Base):
#     __tablename__ = 'profile'
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey('users.telegram_id'))
#     first_name: Mapped[str] = mapped_column(String(50), nullable=True)
#     last_name: Mapped[str] = mapped_column(String(50), nullable=True)
#     user = relationship("User", back_populates="profile")



class Service(Base):
    __tablename__ = 'services'
    service_id: Mapped[int] = mapped_column(Integer, primary_key=True,  autoincrement=True)
    service_name: Mapped[str] = mapped_column(String(40), nullable=False)
    applications: Mapped[list["Application"]] = relationship(back_populates="service")

class Master(Base):
    __tablename__ = 'masters'
    master_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    master_name: Mapped[str] = mapped_column(String(50), nullable=False)
    applications: Mapped[List['Application']] = relationship(back_populates='master')

class Application(Base):
    __tablename__ = 'applications'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    client_name: Mapped[str] = mapped_column(String(40), nullable=False)
    client_surname: Mapped[str] = mapped_column(String(40))
    appointment_date: Mapped[Date] = mapped_column(Date, nullable=False)
    appointment_time: Mapped[Time] = mapped_column(Time, nullable=False)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.telegram_id'))
    master_id: Mapped[int] = mapped_column(Integer, ForeignKey('masters.master_id'),nullable=True) # после теста поменять на обязательно
    service_id: Mapped[int] = mapped_column(Integer, ForeignKey('services.service_id'),nullable=True)

    user: Mapped["User"] = relationship(back_populates="applications")
    master: Mapped["Master"] = relationship(back_populates="applications")
    service: Mapped["Service"] = relationship(back_populates="applications")
