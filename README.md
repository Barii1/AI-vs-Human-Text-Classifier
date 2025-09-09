# AI-vs-Human-Text-Classifier
This project is a full-stack web application that classifies input text as either human-written or AI-generated using machine learning. It leverages a Logistic Regression model trained on a custom dataset with TF-IDF vectorization for feature extraction. The app provides a user-friendly interface for text input and instant predictions.


Key Features
Backend (Flask & ML): Handles text preprocessing (cleaning, normalization), vectorization, and prediction using a pre-trained Logistic Regression model.
Frontend (HTML, CSS): Responsive design with Tailwind CSS, Bootstrap, and custom animations for an engaging user experience, including a text input area and prediction display.
Model Training: Performed in a Jupyter Notebook (not included here) using scikit-learn, with the model and vectorizer saved as .pkl files.
Prediction Logic: Cleans input text, transforms it via TF-IDF, and predicts using the loaded model.

Technologies Used
Backend: Python, Flask, scikit-learn, NLTK, Joblib
Frontend: HTML, CSS (Tailwind, Bootstrap), Custom styles for animations and effects
Other: Jupyter Notebook for model training and evaluation


How to Run
Install dependencies: pip install flask joblib nltk scikit-learn
Ensure project files (app.py, utils.py, classifier.pkl, vectorizer.pkl, index.html, styles.css) are in place.
Run the Flask server: python app.py
Open a browser and navigate to http://127.0.0.1:5000/



Input text and click "Classify" to get a prediction.

