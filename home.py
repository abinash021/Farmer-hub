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
    st.image("crop_rec_project.jpg", use_column_width=True)  # Replace with your image URL
    st.subheader("Crop Recommendation System")
    st.write("""
    A system that suggests the best crops to grow based on weather, soil, and other parameters.
    Click below to explore more.
    """)
    if st.button("Explore Crop Recommendation", key="crop_recommendation", help="Get suggestions for the best crops"):
        st.experimental_set_query_params(project="crop_recommendation")

# Section 2: Potato Disease Classifier with Eradication and Awareness
with col2:
    st.image("potato_prediction.jpg", use_column_width=True)  # Replace with your image URL
    st.subheader("Potato Disease Classifier")
    st.write("""
    Classify potato diseases, learn about them, and get recommendations for eradication.
    Click below to explore more.
    """)
    if st.button("Explore Potato Disease Classifier", key="potato_disease_classifier", help="Learn about potato diseases and how to eradicate them"):
        st.experimental_set_query_params(project="potato_disease_classifier")

# Section 3: Chatbot for Farmer
with col3:
    st.image("kishan_mitra.jpg", use_column_width=True)  # Replace with your image URL
    st.subheader("Chatbot for Farmer")
    st.write("""
    Chat with an AI assistant to get farming-related advice, tips, and guidance.
    Click below to explore more.
    """)
    if st.button("Explore Chatbot for Farmer", key="chatbot_for_farmer", help="Get farming advice from our AI chatbot"):
        st.experimental_set_query_params(project="chatbot_for_farmer")

# Add footer (centered) for better UI
st.markdown("<h4 style='text-align: center;'>--- Developed with 💚 for the farming community. ---</h4>", unsafe_allow_html=True)

# Custom CSS for more eye-catching buttons
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;  /* Green background */
        color: white;               /* White text */
        font-size: 18px;            /* Larger text */
        padding: 10px 24px;         /* Increased padding */
        border: none;               /* Remove border */
        border-radius: 8px;         /* Rounded corners */
        cursor: pointer;           /* Pointer on hover */
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);  /* Shadow effect */
        transition: background-color 0.3s, transform 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker green when hovering */
        transform: scale(1.1);      /* Slight zoom effect */
    }
    </style>
""", unsafe_allow_html=True)
