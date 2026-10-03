# SmartPlanner

SmartPlanner is a machine learning-based event management system that predicts the estimated event budget based on event details such as event type, number of attendees, venue, status, organizer, and event date.

## Features

- Event budget prediction
- Random Forest Regression
- Flask web application
- Event details input form
- Prediction result page
- Budget visualization
- Responsive HTML and CSS interface

# Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- Joblib
- HTML
- CSS
- Chart.js

## Machine Learning

SmartPlanner uses **Random Forest Regression** for predicting the event budget.

Random Forest Regression combines multiple decision trees and produces a prediction based on the results of those trees.

It is suitable for this project because the dataset contains different types of event information, including numerical and categorical features.

## Dataset

The project uses `event_management.csv`, which contains event-related information such as:

- Event ID
- Event Type
- Event Date
- Attendees
- Budget
- Venue
- Status
- Organizer

# Technologies Used

- `event_management.csv` – Dataset containing event details used for training and prediction.
- `check_data.py` – Checks and displays the dataset structure, columns, data types, and missing values.
- `train_model.py` – Preprocesses the dataset, trains the Random Forest Regression model, evaluates it, and saves the model and encoders.
- `app.py` – Runs the Flask web application and handles user input and budget prediction.
- `event_budget_model.pkl` – Saved Random Forest Regression model used to predict the event budget.
- `event_encoders.pkl` – Saved Label Encoders used to convert categorical event details into numerical values.
- `templates/index.html` – Provides the main webpage where users enter event details for prediction.
- `templates/result.html` – Displays the predicted event budget and its graphical representation.

 # Dataset

The project uses:

```text
event_management.csv


