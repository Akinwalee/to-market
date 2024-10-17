from . import db

class Users(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    phone_number = db.Column(db.String(200))

    admin = db.relationship('Admins', uselist=False, backref='user')
    buyer = db.relationship('Buyers', uselist=False, backref='user')
    farner = db.relationship('Farmers', uselist=False, backref='user')

class Admins(db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)

class Buyers(db.Model):
    __tablename__ = 'buyer'
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'))
    shipping_address = db.Column(db.String(100))

    cart = db.relationship('Carts', uselist=False, backref='buyer')

class Farmers(db.Model):
    __tablename__ = 'farmer'
    farmer_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    farm_name = db.Column(db.String(100))
    farm_description = db.Column(db.String(100))

    products = db.relationship('Products', backref='farmer')

class Products(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(120))
    price = db.Column(db.Float)
    stock_quantity = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.farmer_id'))

    category = db.relationship('Categories', backref='products')
    reviews = db.relationship('Reviews', backref='product')

class Categories(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Carts(db.Model):
    __tablename__ = 'cart'
    cart_id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyer.buyer_id'))

    cart_items = db.relationship('CartItems', backref='cart')

class CartItems(db.Model):
    __tablename__ = 'cart_item'
    quantity = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'))

class Orders(db.Model):
    __tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyer.buyer_id'))
    order_date = db.Column(db.DateTime(timezone=True))
    status = db.Column(db.String(50))
    total_amount = db.Column(db.Float)

    order_items = db.relationship('OrderItems', backref='order')

class OrderItems(db.Model):
    __tablename__ = 'order_item'
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), primary_key=True)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))

class Payments(db.Model):
    __tablename__ = 'payment'
    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    amount = db.Column(db.Float)
    payment_method = db.Column(db.String(100))
    status = db.Column(db.String(100))

class Reviews(db.Model):
    __tablename__ = 'review'
    review_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    rating = db.Column(db.Float)
    comment = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True))

    user = db.relationship('Users', backref='reviews')