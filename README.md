Project Title: AI-Based URL Phishing Detector

Description:
This project detects phishing URLs using Machine Learning (Logistic Regression).
It analyzes URL features such as length, special characters, HTTPS usage, and domain structure.

Project Structure:
phishing-mini-project/
│
├── phishing_dataset.csv
├── train_model.py
├── predict.py
└── app.py

Technologies:
- Python
- Scikit-learn
- Pandas
- Streamlit


How it Works:
1. Dataset is used to train a Logistic Regression model.
2. Features are extracted from input URLs.
3. Model predicts whether URL is safe or phishing.
4. Streamlit UI provides real-time prediction.
