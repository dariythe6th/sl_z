from sqlalchemy import Float
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    cash = Column(Integer)
    data = Column(String)
    users_shares = relationship("cars", backref="Users")


class cars(Base):
    __tablename__ = 'Cars'
    id = Column(Integer, primary_key=True)
    mark = Column(String)
    price = Column(Integer)
    meleage = Column(Float)
    model = Column(String)
    user_id = Column(Integer, ForeignKey("User.id"))


if __name__ == "_main_":
    engine = create_engine('sqlite:///relatio.db', echo=False)
    Base.metadata.create_all(engine)
    sessionmaker = sessionmaker(bind=engine)
    with sessionmaker.begin() as s:
        u1 = Users(name="Alice", surname="Sur", cash=100, data="26.11.2005")
        b1 = cars(mark="Apple", price=100, meleage=15.5, model="192")
        u1.users_shares.append(b1)
        s.add_all([u1, b1])
        s.commit()