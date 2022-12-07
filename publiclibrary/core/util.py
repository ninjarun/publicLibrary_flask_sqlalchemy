from publiclibrary import db
import datetime
from random import randint
from publiclibrary.customers.models import Customers
from publiclibrary.books.models import Books
from publiclibrary.loans.models import Loans
from publiclibrary import db,app
from faker import Faker

def dummy():
    """function to add fake data to database"""
    books,loans,customers=[],[],[]
    fake=Faker()
    
    i=0
    while i<50:
        cust=Customers(name=fake.name(),city=fake.city(),age=randint(18,60))
        customers.append(cust)
        book=Books(name=fake.name(),author=fake.name(),year_published=randint(1900,2022),type=randint(1,3))
        books.append(book)
        i+=1
    
    i=0
    while i <10:
        loan=Loans(book_id=randint(1,50),customer_id=randint(1,50),loan_date=datetime.date.today()+datetime.timedelta(days=-10),return_date=datetime.date.today())
        loans.append(loan)
        loan=Loans(book_id=randint(1,50),customer_id=randint(1,50),loan_date=datetime.date.today(),return_date=datetime.date.today()+datetime.timedelta(days=-10))
        loans.append(loan)
        i+=1
    
    with app.app_context():
        db.session.add_all(customers)
        db.session.add_all(books)
        db.session.add_all(loans)
        db.session.commit()
    
    

def del_func(ind,table,bookorcustomer):
    """function to remove data from database - works with the books,customers and loans views"""
    if int(ind)>0:
        id2delete=table.query.get(ind)
        try:
            db.session.delete(id2delete)
            db.session.commit()
            return ["green",f"{bookorcustomer} Removed Succsefully!"]
        except Exception as error:
            x=str(error)
            if "loans" in x:
                msg=f"This {bookorcustomer} Has Active Loans! Return Books!"
            elif "mapped" in x:
                msg=f"{bookorcustomer} Doesn't Exist"
            # db.session.rollback()
            db.session.close()
            return ["red",msg,]

