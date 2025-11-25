import streamlit as st

# Set page configuration
st.set_page_config(page_title="Farmer's Hub", page_icon="🌾", layout="wide")

# Title of the Home Page (centered using Markdown)
st.markdown("<h1 style='text-align: center;'>Welcome to Farmer's Hub 🌾</h1>", unsafe_allow_html=True)

# Introduction text
st.write("""
This is your one-stop solution for agricultural innovation. Choose any of the following projects
to explore advanced technologies tailored for farmers.
""")

# Layout for the 3 sections (using columns)
col1, col2, col3 = st.columns(3)

# Section 1: Crop Recommendation System
with col1:
    st.image("crop_rec_project.jpg", use_column_width=True)  # Replace with your image file or URL
    st.subheader("Crop Recommendation System")
    st.write("""
    A system that suggests the best crops to grow based on weather, soil, and other parameters.
    Click below to explore more.
    """)
    st.markdown("""
        <a href="https://crop-recomendation-project.streamlit.app/" target="_blank">
            <button style='background-color: #4CAF50; color: white; font-size: 18px; padding: 10px 24px; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); transition: background-color 0.3s, transform 0.3s;'>
                Explore Crop Recommendation
            </button>
        </a>
    """, unsafe_allow_html=True)

# Section 2: Potato Disease Classifier with Eradication and Awareness
with col2:
    st.image("potato_prediction.jpg", use_column_width=True)  # Replace with your image file or URL
    st.subheader("Potato Disease Classifier")
    st.write("""
    Classify potato diseases, learn about them, and get recommendations for eradication.
    Click below to explore more.
    """)
    st.markdown("""
        <a href="https://potatodiseasepredediction.streamlit.app/" target="_blank">
            <button style='background-color: #4CAF50; color: white; font-size: 18px; padding: 10px 24px; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); transition: background-color 0.3s, transform 0.3s;'>
                Explore Potato Disease Classifier
            </button>
        </a>
    """, unsafe_allow_html=True)

# Section 3: Chatbot for Farmer
with col3:
    st.image("kishan_mitra.jpg", use_column_width=True)  # Replace with your image file or URL
    st.subheader("Chatbot for Farmer")
    st.write("""
    Chat with an AI assistant to get farming-related advice, tips, and guidance.
    Click below to explore more.
    """)
    st.markdown("""
        <a href="https://chatbotfarmerudemy.streamlit.app//" target="_blank">
            <button style='background-color: #4CAF50; color: white; font-size: 18px; padding: 10px 24px; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); transition: background-color 0.3s, transform 0.3s;'>
                Explore Chatbot for Farmer
            </button>
        </a>
    """, unsafe_allow_html=True)

# Footer (centered)
st.markdown("<h4 style='text-align: center;'>--- Developed with 💚 for the farming community. ---</h4>", unsafe_allow_html=True)
