
from flask import Flask, render_template, request


app = Flask(__name__)

@app.get("/")
def showPage():
    return render_template('index.html')

@app.post("/analyze")
def analyze():
    text = request.form['text']
    action = request.form['action']
    answer = ""
    if action == "cntchr":
        # count number of character
        answer = f"The number of characters are:- {len(text)}"
    elif action == "cntws":
        # count number of white spaces
        answer = f"The number of white spaces are:- {text.count(' ')}"
    elif action == "upr":
        # text in upper case
        answer = f"The text in upper case:- {text.upper()}"
    elif action == "lwr":
        # text in lower case
        answer = f"The text in lower case:- {text.lower()}"
    elif action == "splt":
        # spliting with white space
        answer = f"The sentence after spliting with white spaces:- {text.split()}"
    elif action == "strp":
        # removing extra white space from both side
        answer = f"The sentence after removing extra white spaces:- {text.strip(" ")}"
    elif action == "rstrp":
        # removing extra white space from right side
        answer = f"The sentence after removing white spaces from right side:- {text.rstrip()}"
    elif action == "lstrp":
        # removing extra white space from left side
        answer = f"The sentence after removing white spaces from left side:- {text.lstrip()}"
    elif action == "cap":
        # capitalize the sentence
        answer = f"The sentence with first letter capital:- {text.capitalize()}"
    elif action == "isaln":
        # Checking both alphabet and digit
        answer = f"Checking both alphabet and digit:- {text.isalnum()}"
    elif action == "isalp":
        # Checking both alphabet only
        answer = f"Checking alphabet only:- {text.isalpha()}"
    elif action == "islwr":
        # Checking lower case
        answer = f"Checking lower case:- {text.islower()}"
    elif action == "isspc":
        # Checking space
        answer = f"Checking space:- {text.isspace()}"
    elif action == "isupr":
        # Checking upper case
        answer = f"Checking upper case:- {text.isupper()}"
    elif action == "swap":
        # Converting lower to upper and upper to lower
        answer = f"After converting lower to upper and upper to lower:- {text.swapcase()}"
    return render_template('index.html',output = answer)


app.run(debug=True)