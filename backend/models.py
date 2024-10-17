from . import db

class Users(db.Model):
    __tablename__ = 'user'
    _user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    phone_number = db.Column(db.String(200))

class Admins(db.Model):
    __tablename__ = 'admins'
    _admin_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

class Buyers(db.Model):
    __tablename__ = 'buyers'
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.cart_id'))
    shipping_address = db.Column(db.String(100))

class Farmers(db.Model):
    __tablename__ = 'farmers'
    farmer_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    farm_name = db.Column(db.String(100))
    farm_description = db.Column(db.String(100))

class Products(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(120))
    price = db.Column(db.Float)
    stock_quantity = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))

class Categorys(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Carts(db.Model):
    __tablename__ = 'carts'
    cart_id = db.Column(db.Integer, db.ForeignKey('buyers.buyer_id'), primary_key=True)
    cart_items = db.relationship('CartItems', backref='carts')

class CartItems(db.Model):
    __tablename__ = 'cart_items'
    quantity = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.cart_id'))

class Orders(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyers.buyer_id'))
    order_date = db.Column(db.DateTime(timezone))
    status = db.Column(db.String(101))
    total_amount = db.Column(db.Float)

class OrderItems(db.Model):
    __tablename__ = 'order_items'
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))

class Payments(db.Model):
    __tablename__ = 'payments'
    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    amount = db.Column(db.Float)
    payment_method = db.Column(db.String(100))
    status = db.Column(db.String(100))

class Reviews(db.Models):
    __tablename__ = 'reviews'
    review_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    rating = db.Column(db.Float)
    comment = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True))