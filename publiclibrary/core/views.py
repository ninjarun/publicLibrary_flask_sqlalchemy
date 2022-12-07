from flask import render_template, Blueprint, request
from publiclibrary.core.util import dummy
core= Blueprint('core',__name__,template_folder="templates")

@core.route("/", methods=['POST','GET'])
def index():
    """starting view"""
    if request.method=='POST':dummy()
    return render_template('layout.html')

