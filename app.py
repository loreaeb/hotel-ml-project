from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        # Get input from the form
        data = {
            'lead_time': float(request.form['lead_time']),
            'stays_in_weekend_nights': float(request.form['weekend']),
            'stays_in_week_nights': float(request.form['week']),
            'adults': float(request.form['adults']),
            'children': float(request.form['children']),
            'babies': float(request.form['babies']),
        }
        df_input = pd.DataFrame([data])
        prediction = model.predict(df_input)[0]

    # Render the page with prediction (or None if GET request)
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

