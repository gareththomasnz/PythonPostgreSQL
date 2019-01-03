from project.user import User
from project.database import Database

Database.initialise(database="Learning", user="postgres", password="1234", host="localhost")

user = User('gareththomasnz@yahoo.com', 'Gareth', 'Thomas')

user.save_to_db()

user_from_db = User.load_from_db_by_email('gareththomasnz@yahoo.com')

print(user_from_db)