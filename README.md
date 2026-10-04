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
SmartPlanner uses Random Forest Regression to predict the estimated budget of an event. It is a supervised machine learning algorithm used for predicting continuous numerical values such as event costs.

Random Forest creates multiple decision trees, where each tree learns different patterns from the training data and produces its own prediction. The final budget prediction is calculated by combining the results of these trees, making the model more reliable and reducing prediction errors.

This algorithm is suitable for SmartPlanner because the dataset contains different event-related features such as event type, number of attendees, venue, status, organizer, and event date. After preprocessing and Label Encoding, these features are used by the model to learn the relationship between event details and budget.

The model is trained using 80% of the dataset and tested on the remaining 20%. Its performance is evaluated using MAE and R² Score. The trained model is saved using Joblib and integrated with Flask to provide budget predictions through the web application.

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


