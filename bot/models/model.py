from typing import List

from sqlalchemy import BigInteger, String, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from bot.models.Basemodel import Base


class User(Base):
    __tablename__ = 'users'
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    applications: Mapped['Application'] = relationship(back_populates='user')
    profile = relationship("Profile", back_populates="user", uselist=False)

class Profile(Base):
    __tablename__ = 'profile'
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    user = relationship("User", back_populates="profile")

class Service(Base):
    __tablename__ = 'services'
    service_name: Mapped[str] = mapped_column(String(40), nullable=False)
    applications: Mapped[list["Application"]] = relationship(back_populates="service")

class Master(Base):
    __tablename__ = 'masters'
    master_id: Mapped[int] = mapped_column(Integer, unique=True)
    master_name: Mapped[str] = mapped_column(String(50), nullable=False)
    applications: Mapped[List['Application']] = relationship(back_populates='master')

class Application(Base):
    __tablename__ = 'applications'
    client_name: Mapped[str] = mapped_column(String(40), nullable=False)
    appointment_date: Mapped[Date] = mapped_column(Date, nullable=False)
    appointment_time: Mapped[Time] = mapped_column(Time, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    master_id: Mapped[int] = mapped_column(Integer, ForeignKey('masters.id'))
    service_id: Mapped[int] = mapped_column(Integer, ForeignKey('services.id'))

    user: Mapped["User"] = relationship(back_populates="applications")
    master: Mapped["Master"] = relationship(back_populates="applications")
    service: Mapped["Service"] = relationship(back_populates="applications")
