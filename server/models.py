from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db=SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Restaurant {self.id}: {self.name} at {self.address}>"
    
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingridients = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Pizza {self.id}: {self.name} made with {self.ingridients}>"
    
class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurantspizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Restaurant Pizza {self.id}: {self.price}>"