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

    restaurantspizzas = db.relationship('RestaurantPizza', back_populates='restaurant')

    def __repr__(self):
        return f"<Restaurant {self.id}: {self.name} at {self.address}>"
    
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingridients = db.Column(db.String, nullable=False)

    restaurantspizzas = db.relationship('RestaurantPizza', back_populates='pizza')

    def __repr__(self):
        return f"<Pizza {self.id}: {self.name} made with {self.ingridients}>"
    
class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurantspizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    # Relationship mapping the RestaurantPizza to related Restaurant
    restaurant = db.relationship('Restaurant', back_populates='restaurantspizzas')

    # Relationship mapping the RestaurantPizza to related Pizza
    pizza = db.relationship('Pizza', back_populates='restaurantspizzas')


    def __repr__(self):
        return f"<Restaurant Pizza {self.id}: {self.price}>"