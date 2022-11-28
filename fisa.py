from flask import *
from z3 import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

NAMES = [
    "*formAcqu*",
    "*form*",
    "*nationalitySender*",
    "*locationSender*",
    "*nationalityReceiver*",
    "*locationReceiver*",
    "*privacy*",
    "*needWarrant*",
    "*targetNationaliy*",
    "*consent*",

    "*authorize*",
    "*investigation*",

]

# HANDLE LOGIC
def logic_handler(request):
    # FILE MANIPULATION
    data1 = None; data2 = None
    with open("50 USC 1801 (f)-z3-tmp1.txt", "r") as file:
        data1 = file.read()
        data2 = data1

        # for name in NAMES:
            # data2 = data1.replace(name, request.form.get(name)) # replace placeholders
    
    with open("50 USC 1801 (f)-z3-tmp2.txt", "w") as file:
        file.write(data2)

    # USE SELENIUM TO SOLVE IT ACCORDINGLY
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("https://webspass.spass-prover.org/")


    browser.quit()

    # USE Z3 SOLVER ACORDINGLY
    s = Solver()
    s.from_file("50 USC 1801 (f)-z3-tmp1.txt") # don't forget to change to tmp2
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
