from flask import *
from z3 import *

NAMES = [
    "consent",
]

# HANDLE LOGIC
def logic_handler(request):
    # FILE MANIPULATION
    data1 = None; data2 = None
    with open("50 USC 1801 (f)-z3-tmp1.txt", "r") as file:
        data1 = file.read()
        print(request.form.get("consent"))
        data2 = data1.replace("check-sat", "check-sat1") # replace placeholders
    
    with open("50 USC 1801 (f)-z3-tmp2.txt", "w") as file:
        file.write(data2)

    # USE Z3 SOLVER ACORDINGLY
    s = Solver()
    s.from_file("50 USC 1801 (f)-z3-tmp1.txt")
    # print(s.check())
    # print(s.model())

    return True

# CREATE FLASK APP
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        result = logic_handler(request)

    return render_template("index.html", data=result)

if __name__ == "__main__":
    app.run()
