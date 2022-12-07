from publiclibrary import db

class Customers(db.Model):
    """Customers Table"""
    __tablename__ = 'customers'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    city = db.Column(db.String(15))
    age = db.Column(db.Integer)
    customer_loans = db.relationship("Loans", backref="Customers", lazy=True)

    def __init__(self, name, city, age):
        self.name=name
        self.city=city
        self.age=age

# db.create_all()
