import streamlit as st
import requests

# Streamlit UI
st.title("Real-Time Language Translator")
st.subheader("Enter text and select the target language for translation.")

# Input fields for text and target language
text = st.text_area("Enter text to translate:")
target_language = st.selectbox("Select Target Language", ["Hindi", "French"])

# Button to trigger translation
if st.button("Translate"):
    if not text:
        st.error("Please enter some text to translate.")
    else:
        # Send request to Flask API
        api_url = "http://127.0.0.1:5000/translate"  # Update with your Flask API URL
        response = requests.post(api_url, json={"text": text, "target_language": target_language})

        if response.status_code == 200:
            result = response.json()
            st.success("Translation Completed!")
            st.write("**Translated Text:**")
            st.write(result["translated_text"])
        else:
            st.error("Error in translation. Please check the server.")
