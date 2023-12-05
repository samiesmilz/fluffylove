""" Seed file to pre-fill sample data in tables """
from app import app
from models import db, Pet, User


# create tables
db.drop_all()
db.create_all()

# Sample data for Pet model
pet1 = Pet(name='Coco', species='Dog', photo_url='https://img.freepik.com/free-photo/adorable-chocolate-labrador-retriever-portrait_53876-64833.jpg?w=2000&t=st=1701330895~exp=1701331495~hmac=9200f39cb83e27f242b6b4c4f3fbe14e4e6acd903b3033511d7c6b98a3564466',
           age=2, notes='Playful and friendly')
pet2 = Pet(name='Mochi', species='Dog',
           photo_url='https://img.freepik.com/free-photo/image-dog-isolated-yellow-background_1409-4222.jpg?t=st=1701330777~exp=1701334377~hmac=7de921281e74d6d42c1ac0a86ebfc5af2566d33eea43633d8ed6b377d07c1e76&w=2000', age=1, notes='Loves to cuddle')
pet3 = Pet(name='Buddy', species='Dog',
           photo_url='https://img.freepik.com/free-photo/cute-dog-with-nature-background_23-2150687007.jpg?t=st=1701330685~exp=1701334285~hmac=569f23775c7a91de27dbc0fb246ebf334b5c3cf56940ed32d9abcfe4295e2cd2&w=2000', age=3, notes='Energetic and loyal')
pet4 = Pet(name='Whiskers', species='Dog', photo_url='https://img.freepik.com/free-photo/adorable-jack-russell-retriever-puppy-portrait_53876-64825.jpg?w=2000&t=st=1701330585~exp=1701331185~hmac=2a01a339335db735fda07816716694e864287f7877287747bb11c182c622febd',
           age=2, notes='Independent but affectionate')

# Sample data for User model
user1 = User(username='johndoe', first_name='John', last_name='Doe')
user2 = User(username='janedoe', first_name='Jane', last_name='Doe')
user3 = User(username='petlover', first_name='Pet', last_name='Lover')
user4 = User(username='furryfriend', first_name='Furry', last_name='Friend')


db.session.add_all([pet1, pet2, pet3, pet4])
db.session.commit()

# Add sample user data seperatesly inncase we establish a relationship later
db.session.add_all([user1, user2, user3, user4])
db.session.commit()
