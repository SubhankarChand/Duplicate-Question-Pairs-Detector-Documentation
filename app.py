import streamlit as st
import helper
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Page Config
st.set_page_config(page_title="Duplicate Question Detector", page_icon="🔄", layout="centered")

# Custom CSS for a better UI
st.markdown("""
    <style>
        /* General Page Styles */
        body {
            background-color: #121212;
        }
        .main {
            background-color: #121212;
        }

        /* Title Styling */
        .title-container {
            text-align: center;
            padding: 15px;
        }
        .title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #00ccff;
            text-shadow: 2px 2px 8px rgba(0, 204, 255, 0.5);
        }

        
        
        .stTextInput > div > div > input {
            background-color: #262626 !important;
            color: #ffffff !important;
            font-size: 1.1rem;
            border-radius: 10px;
            padding: 12px;
            transition: 0.3s ease-in-out;
            border: 2px solid #444;
        }
        .stTextInput > div > div > input:focus {
            border: 2px solid #00ccff !important;
            box-shadow: 0 0 8px rgba(0, 204, 255, 0.7);
        }

        /* Button Styling */
        .stButton button {
            background-color: #0077cc;
            color: white;
            padding: 12px 30px;
            border-radius: 10px;
            font-size: 1.2rem;
            transition: 0.3s;
            box-shadow: 0px 4px 8px rgba(0, 119, 204, 0.3);
        }
        .stButton button:hover {
            background-color: #005fa3;
            box-shadow: 0px 6px 12px rgba(0, 119, 204, 0.5);
            transform: scale(1.05);
        }

        /* Result Box */
        .result-box {
            font-size: 1.5rem;
            font-weight: 600;
            text-align: center;
            padding: 15px;
            border-radius: 10px;
            animation: fadeIn 0.5s ease-in-out;
        }
        .duplicate {
            background-color: #d4edda;
            color: #155724;
        }
        .not-duplicate {
            background-color: #f8d7da;
            color: #721c24;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0px); }
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title-container'><div class='title'>🔁 Duplicate Question Detector</div></div>", unsafe_allow_html=True)

# Input Fields in a Neat Box
st.markdown("<div class='input-box'>", unsafe_allow_html=True)

q1 = st.text_input("📝 Enter Question 1", placeholder="Type the first question here")
q2 = st.text_input("📝 Enter Question 2", placeholder="Type the second question here")

submit = st.button("🔍 Check for Duplicate")

st.markdown("</div>", unsafe_allow_html=True)

# Display result
if submit:
    if q1.strip() == "" or q2.strip() == "":
        st.warning("⚠️ Please enter both questions to proceed.")
    else:
        query = helper.query_point_creator(q1, q2)
        result = model.predict(query)[0]

        if result:
            st.markdown("<div class='result-box duplicate'>✅ These questions are Duplicate.</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result-box not-duplicate'>❌ These questions are Not Duplicate.</div>", unsafe_allow_html=True)
