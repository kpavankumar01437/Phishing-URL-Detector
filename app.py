import streamlit as st

st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🔒",
    layout="centered"
)

def check_phishing(url):
    score = 0
    reasons = []

    if "https" not in url:
        score += 1
        reasons.append("Missing HTTPS")

    if "@" in url:
        score += 1
        reasons.append("Contains @ symbol")

    if "-" in url:
        score += 1
        reasons.append("Contains hyphen")

    suspicious_words = [
        "login",
        "verify",
        "bank",
        "update",
        "free",
        "offer"
    ]

    for word in suspicious_words:
        if word in url.lower():
            score += 1
            reasons.append(f"Contains suspicious word: {word}")

    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long")

    risk_percentage = min(score * 20, 100)

    return risk_percentage, reasons

st.title("🔒 Phishing URL Detector")

st.write("Analyze URLs for phishing indicators.")

url = st.text_input("Enter URL")

if st.button("Analyze URL"):

    risk, reasons = check_phishing(url)

    st.subheader("Analysis Result")

    if risk >= 60:
        st.error(f"⚠ High Risk ({risk}%)")
    elif risk >= 40:
        st.warning(f"⚠ Medium Risk ({risk}%)")
    else:
        st.success(f"✅ Low Risk ({risk}%)")

    st.progress(risk)

    st.subheader("Detected Indicators")

    if reasons:
        for reason in reasons:
            st.write("•", reason)
    else:
        st.write("No suspicious indicators detected.")