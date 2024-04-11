# Pizza Restaurants.
## Introduction
This API provides endpoints to manage restaurants and pizzas. It allows users to retrieve information about restaurants and pizzas, add new restaurant-pizza associations, and delete restaurants.
## Dependencies
- Flask
- Flask-Migrate
- Flask-SQLAlchemy
- Werkzeug
- SQLAlchemy Serializer
- Faker
## Setup and Installation
1. Clone the repository
2. Navigate to the project directory `cd pizza-restaurants`
3. Create environment and install dependencies `pipenv install && pipenv shell`
4. Set up the database
    - `cd server`
    - `flask db init`
    - `flask db migrate -m "First Migration"`
    - `flask db upgrade head`
    - Test and populate database with tests data `python seed.py`
5. Start the Flask Server using `flask run` or `python app.py`
## Endpoints
### GET /restaurants
Returns a list of all restaurants.
## Request
`GET /restaurants`
## Response
```json
[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5th Avenue"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
]
```
### GET /restaurants/:id
Returns details of a specific restaurant by ID.
## Request
`GET /restaurants/1`
## Response
```json
{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}
```
## DELETE /restaurants/:id
Deletes a restaurant by ID.
## Request
`DELETE /restaurants/1`
## Response
```json
{}
```
## GET /pizzas
Returns a list of all pizza
## Request
`GET /pizzas`
## Response
```json
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
```
## POST /restaurant_pizzas
Creates a new restaurant-pizza association.
## Request
`POST /restaurant_pizzas`
## Response
```json
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
```
## Contributions and Pull Requests
Contributions to the Pizza Restaurant API are welcome! If you find any bugs, have feature requests, or want to contribute improvements, please feel free to open an issue or submit a pull request.
## License
MIT LICENSE
## Author
#### John Kimani M.