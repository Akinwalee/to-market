from .models import db, Users, Farmers, Buyers, Admins
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    #createuser() - creates the user model in the database 
    def __init__(self, user_id, email, first_name, last_name, password, phone_number, admin, buyer, farmer):
        self.user_id = user_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.phone_number = phone_number

    def hash_password(self, password):
        password_hash = generate_password_hash(password)
        return password_hash

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

    def register_user(self):
        if Users.query.filter_by(email=self.email).first():
            return {"message": "Email already exists"}
        user = Users(
            user_id=self.user_id, 
            email=self.email, 
            first_name=self.first_name, 
            last_name=self.last_name, 
            password=self.hash_password(self.password), 
            phone_number=self.phone_number
        )
        db.session.add(user)
        db.session.commit()
        return {"message": "User registered successfully"}
    
    def register_buyer(self, user_id, cart_id=None, shipping_address=None):
        buyer = Buyers(buyer_id=user_id, cart_id=cart_id, shipping_address=shipping_address)
        db.session.add(buyer)
        db.session.commit()
        return {"message": "Buyer registered successfully"}
    
    def register_farmer(self, user_id, farm_name, farm_description):
        farmer = Farmers(farm_id=user_id, farm_name=farm_name, farm_description=farm_description)
        db.session.add(farmer)
        db.session.commit()
        return {"message": "Farmer registered successfully"}
    
    def register_admin(self, user_id):
        admin = Admins(admin_id=user_id)
        db.session.add(admin)
        db.session.commit()
        return {"message": "Admin registered successfully"}
    
    def login(self):
        user = Users.query.filter_by(email=self.email).first()
        if user and self.check_password(self.password):
            return {"message": "User logged in successfully"}
        else:
            return {"message": "Invalid email or password"}
        
    def check_profile(self):
        user = Users.query.filter_by(email=self.email).first()
        if user:
            return {
                "user_id": user.user_id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
                "admin": bool(user.admin),
                "buyer": bool(user.buyer),
                "farmer": bool(user.farmer)
            }
        else:
            return {"message": "User not found"}
        
    def update_profile(self, first_name=None, last_name=None, phone_number=None):
        user = Users.query.filter_by(email=self.email).first()
        if user:
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if phone_number:
                user.phone_number = phone_number
            db.session.commit()
            return {"message": "Profile updated successfully"}
        else:
            return {"message": "User not found"}
        

    