from flask import Flask
from z3 import *

Tie, Shirt = Bools('Tie Shirt')
s = Solver()
s.add(Or(Tie, Shirt), Or(Not(Tie), Shirt), Or(Not(Tie), Not(Shirt)))
print(s.check())
print(s.model())


# CREATE FLASK APP
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'



