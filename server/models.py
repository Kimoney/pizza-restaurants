from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db=SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    serialize_rules = ('-restaurantspizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurantspizzas = db.relationship('RestaurantPizza', backref='restaurant')
    pizzas = association_proxy('restaurantspizzas', 'pizza',
                               creator=lambda pizza_obj: RestaurantPizza(pizza=pizza_obj))
    
    @validates('name')
    def validate_name(self, key, name):
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters.")
        return name

    def __repr__(self):
        return f"<Restaurant {self.id}: {self.name} at {self.address}>"
    
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    serialize_rules = ('-restaurantspizzas.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingridients = db.Column(db.String, nullable=False)

    restaurantspizzas = db.relationship('RestaurantPizza', backref='pizza')
    restaurants = association_proxy('restaurantspizzas', 'restaurant',
                                    creator = lambda restaurant_obj: RestaurantPizza(restaurant=restaurant_obj))

    def __repr__(self):
        return f"<Pizza {self.id}: {self.name} made with {self.ingridients}>"
    
class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurantspizzas'
    serialize_rules = ('-restaurant.reviews', '-pizza.reviews',)

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    @validates('price')
    def validate_price(self, key, price):
        price = int(price)
        if not 1 <= price <= 30:
            raise ValueError("Price must be between 1 and 30.")
        return price
    
    def __repr__(self):
        return f"<Restaurant Pizza {self.id}: {self.price}>"