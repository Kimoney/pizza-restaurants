from models import db, Restaurant, Pizza, RestaurantPizza
from app import app

with app.app_context():

    # Delete All Rows To Work On A Clean Slate
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    # Populate restaurants table
    rest1 = Restaurant(name="Hotel 1", address="Nairobi. Kenya")
    db.session.add(rest1)
    db.session.commit()

    # Populate pizzas table
    pizza1 = Pizza(name='Peperoni', ingridients="Flour, Chicken, ma Zaga Zaga")
    db.session.add(pizza1)
    db.session.commit()
    
    # Populate restaurantspizzas table
    restpizza1 = RestaurantPizza(price=1200, restaurant_id=1, pizza_id=1)
    db.session.add(restpizza1)
    db.session.commit()