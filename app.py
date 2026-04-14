import streamlit as st
from predict import predict_url

st.title("🔐 URL Phishing Detector")

url = st.text_input("Enter URL")

if st.button("Check"):
    if url:
        result = predict_url(url)
        
        if result == "Phishing":
            st.error("⚠️ Phishing URL")
        else:
            st.success("✅ Safe URL")
    else:
        st.warning("Enter a URL")
