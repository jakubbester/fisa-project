from flask import *
from z3 import *

# HANDLE LOGIC
def logic_handler(request):
    s = Solver()
    print(s.from_file("agatha-z3.txt"))
    # print(s.proof())
    print(s.check())
    print(s.model())

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
