import streamlit as st
from PIL import Image
import numpy as np
import joblib
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array

# ----------------------
# Load saved RandomForest + LabelEncoder
# ----------------------
rf_model_path = 'rf_model_mobilenetv2_potato.joblib'
le_path = 'label_encoder_mobilenetv2_potato.joblib'

rf_classifier = joblib.load(rf_model_path)
label_encoder = joblib.load(le_path)

# ----------------------
# Load MobileNetV2 (feature extractor)
# ----------------------
IMG_SIZE = (224, 224)
feature_extractor = MobileNetV2(weights='imagenet',
                                include_top=False,
                                pooling='avg',
                                input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3))
feature_extractor.trainable = False

# ----------------------
# Preprocessing & feature extraction
# ----------------------
def preprocess_image(image: Image.Image):
    img = image.convert("RGB").resize(IMG_SIZE)
    arr = img_to_array(img)
    arr = preprocess_input(arr)  # MobileNetV2-specific preprocessing
    arr = np.expand_dims(arr, axis=0)  # shape (1,224,224,3)
    return arr

def image_to_embedding(image: Image.Image):
    x = preprocess_image(image)
    features = feature_extractor.predict(x, verbose=0)  # shape (1,1280)
    return features

# ----------------------
# Extra content: descriptions, tips, links
# ----------------------
# (Place example images in ./images/ or adjust paths)
eradication_methods = {
    'Potato___Early_blight': {
        'image': "images/potato-early-blight-leaves.jpg",  # change path if needed
        'description': """
### 🐛 Early Blight - *Alternaria solani*

**Symptoms:**
- Brown spots with concentric rings on older leaves.
- Yellowing and drying leaves starting from the bottom.

**Pesticide Treatment:**
- Apply fungicides like **Chlorothalonil**, **Mancozeb**, or **Azoxystrobin** early in the season.
- Repeat every 7–10 days during humid conditions.

**Organic Treatment:**
- Use **neem oil** or **compost tea spray** weekly.
- Remove infected leaves manually.
- Improve air circulation through proper spacing.

**Prevention Tips:**
- Rotate crops every 2–3 years.
- Avoid overhead watering.
- Ensure good drainage and soil health.
        """
    },

    'Potato___Late_blight': {
        'image': "images/LateBlight03.JPG",
        'description': """
### 🌧️ Late Blight - *Phytophthora infestans*

**Symptoms:**
- Large, dark brown to black lesions on leaves and stems.
- White fungal growth on undersides of leaves in humid weather.
- Rapid plant collapse in severe infections.

**Pesticide Treatment:**
- Use **Metalaxyl**, **Copper-based fungicides**, or **Cyazofamid**.
- Apply before disease spreads, especially in wet weather.

**Organic Treatment:**
- Remove and destroy infected plants immediately.
- Apply **baking soda + oil + soap** spray.
- Use resistant varieties if possible.

**Prevention Tips:**
- Avoid waterlogged soils.
- Disinfect tools after contact.
- Keep leaves dry—water in early morning.
        """
    },

    'Potato___healthy': {
        'image': "images/healthy_leaf.jpg",
        'description': """
### 🌿 Healthy Potato Plant

Your plant shows no signs of disease. Keep up the good work!

**Care Tips:**
- Regularly check leaves for early signs of spots or lesions.
- Fertilize with balanced NPK fertilizers.
- Mulch around the base to retain moisture and control weeds.
- Keep good air flow between plants.

**Preventative Measures:**
- Crop rotation.
- Use certified disease-free seed potatoes.
- Water early in the day to avoid prolonged moisture.
        """
    }
}

