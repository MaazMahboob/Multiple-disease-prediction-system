{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b271ed7c-b34f-47c6-9d8f-1350cde53863",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\dell\\anaconda3\\lib\\site-packages (1.30.0)\n",
      "Requirement already satisfied: numpy in c:\\users\\dell\\anaconda3\\lib\\site-packages (1.26.4)\n",
      "Requirement already satisfied: opencv-python in c:\\users\\dell\\anaconda3\\lib\\site-packages (4.9.0.80)\n",
      "Requirement already satisfied: pillow in c:\\users\\dell\\anaconda3\\lib\\site-packages (10.4.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: importlib-metadata<8,>=1.4 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (7.0.1)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (2.1.4)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pyarrow>=6.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (14.0.2)\n",
      "Requirement already satisfied: python-dateutil<3,>=2.7.3 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (13.3.5)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (4.9.0)\n",
      "Requirement already satisfied: tzlocal<6,>=1.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (2.1)\n",
      "Requirement already satisfied: validators<1,>=0.2 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (0.18.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (3.1.37)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (6.3.3)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
      "Requirement already satisfied: toolz in c:\\users\\dell\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\dell\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from importlib-metadata<8,>=1.4->streamlit) (3.17.0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from python-dateutil<3,>=2.7.3->streamlit) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from validators<1,>=0.2->streamlit) (5.1.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\dell\\anaconda3\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit numpy opencv-python pillow\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3bcca540-ae43-4f9f-bc09-96673f40c37f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-27 00:24:37.219 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Dell\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import time\n",
    "import numpy as np\n",
    "import cv2\n",
    "from PIL import Image\n",
    "\n",
    "# Ensure Streamlit is installed\n",
    "try:\n",
    "    import streamlit as st\n",
    "except ModuleNotFoundError:\n",
    "    print(\"Error: Streamlit is not installed. Please install it using 'pip install streamlit'\")\n",
    "    exit()\n",
    "\n",
    "# ---- PAGE CONFIG ----\n",
    "st.set_page_config(page_title=\"AI Disease Detection\", page_icon=\"🩺\", layout=\"wide\")\n",
    "\n",
    "# ---- SIDEBAR NAVIGATION ----\n",
    "st.sidebar.title(\"🔍 AI Disease Detection\")\n",
    "st.sidebar.write(\"Upload a Chest X-ray to analyze possible symptoms.\")\n",
    "\n",
    "dark_mode = st.sidebar.checkbox(\"🌙 Dark Mode\")\n",
    "\n",
    "# ---- HEADER ----\n",
    "st.markdown(\"\"\"\n",
    "    <h1 style='text-align: center; color: #4CAF50;'>AI-Powered Chest X-ray Analysis</h1>\n",
    "    <p style='text-align: center;'>Upload an X-ray image to detect symptoms with bounding boxes.</p>\n",
    "    <hr>\n",
    "\"\"\", unsafe_allow_html=True)\n",
    "\n",
    "# ---- FILE UPLOADER ----\n",
    "uploaded_file = st.file_uploader(\"📤 Upload Chest X-ray (PNG, JPG, JPEG)\", type=['png', 'jpg', 'jpeg'])\n",
    "\n",
    "if uploaded_file:\n",
    "    col1, col2 = st.columns([1, 1])\n",
    "    \n",
    "    # Display uploaded image\n",
    "    with col1:\n",
    "        st.image(uploaded_file, caption=\"Uploaded X-ray\", use_column_width=True)\n",
    "        st.write(\"✅ Image uploaded successfully!\")\n",
    "    \n",
    "    with col2:\n",
    "        st.subheader(\"⏳ Processing...\")\n",
    "        progress_bar = st.progress(0)\n",
    "        for i in range(100):\n",
    "            time.sleep(0.02)\n",
    "            progress_bar.progress(i + 1)\n",
    "        st.success(\"✅ Analysis Complete!\")\n",
    "        \n",
    "        # ---- SIMULATED PREDICTION ----\n",
    "        disease = np.random.choice([\"Pneumonia\", \"Tuberculosis\", \"No Findings\", \"Lung Tumor\"])\n",
    "        confidence = np.random.uniform(80, 99)\n",
    "        \n",
    "        st.markdown(f\"**🦠 Predicted Disease:** {disease}\")\n",
    "        st.markdown(f\"**📊 Confidence Score:** {confidence:.2f}%\")\n",
    "        \n",
    "        # ---- SHOWING BOUNDING BOX ----\n",
    "        st.subheader(\"🖼️ Highlighted Region\")\n",
    "        image = Image.open(uploaded_file)\n",
    "        image_np = np.array(image)\n",
    "        x_min, y_min, x_max, y_max = 50, 50, 200, 200  # Simulated Box\n",
    "        \n",
    "        image_with_box = image_np.copy()\n",
    "        cv2.rectangle(image_with_box, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)\n",
    "        cv2.putText(image_with_box, f\"{disease} ({confidence:.2f}%)\", \n",
    "                    (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)\n",
    "        st.image(image_with_box, caption=\"Simulated Bounding Box\", use_column_width=True)\n",
    "\n",
    "# ---- FOOTER ----\n",
    "st.markdown(\"\"\"\n",
    "    <hr>\n",
    "    <p style='text-align: center;'>Developed with ❤️ using Streamlit</p>\n",
    "\"\"\", unsafe_allow_html=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "edf66020-3de0-4af1-92cf-8819605c484f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
