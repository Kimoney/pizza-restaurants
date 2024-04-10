from models import db, Restaurant, Pizza, RestaurantPizza
from app import app
from faker import Faker

fake = Faker()

with app.app_context():

    # Delete All Rows To Work On A Clean Slate
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    # Populate restaurants table
    for x in range(10):
        restaurant = Restaurant(name=(fake.company() + ' Lounge & Restaurant'), address=fake.address())
        db.session.add(restaurant)
        db.session.commit()

    # Populate pizzas table
    for x in range(25):
        test_ingridients = fake.words(nb=5)
        pizza1 = Pizza(name=fake.language_name(), ingridients=', '.join(test_ingridients))
        db.session.add(pizza1)
        db.session.commit()
    
    # Populate restaurantspizzas table
    for x in range (100):
        restpizza1 = RestaurantPizza(price=fake.random_int(min=1, max=30), restaurant_id=fake.random_int(min=1, max=10), pizza_id=fake.random_int(min=1, max=25))
        db.session.add(restpizza1)
        db.session.commit()