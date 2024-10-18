from flask import jsonify
from models import Categories
from . import db


class Category:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def create_category(self):
        category = Categories.query.filter_by(id=self.id).first()
        if category:
            return jsonify({'message': 'Category already exists'}), 400
        new_category = Categories(name=self.name)
        db.session.add(new_category)
        db.session.commit()
        return jsonify({'message': 'Category created successfully', 'category': new_category.to_json()}), 201
    
    def update_category(self):
        category = Categories.query.filter_by(id=self.id).first()
        if not category:
            return jsonify({'message': 'Category not found'}), 404
        category.name = self.name
        db.session.commit()
        return jsonify({'message': 'Category updated successfully', 'category': category.to_json()}), 200
    
    def delete_category(self):
        category = Categories.query.filter_by(id=self.id).first()
        if not category:
            return jsonify({"message": "Category not found"}), 404
        
        db.session.delete(category)
        db.session.commit()
        return jsonify({"message": "Category deleted successfully"}), 200
    
    
    def get_categories(self):
        categories = Categories.query.all()
        return jsonify([category.to_json() for category in categories]), 200


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }
