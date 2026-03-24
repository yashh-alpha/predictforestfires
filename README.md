# Forest Fire Prediction Web App

## Overview

This project is a machine learning-based web application that predicts the likelihood of forest fires using environmental and meteorological inputs. The model is trained on historical data and deployed using a Flask backend.

The application allows users to input parameters such as temperature, humidity, wind speed, and rainfall, and returns a prediction indicating the fire risk.

---

## Live Demo

https://predictforestfires-ga2w.onrender.com

Note: The application may take a few seconds to load initially due to free hosting limitations.

---

## Features

* Predict forest fire risk based on user inputs
* End-to-end machine learning pipeline
* Flask-based web deployment
* Simple and interactive user interface
* Deployed on cloud (Render)

---

## Tech Stack

* Python
* NumPy
* Pandas
* Scikit-learn
* Flask
* Gunicorn

---

## Project Structure

```id="r8lbw6"
predictforestfires/
│
├── app.py                # Flask application
├── model.pkl             # Trained machine learning model
├── requirements.txt      # Dependencies
├── Procfile              # Deployment configuration
├── templates/
│   └── index.html        # Frontend UI
└── README.md
```

---

## Installation

1. Clone the repository

```id="ocd6bs"
git clone https://github.com/yashh-alpha/predictforestfires.git
cd predictforestfires
```

2. Create a virtual environment (optional)

```id="e5p4rs"
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```id="y9n9pv"
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server locally:

```id="3th1ut"
python app.py
```

Open in browser:

```id="c5cy0s"
http://127.0.0.1:5000/
```

---

## Usage

1. Enter input values:

   * Temperature
   * Relative Humidity
   * Wind Speed
   * Rain

2. Click **Predict**

3. The model will output the predicted forest fire risk.

---

## Deployment

This application is deployed using Render.

To deploy:

* Add `gunicorn` to requirements.txt
* Create a Procfile:

```id="is74x3"
web: gunicorn app:app
```

---

## Future Improvements

* Improve model performance using advanced algorithms (e.g., XGBoost)
* Add feature scaling and preprocessing pipeline
* Enhance UI with better styling and interactivity
* Add probability/confidence score
* Integrate real-time weather data

---

## Author

Yash Kumar

---

## License

This project is for educational purposes and can be freely used or modified.
