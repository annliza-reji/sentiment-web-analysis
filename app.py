from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        text = request.form["text"]
        analysis = TextBlob(text)

        if analysis.sentiment.polarity > 0:
            result = "Positive "
        elif analysis.sentiment.polarity < 0:
            result = "Negative "
        else:
            result = "Neutral "

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)