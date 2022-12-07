from publiclibrary import db

class Books(db.Model):
    """Books table
    includes id, name, author, year published and type colums
    related to Loans table - books_loans - colunm"""    
    __tablename__="books"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    author = db.Column(db.String(20))
    year_published  = db.Column(db.Integer)
    type = db.Column(db.Integer)
    books_loans = db.relationship("Loans", backref="Books", lazy=True)

    def __init__(self,name,author,year_published,type):
        self.name=name
        self.author=author
        self.year_published=year_published
        self.type=type
