from time import sleep # to use together with Selenium

# IMPORT FLASK (for website server)
from flask import *

# IMPORT REQUIRED SELENIUM MODULES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

NAMES = [
    "*formAcqu*",
    "*form*",
    "*nationalitySender*",
    "*locationSender*",
    "*nationalityReceiver*",
    "*locationReceiver*",
    "*privacy*",
    "*needWarrant*",
    "*targetNationality*",
    "*consent*",
    "*authorize*",
    "*investigation*",
    "*relevant*",
    "*onlyRelevant*",
    "*intentional*",
    "*installOrUse*",
    "*monitor*",
    "*locationDevice*",
]

# HANDLE LOGIC
def logic_handler(request):
    # FILE MANIPULATION
    data = None
    with open("50 USC 1801 (f)-spass-tmp1.txt", "r") as file:
        data = file.read()
        for name in NAMES:
            data = data.replace(name, str(request.form.get(name))) # replace placeholders
    
    with open("50 USC 1801 (f)-spass-tmp2.txt", "w") as file:
        file.write(data)

    # USE SELENIUM TO OPEN WEBSPASS
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("https://webspass.spass-prover.org/")
    # browser.maximize_window() # use if want to maximize the intermediary window

    # FIND THE INPUT TEXTAREA PORTION
    file = open("50 USC 1801 (f)-spass-tmp2.txt", "r").read()
        
    input = browser.find_element(By.XPATH, value="//textarea[@name='textinput']")
    input.clear()
    browser.execute_script('arguments[0].value=arguments[1]', input, file)
    sleep(5.0)

    # FIND THE SUBMIT BUTTON AND PRESS IT (after some delay)
    submit = browser.find_element(By.XPATH, value="//input[@value=' Submit Form ']")
    submit.click()

    # SCRAPE THE RESULTS
    result = browser.find_element(By.XPATH, value="//pre")
    sleep(5.0)

    # RETURN THE CORRESPONDING RESULT
    if "Proof found" in result.text:
        browser.quit()
        return True
    else:
        browser.quit()
        return False

# CREATE FLASK APP
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        result = logic_handler(request)

    return render_template("index.html", data=result)

if __name__ == "__main__":
    app.run(port=6553)
