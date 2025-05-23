# -*- coding: utf-8 -*-
"""Untitled44.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JRL74QfxTKIdq-XjZ_cFasnZoDdfBtYf
"""

import streamlit as st
import time
import numpy as np
import cv2
from PIL import Image

# Ensure Streamlit is installed
try:
    import streamlit as st
except ModuleNotFoundError:
    print("Error: Streamlit is not installed. Please install it using 'pip install streamlit'")
    exit()

# ---- PAGE CONFIG ----
st.set_page_config(page_title="AI Disease Detection", page_icon="🩺", layout="wide")

# ---- SIDEBAR NAVIGATION ----
st.sidebar.title("🔍 AI Disease Detection")
st.sidebar.write("Upload a Chest X-ray to analyze possible symptoms.")

dark_mode = st.sidebar.checkbox("🌙 Dark Mode")

# ---- HEADER ----
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>AI-Powered Chest X-ray Analysis</h1>
    <p style='text-align: center;'>Upload an X-ray image to detect symptoms with bounding boxes.</p>
    <hr>
""", unsafe_allow_html=True)

# ---- FILE UPLOADER ----
uploaded_file = st.file_uploader("📤 Upload Chest X-ray (PNG, JPG, JPEG)", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    col1, col2 = st.columns([1, 1])

    # Display uploaded image
    with col1:
        st.image(uploaded_file, caption="Uploaded X-ray", use_column_width=True)
        st.write("✅ Image uploaded successfully!")

    with col2:
        st.subheader("⏳ Processing...")
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
        st.success("✅ Analysis Complete!")

        # ---- SIMULATED PREDICTION ----
        disease = np.random.choice(["Pneumonia", "Tuberculosis", "No Findings", "Lung Tumor"])
        confidence = np.random.uniform(80, 99)

        st.markdown(f"**🦠 Predicted Disease:** {disease}")
        st.markdown(f"**📊 Confidence Score:** {confidence:.2f}%")

        # ---- SHOWING BOUNDING BOX ----
        st.subheader("🖼️ Highlighted Region")
        image = Image.open(uploaded_file)
        image_np = np.array(image)
        x_min, y_min, x_max, y_max = 50, 50, 200, 200  # Simulated Box

        image_with_box = image_np.copy()
        cv2.rectangle(image_with_box, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        cv2.putText(image_with_box, f"{disease} ({confidence:.2f}%)",
                    (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        st.image(image_with_box, caption="Simulated Bounding Box", use_column_width=True)

# ---- FOOTER ----
st.markdown("""
    <hr>
    <p style='text-align: center;'>Developed with ❤️ using Streamlit</p>
""", unsafe_allow_html=True)