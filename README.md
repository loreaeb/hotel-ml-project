# Hotel ADR Prediction Web App

This is a **Flask web app** that predicts hotel room prices (Average Daily Rate) using a machine learning model.

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


## Dataset

Dataset from Kaggle: [Hotel Booking Demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

## Installation

Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/hotel-ml-project.git
cd hotel-ml-project


Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate   # macOS/Linux


Install dependencies:

pip install -r requirements.txt


Run the App

python app.py


Open your browser:
http://127.0.0.1:5000/

Fill the form → click Predict → see the ADR.

Dependencies
Flask
pandas
numpy
scikit-learn

Notes
Trained model stored in model.pkl
HTML template in templates/index.html
Background image in static/background.jpg