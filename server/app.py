from flask import Flask
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Pizza Restaurants</h1>'

@app.route('/restaurants')
def restaurants():
    return '<h1>Return JSON data of the Restaurant Model</h1>'

@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurants_by_id(id):
    return '<h1>If the Restaurant exists, return JSON with associated pizzas </h1>'

@app.route('/pizzas')
def pizzas():
    return '<h1>Return JSON data of the Pizza Model</h1>'

@app.route('/restaurant_pizzas')
def restaurant_pizzas():
    return '<h1>This route should create a new RestaurantPizza that is associated with an existing Pizza and Restaurant.</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)