from models import Products
from flask import jsonify
from models import Categories, Farmers
from . import db
class Product():
    def __init__(self, id, name=None, description=None, price=None, stock_quantity=None, category_id=None, farmer_id=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = stock_quantity
        self.category_id = category_id
        self.farmer_id = farmer_id

    def create_product(self):
        category = Categories.query.filter_by(category_id=self.category_id).first()
        if not category:
            return jsonify({"message": "Category not found"}), 404
        farmer = Farmers.query.filter_by(farmer_id=self.farmer_id).first()
        if not farmer:
            return jsonify({"message": "Farmer not found"}), 404
        product = Products.query.filter_by(product_id=self.id).first()
        if not product:
            return jsonify({"message": "Product not found"}), 404
        new_product = Products(
            name=self.name, 
            description=self.description, 
            price=self.price, 
            stock_quantity=self.stock_quantity, 
            category_id=self.category_id, 
            farmer_id=self.farmer_id
        )
        db.session.add(new_product)
        db.session.commit()

        return jsonify({"message": "Product created successfully"}), 201
    
    def update_product(self):
        category = Categories.query.filter_by(category_id=self.category_id).first()
        if not category:
            return jsonify({"message": "Category not found"}), 404
        farmer = Farmers.query.filter_by(farmer_id=self.farmer_id).first()
        if not farmer:
            return jsonify({"message": "Farmer not found"}), 404
        
        product = Products.query.filter_by(product_id=self.id).first()
        if not product:
            return jsonify({"message": "Product not found"}), 404
        
        if self.name:
            product.name = self.name
            # db.session.commit()
        if self.description:
            product.description = self.description
            # db.session.commit()
        if self.price:
            product.price = self.price
            # db.session.commit()
        if self.stock_quantity:
            if self.stock_quantity < 0:
                return jsonify({"message": "Invalid stock quantity"}), 400
            product.stock_qunatity = self.stock_quantity
            # db.session.commit()
        if self.category_id:
            product.category_id = self.category_id
            # db.session.commit()
        if self.farmer_id:
            product.farmer_id = self.farmer_id
            # db.session.commit()

        db.session.commit()
        return jsonify({"message": "Product updated successfully"}), 200


    
    def delete_product(self):
        product = Products.query.filter_by(product_id=self.id).first()
        if not product:
            return jsonify({"message": "Product not found"}), 404
        db.session.delete(product)
        db.session.commit()

        return jsonify({"message": "Product deleted successfully"}), 200
    
    
    def get_products(self):
        products = Products.query.all()
        result = []
        for product in products:
            category = Categories.query.filter_by(category_id=product.category_id).first()
            farmer = Farmers.query.filter_by(product_id=product.farmer_id).first()
            result.append({
                "id": product.product_id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "stock_qunatity": product.stock_qunatity,
                "category": category.name,
                "farmer": farmer.farm_name
            })
        return jsonify(result), 200
    
    def get_product_by_id(self, product_id):
        product = Products.query.filter_by(product_id=product_id).first()
        if not product:
            return jsonify({"message": "Product not found"}), 404
        category = Categories.query.filter_by(category_id=product.category_id).first()
        if not category:
            return jsonify({"message": "Category not found"}), 404
        farmer = Farmers.query.filter_by(farmer_id=product.farmer_id).first()
        if not farmer:
            return jsonify({"message": "Farmer not found"}), 404
        result = {
            "id": product.product_id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock_qunatity": product.stock_qunatity,
            "category": category.name,
            "farmer": farmer.farm_name
        }
        return jsonify(result), 200
    

