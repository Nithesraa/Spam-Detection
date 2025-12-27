import streamlit as st
from src.predict import predict_spam_with_confidence

st.set_page_config(
    page_title="Spam Detection System",
    page_icon="📩",
    layout="centered"
)

st.title("📩 Spam Detection System")
st.write("Enter a message to check whether it is **Spam** or **Not Spam**.")

user_input = st.text_area("✉️ Message", height=150)

if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:
        label, confidence = predict_spam_with_confidence(user_input)

        if "Spam" in label:
            st.error(f"🚨 Result: {label}\n\nConfidence: {confidence}%")
        else:
            st.success(f"✅ Result: {label}\n\nConfidence: {confidence}%")
