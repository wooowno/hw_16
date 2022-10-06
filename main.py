from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hw_16.db"
db = SQLAlchemy(app)


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))


class Executor(db.Model):
    __tablename__ = "executors"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(500))
    start_date = db.Column(db.String(100))
    end_date = db.Column(db.String(100))
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("executors.id"))

    customer = db.relationship("Customer")
    executor = db.relationship("Executor")


class Offer(db.Model):
    __tablename__ = "offers"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("executors.id"))

    order = db.relationship("Order")
    executor = db.relationship("Executor")


@app.route("/customers")
def customers_page():
    customers = []

    for customer in Customer.query.all():
        customers.append(
            {
                "id": customer.id,
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "age": customer.age,
                "email": customer.email,
                "phone": customer.phone
            }
        )

    return jsonify(customers)


@app.route("/customers/<int:id>")
def customer_page(id):
    customer = Customer.query.get(id)

    return jsonify(
        {
            "id": customer.id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "age": customer.age,
            "email": customer.email,
            "phone": customer.phone
        }
    )


@app.route("/executors")
def executors_page():
    executors = []

    for executor in Executor.query.all():
        executors.append(
            {
                "id": executor.id,
                "first_name": executor.first_name,
                "last_name": executor.last_name,
                "age": executor.age,
                "email": executor.email,
                "phone": executor.phone
            }
        )

    return jsonify(executors)


@app.route("/executors/<int:id>")
def executor_page(id):
    executor = Executor.query.get(id)

    return jsonify(
        {
            "id": executor.id,
            "first_name": executor.first_name,
            "last_name": executor.last_name,
            "age": executor.age,
            "email": executor.email,
            "phone": executor.phone
        }
    )


@app.route("/orders")
def orders_page():
    orders = []

    for order in Order.query.all():
        orders.append(
            {
                "id": order.id,
                "name": order.name,
                "description": order.description,
                "start_date": order.start_date,
                "end_date": order.end_date,
                "address": order.address,
                "price": order.price,
                "customer_id": order.customer_id,
                "executor_id": order.executor_id
            }
        )

    return jsonify(orders)


@app.route("/orders/<int:id>")
def order_page(id):
    order = Order.query.get(id)

    return jsonify(
        {
            "id": order.id,
            "name": order.name,
            "description": order.description,
            "start_date": order.start_date,
            "end_date": order.end_date,
            "address": order.address,
            "price": order.price,
            "customer_id": order.customer_id,
            "executor_id": order.executor_id
        }
    )


@app.route("/offers")
def offers_page():
    offers = []

    for offer in Offer.query.all():
        offers.append(
            {
                "id": offer.id,
                "order_id": offer.order_id,
                "executor_id": offer.executor_id
            }
        )

    return jsonify(offers)


@app.route("/offers/<int:id>")
def offer_page(id):
    offer = Offer.query.get(id)

    return jsonify(
        {
            "id": offer.id,
            "order_id": offer.order_id,
            "executor_id": offer.executor_id
        }
    )


@app.route("/customers", methods=['POST'])
def add_customer_page():
    customer = Customer(
        id=request.json.get("id"),
        first_name=request.json.get("first_name"),
        last_name=request.json.get("last_name"),
        age=request.json.get("age"),
        email=request.json.get("email"),
        phone=request.json.get("phone")
    )

    with db.session.begin():
        db.session.add(customer)

    return "Customer added"


@app.route("/customers/<int:id>", methods=['PUT'])
def update_customer_page(id):
    customer = Customer.query.get(id)
    customer.id = request.json.get("id")
    customer.first_name = request.json.get("first_name")
    customer.last_name = request.json.get("last_name")
    customer.age = request.json.get("age")
    customer.email = request.json.get("email")
    customer.phone = request.json.get("phone")

    with db.session.begin():
        db.session.add(customer)

    return "Customer updated"


@app.route("/customers/<int:id>", methods=['DELETE'])
def delete_customer_page(id):
    customer = Customer.query.get(id)

    with db.session.begin():
        db.session.delete(customer)

    return "Customer deleted"


@app.route("/executors", methods=['POST'])
def add_executor_page():
    executor = Executor(
        id=request.json.get("id"),
        first_name=request.json.get("first_name"),
        last_name=request.json.get("last_name"),
        age=request.json.get("age"),
        email=request.json.get("email"),
        phone=request.json.get("phone")
    )

    with db.session.begin():
        db.session.add(executor)

    return "Executor added"


@app.route("/executors/<int:id>", methods=['PUT'])
def update_executor_page(id):
    executor = Executor.query.get(id)
    executor.id = request.json.get("id")
    executor.first_name = request.json.get("first_name")
    executor.last_name = request.json.get("last_name")
    executor.age = request.json.get("age")
    executor.email = request.json.get("email")
    executor.phone = request.json.get("phone")

    with db.session.begin():
        db.session.add(executor)

    return "Executor updated"


@app.route("/executors/<int:id>", methods=['DELETE'])
def delete_executor_page(id):
    executor = Executor.query.get(id)

    with db.session.begin():
        db.session.delete(executor)

    return "Executor deleted"


@app.route("/orders", methods=['POST'])
def add_order_page():
    order = Order(
        id=request.json.get("id"),
        name=request.json.get("name"),
        description=request.json.get("description"),
        start_date=request.json.get("start_date"),
        end_date=request.json.get("end_date"),
        address=request.json.get("address"),
        price=request.json.get("price"),
        customer=Customer.query.get(request.json.get("customer_id")),
        executor=Executor.query.get(request.json.get("executor_id"))
    )

    with db.session.begin():
        db.session.add(order)

    return "Order added"


@app.route("/orders/<int:id>", methods=['PUT'])
def update_order_page(id):
    order = Order.query.get(id)
    order.id = request.json.get("id")
    order.name = request.json.get("name")
    order.description = request.json.get("description")
    order.start_date = request.json.get("start_date")
    order.end_date = request.json.get("end_date")
    order.address = request.json.get("address")
    order.price = request.json.get("price")
    order.customer = Customer.query.get(request.json.get("customer_id"))
    order.executor = Executor.query.get(request.json.get("executor_id"))

    with db.session.begin():
        db.session.add(order)

    return "Order updated"


@app.route("/orders/<int:id>", methods=['DELETE'])
def delete_order_page(id):
    order = Order.query.get(id)

    with db.session.begin():
        db.session.delete(order)

    return "Order deleted"


@app.route("/offers", methods=['POST'])
def add_offer_page():
    offer = Offer(
        id=request.json.get("id"),
        order=Order.query.get(request.json.get("order_id")),
        executor=Executor.query.get(request.json.get("executor_id"))
    )

    with db.session.begin():
        db.session.add(offer)

    return "Offer added"


@app.route("/offers/<int:id>", methods=['PUT'])
def update_offer_page(id):
    offer = Offer.query.get(id)
    offer.id = request.json.get("id")
    offer.order = Order.query.get(request.json.get("order_id"))
    offer.executor = Executor.query.get(request.json.get("executor_id"))

    with db.session.begin():
        db.session.add(offer)

    return "Offer updated"


@app.route("/offers/<int:id>", methods=['DELETE'])
def delete_offer_page(id):
    offer = Offer.query.get(id)

    with db.session.begin():
        db.session.delete(offer)

    return "Offer deleted"


if __name__ == "__main__":
    app.run()
