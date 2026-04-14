import joblib

model = joblib.load("model.pkl")

def extract_features(url):
    return [[
        len(url),
        1 if url.startswith("https") else 0,
        1 if any(char.isdigit() for char in url) else 0,
        1 if "@" in url else 0,
        1 if "-" in url else 0,
        url.count("."),
        url.count(".") - 1,
        365,
        0
    ]]

def predict_url(url):
    features = extract_features(url)
    result = model.predict(features)[0]
    return "Phishing" if result == 1 else "Safe"