# Awareness links
disease_awareness_links = {
    'Potato___Early_blight': [
        {"title": "📝 Understanding Early Blight in Potatoes (Symptoms, Lifecycle & Damage)",
         "url": "https://plantvillage.psu.edu/topics/potato/infos/disease-early-blight"},
        {"title": "🌱 Organic Control of Early Blight - University of Minnesota Extension",
         "url": "https://extension.umn.edu/disease-management/early-blight-potato"},
        {"title": "🎥 Video Guide: Identifying & Managing Early Blight (YouTube)",
         "url": "https://www.youtube.com/watch?v=J1KefcszLxA"},
        {"title": "👩‍🌾 Farmer Forum: Real Experiences with Early Blight Treatments",
         "url": "https://www.growveg.com/guides/early-blight-in-potatoes/"}
    ],

    'Potato___Late_blight': [
        {"title": "🧬 Late Blight: Causes, Spread, and Devastation in Crops",
         "url": "https://cipotato.org/pressroom/blogs/late-blight-of-potato/"},
        {"title": "🔬 Management of Late Blight - UC IPM",
         "url": "https://ipm.ucanr.edu/PMG/r607101311.html"},
        {"title": "🎥 Late Blight: How It Looks & How to Stop It (YouTube)",
         "url": "https://www.youtube.com/watch?v=6F_Wv0U3Lf4"},
        {"title": "📚 Late Blight Research Publications - PotatoPro",
         "url": "https://www.potatopro.com/topics/late-blight"}
    ],

    'Potato___healthy': [
        {"title": "🌿 Best Practices for Growing Healthy Potato Plants",
         "url": "https://www.ag.ndsu.edu/publications/crops/potato-production-and-management"},
        {"title": "🚜 10 Tips to Prevent Common Potato Diseases",
         "url": "https://www.planetnatural.com/pest-problem-solver/plant-disease/potato-disease/"},
        {"title": "🔄 Crop Rotation & Soil Health Strategies",
         "url": "https://www.canr.msu.edu/news/crop_rotation_and_disease_control_in_potato_fields"},
        {"title": "👨‍🔬 Healthy Plant Checklist (PDF Download)",
         "url": "https://edis.ifas.ufl.edu/pdf/CV/CV29800.pdf"}
    ]
}

# ----------------------
# Streamlit UI
# ----------------------
st.set_page_config(page_title="Potato Disease Classifier", layout="centered")
st.title("🥔 Potato Disease Classification (MobileNetV2 + Random Forest)")
st.write("Upload a potato leaf image to classify it as **Early Blight**, **Late Blight**, or **Healthy**.")

uploaded_file = st.file_uploader("📷 Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
    except Exception as e:
        st.error(f"Could not open the image: {e}")
        st.stop()

    st.image(image, caption="🖼️ Uploaded Image", use_column_width=True)
    st.write("🔍 Classifying...")

    # Extract features
    embedding = image_to_embedding(image)

    # Predict with RF
    pred_numeric = rf_classifier.predict(embedding)[0]
    pred_proba = rf_classifier.predict_proba(embedding)[0]

    # Decode class name
    pred_label = label_encoder.inverse_transform([pred_numeric])[0]
    display_label = pred_label.split('___')[-1].replace('_', ' ')

    st.markdown(f"### ✅ Prediction: **{display_label}**")

    # Show probabilities (sorted display or original order)
    st.subheader("📊 Prediction Probabilities")
    class_names = label_encoder.classes_
    for cls, prob in zip(class_names, pred_proba):
        pretty = cls.split('___')[-1].replace('_', ' ')
        st.write(f"- **{pretty}**: {prob:.2%}")

    # OPTIONAL: show a simple bar chart of probabilities
    try:
        import pandas as pd
        prob_df = pd.DataFrame({
            "class": [c.split('___')[-1].replace('_', ' ') for c in class_names],
            "probability": pred_proba
        })
        st.bar_chart(prob_df.set_index("class"))
    except Exception:
        pass

    # ----------------------
    # Display eradication/tips + image + links for predicted class
    # ----------------------
    info = eradication_methods.get(pred_label)
    if info:
        st.markdown("---")
        st.subheader("🩺 Diagnosis & Care Recommendations")

        # example image (if available)
        img_path = info.get('image')
        if img_path:
            try:
                ex_img = Image.open(img_path)
                st.image(ex_img, caption=f"Example: {display_label}", use_column_width=True)
            except FileNotFoundError:
                st.info(f"Example image not found at `{img_path}`. Put the image in your app folder or update the path.")
            except Exception:
                st.info("Could not load example image (check path and file).")

        # rich description (markdown)
        st.markdown(info.get('description', "No additional info available."))

        # useful links
        links = disease_awareness_links.get(pred_label, [])
        if links:
            st.subheader("🔗 Useful resources")
            for link in links:
                # show clickable markdown link
                st.markdown(f"- [{link['title']}]({link['url']})")
    else:
        st.info("No extended info available for this class.")
