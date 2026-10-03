from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("event_budget_model.pkl")

# Load encoders
encoders = joblib.load("event_encoders.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from form
    event_type = request.form["event_type"]
    attendees = int(request.form["attendees"])
    venue = request.form["venue"]
    status = request.form["status"]
    organizer = request.form["organizer"]
    year = int(request.form["year"])
    month = int(request.form["month"])
    day = int(request.form["day"])

    # Encode categorical values
    event_type_encoded = encoders["Event_Type"].transform([event_type])[0]
    venue_encoded = encoders["Venue"].transform([venue])[0]
    status_encoded = encoders["Status"].transform([status])[0]
    organizer_encoded = encoders["Organizer"].transform([organizer])[0]

    # Prepare input
    input_data = [[
        event_type_encoded,
        attendees,
        venue_encoded,
        status_encoded,
        organizer_encoded,
        year,
        month,
        day
    ]]

    # Predict budget
    prediction = model.predict(input_data)

    predicted_budget = round(prediction[0], 2)

    return render_template(
        "result.html",
        prediction=predicted_budget
    )


if __name__ == "__main__":
    print("Starting Event Management Flask App...")
    app.run(debug=True)