# Hotel Prediction Web App

This is a **Flask web app** that predicts hotel room prices (Average Daily Rate) using a machine learning model.

---

## Project Structure

hotel-ml-project/
│ app.py
│ model.pkl
│ hotel_bookings.csv
│ requirements.txt
│ templates/
│ index.html
│ static/
│ background.jpg


---

## Dataset

The dataset used is from Kaggle:  
[Hotel Booking Demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/loreaeb/hotel-ml-project.git
cd hotel-ml-project
```

2. **Create and activate a virtual environment:**
python3 -m venv venv
source venv/bin/activate   # macOS/Linux

3. **Install Dependencies:**
pip install -r requirements.txt

4. **Run the app:**
python app.py

5. **Open your browser:**
http://127.0.0.1:5000/

Fill in the form → click Predict → see the ADR (predicted room price).

## Dependencies
Flask
pandas
numpy
scikit-learn

## Notes
Trained model stored in model.pkl
HTML template in templates/index.html
Background image in static/background.jpg
All UI changes (transparent buttons, olive-green color, background image) are reflected in the web app.

## Web Application
The app allows users to input booking details such as:
Lead time
Number of nights (weekend and weekday)
Number of adults, children, and babies

…and predicts the Average Daily Rate using the trained machine learning model.

The interface features a clean, elegant design with semi-transparent olive-green buttons and a luxury-style background image.

## Data Workflow
1. Load dataset (hotel_bookings.csv)
2. Validate and clean data
3. Train regression model using scikit-learn
4. Save trained model as model.pkl
5. Deploy the model in Flask web app for predictions


