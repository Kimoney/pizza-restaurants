from flask import Flask, request, make_response, jsonify
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
    restaurants = []
    for restaurant in Restaurant.query.all():
        rest_dict = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
        restaurants.append(rest_dict)
    resp = make_response(jsonify(restaurants), 200)
    return resp

@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurants_by_id(id):
    if request.method == 'GET':
        restaurant = Restaurant.query.filter(Restaurant.id == id).first()
        if not restaurant:
            resp_dict = {'error': "Restaurant not found!"}
            resp = make_response(jsonify(resp_dict))
            return resp
        else:
            rest_dict = {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address,
                'pizzas': [{
                    'id': pizza.id,
                    'name': pizza.name,
                    'ingridients': pizza.ingridients
                } for pizza in restaurant.pizzas]
            }
            resp = make_response(jsonify(rest_dict), 200)
            return resp
    
    elif request.method == 'DELETE':
        restaurant = Restaurant.query.filter(Restaurant.id == id).first()
        if not restaurant:
            resp_dict = {'error': "Restaurant not found!"}
            resp = make_response(jsonify(resp_dict))
            return resp
        else:
            db.session.delete(restaurant)
            db.session.commit()

            resp_dict = {
                "deletion_success": True,
                "message": "Restaurant Deleted Successfully!"
            }
            resp = make_response(resp_dict, 200)
            return resp

@app.route('/pizzas')
def pizzas():
    pizzas = []
    for pizza in Pizza.query.all():
        pizza_dict = {
            'id': pizza.id,
            'name': pizza.name,
            'ingridients': pizza.ingridients
        }
        pizzas.append(pizza_dict)
    resp = make_response(pizzas, 200)
    return resp

@app.route('/restaurant_pizzas', methods=['POST'])
def restaurant_pizzas():
    if request.method == 'POST':
        try:
            restaurant_pizza = RestaurantPizza(
                price=request.args.get('price'),
                restaurant_id=request.args.get('restaurant_id'),
                pizza_id=request.args.get('pizza_id')
            )
            db.session.add(restaurant_pizza)
            db.session.commit()
            pizza_id=request.args.get('pizza_id')
            pizza = Pizza.query.filter(Pizza.id == pizza_id).first()
            pizza_dict = {
            'id': pizza.id,
            'name': pizza.name,
            'ingridients': pizza.ingridients
            }
            resp = make_response(jsonify(pizza_dict), 200)
            return resp
        except ValueError:
            error_msg = {'errors': ["validation errors"]}
            resp = make_response(jsonify(error_msg), 400)
            return resp


if __name__ == '__main__':
    app.run(port=5555, debug=True)