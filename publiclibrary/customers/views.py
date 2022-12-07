from flask import Flask, render_template, request, Blueprint
from publiclibrary import db
from publiclibrary.core.util import del_func
from publiclibrary.customers.models import Customers

customers= Blueprint('customers',__name__,template_folder="templates")

##############################################################################
##################### start of customer functions ###########################
##############################################################################
@customers.route("/addcustomer/", methods=['POST','GET'])
def add_customer():
    """add customer to database"""
    if request.method=='POST':
        new_customer=request.form
        newCustomer=Customers(new_customer['nm'],new_customer['ct'],new_customer['age'])
        db.session.add(newCustomer)
        db.session.commit()
        return render_template('addcustomer.html', msg="Customer Added Succsefully!")
    return render_template('addcustomer.html')

@customers.route("/findcustomer/", methods=['GET','POST'])
@customers.route("/findcustomer/<ind>", methods=['DELETE','GET'])
def find_customer(ind=-1):
    """find customer by name - also customers can be removed once found"""
    names=db.session.query(Customers).filter_by(name=request.form.get('nm')).all() if request.method=="POST" else []
    flag=True if len(names)>0 else False
    render_info=del_func(ind, Customers,"Customer") if int(ind)>0 else ["None","None"]
    return render_template('findcustomer.html',allcustomers=Customers.query.all(),names=names ,flag=flag, msg=render_info[1], color=render_info[0])

@customers.route("/displayall/", methods=['GET'])
@customers.route("/displayall/<ind>", methods=['DELETE','GET'])
def display_all(ind=-1):
    """display all customers - customers can also be removed with this function"""
    render_info=del_func(ind, Customers,"Customer") if int(ind)>0 else ["None","None"]
    return render_template('displayallcustomers.html',names=Customers.query.all(),msg=render_info[1],color=render_info[0])    
##############################################################################
######################### end of customer functions ##########################
##############################################################################