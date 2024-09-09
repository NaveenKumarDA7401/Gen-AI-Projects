from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

from google.generativeai import configure

configure(api_key="AIzaSyAMSD8qSTX_MqVczgfMjuohwGSBSt-S4EQ")


# Load environment variables
load_dotenv()

# Initialize the Generative Model with the updated model ID
try:
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"Error initializing model: {e}")

# Function to get response from the Gemini model
def get_gemeni_response(question, image):
    try:
        if question:
            response = model.generate_content(question, image)
        else:
            response = model.generate_content(image)
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"

# Initialize the Streamlit application
st.set_page_config(page_title="PRINCE IMAGE Demo")
st.header("PRINCE CHATBOT & IMAGE DETECTOR")

user_input = st.text_input("Input prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the Image")

# If submit is clicked
if submit:
    response = get_gemeni_response(user_input, image)
    st.subheader("The response is")
    st.write(response)
