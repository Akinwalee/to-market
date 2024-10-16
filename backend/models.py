from . import db

class User(db.Model):
    __tablename__ = 'user'
    _user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    phone_number = db.Column(db.String(200))

class Admin(db.Model):
    __tablename__ = 'admin'
    _user_id = db.Column(db.Integer)

class Buyer(db.Model):
    __tablename__ = 'buyer'
    buyer_id = db.Column(db.Integer)
    cart_id = db.Column(db.Integer)
    shipping_address = db.Column(db.String(100))

class Farmer(db.Model):
    __tablename__ = 'farmer'
    farmer_id = db.Column(db.Integer)
    farm_name = db.Column(db.String(100))
    farm_description = db.Column(db.String(100))

class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(120))
    price = db.Column(db.Float)
    stock_quantity = db.Column(db.Integer)
    category_id = db.Column(db.Integer)

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer)
    name = db.Column(db.String(100))

class Cart(db.Model):
    __tablename__ = 'cart'
    cart_id = db.Column(db.Integer)

class CartItem(db.Model):
    __tablename__ = 'cart_item'
    quantity = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    cart_id = db.Column(db.Integer)

class Order(db.Model):
    __tablename__ = 'order'
    order_id = db.Column(db.Integer)
    buyer_id = db.Column(db.Integer)
    order_date = db.Column(db.Stirng(100))
    status = db.Column(db.String(101))
    total_amount = db.Column(db.Float)

class OrderItem(db.Model):
    __tablename__ = 'order_item'
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    order_id = db.Column(db.Integer)

class Payment(db.Model):
    __tablename__ = 'payment'
    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    amount = db.Column(db.Float)
    payment_method = db.Column(db.String(100))
    status = db.Column(db.String(100))

class Review(db.Models):
    __tablename__ = 'review'
    review_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    rating = db.Column(db.Float)
    comment = db.Column(db.String(500))
    date = db.Column(db.String(100))