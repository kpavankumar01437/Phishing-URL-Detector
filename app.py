import streamlit as st

def check_phishing(url):
    score = 0

    if "https" not in url:
        score += 1

    if "@" in url:
        score += 1

    if "-" in url:
        score += 1

    suspicious_words = ["login", "verify", "bank", "update", "free", "offer"]

    for word in suspicious_words:
        if word in url.lower():
            score += 1

    if len(url) > 75:
        score += 1

    if score >= 3:
        return "⚠ Likely Phishing URL"
    else:
        return "✅ Looks Safe"


st.title("🔒 Phishing URL Detector")

url = st.text_input("Enter URL")

if st.button("Check URL"):
    result = check_phishing(url)
    st.write(result)