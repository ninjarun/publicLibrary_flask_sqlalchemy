from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_library.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

from publiclibrary.core.views import core
from publiclibrary.customers.views import customers
from publiclibrary.books.views import books
from publiclibrary.loans.views import loans

app.register_blueprint(core)
app.register_blueprint(customers)
app.register_blueprint(books)
app.register_blueprint(loans)

