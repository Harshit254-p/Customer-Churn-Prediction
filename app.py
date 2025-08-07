from flask import Flask, request, jsonify, render_template
from churn_model.preprocess import preprocess_input
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load("churn_model/model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_df = preprocess_input(data)
    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0].tolist()
    return jsonify({"churn": int(prediction), "probabilities": probabilities})


if __name__ == "__main__":
    app.run(debug=True)
