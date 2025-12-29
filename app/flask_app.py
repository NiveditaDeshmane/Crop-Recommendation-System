# Crop Recommendation Web App
# --------------------------------------------------
# Run using: Flask (python flask_app.py)
# --------------------------------------------------



from flask import Flask, render_template, request
import joblib
import pandas as pd

# Load model and preprocessor
model = joblib.load("../Models/crop_model.pkl")
preprocessor = joblib.load("../Models/scaler.pkl")
label_encoder = joblib.load("../Models/label_encoder.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        # Collect form data
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        # Create DataFrame
        sample = pd.DataFrame([{
            "N": N,
            "P": P,
            "K": K,
            "temperature": temperature,
            "humidity": humidity,
            "ph": ph,
            "rainfall": rainfall
        }])

        # Transform + Predict
        x_processed = preprocessor.transform(sample)
        predicted_class = model.predict(x_processed)[0]
        prediction = label_encoder.inverse_transform([predicted_class])[0]

    return render_template("index.html", result=prediction)

if __name__ == "__main__":
    app.run(debug=True)