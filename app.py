from flask import Flask, render_template, request
import joblib
import pandas as pd

# Initialize Flask App
app = Flask(__name__)

# Load the trained model
model = joblib.load("model/rainfall_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Read values from the HTML form
        day = float(request.form["day"])
        pressure = float(request.form["pressure"])
        maxtemp = float(request.form["maxtemp"])
        temperature = float(request.form["temparature"])
        mintemp = float(request.form["mintemp"])
        humidity = float(request.form["humidity"])

        # Create DataFrame
        input_data = pd.DataFrame([{
            "day": day,
            "pressure": pressure,
            "maxtemp": maxtemp,
            "temparature": temperature,
            "mintemp": mintemp,
            "humidity": humidity
        }])

        # Prediction
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            result = "🌧 Rainfall Expected"
        else:
            result = "☀ No Rainfall"

        return render_template("index.html", prediction=result)

    except Exception as e:
        return render_template("index.html",
                               prediction="Error : " + str(e))


if __name__ == "__main__":
    app.run(debug=True)