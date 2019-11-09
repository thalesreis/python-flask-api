from api.data.db_setup import db

class WineModel(db.Model):
    __tablename__ = 'wine'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), unique = True, nullable = False)
    price = db.Column(db.Float(10,2), nullable = False)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


# https://www.oreilly.com/library/view/essential-sqlalchemy/9780596516147/ch04.html        