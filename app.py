# app.py
from flask import Flask, render_template, request
import joblib
from model.utils import clean_text

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("model/classifier.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        text = request.form["input_text"]
        cleaned = clean_text(text)
        vec = vectorizer.transform([cleaned])
        result = model.predict(vec)[0]
        prediction = "AI-Generated" if result == 1 else "Human-Written"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
