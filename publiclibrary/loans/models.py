from publiclibrary import db





class Loans(db.Model):
    """Loans Table"""
    __tablename__ = "loans"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    loan_date = db.Column(db.Integer)
    return_date = db.Column(db.Integer)

    def __init__(self,customer_id,book_id,loan_date,return_date):
        self.customer_id=customer_id
        self.book_id=book_id
        self.return_date=return_date
        self.loan_date=loan_date

