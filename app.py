from flask import Flask, render_template
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///footprint_db2'

############## 
# Start page #   
##############  

@app.route('/')
def introduce():
    """Show start_page"""
    breakpoint()
    return render_template("start.html")
