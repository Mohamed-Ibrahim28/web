import streamlit as st
import time
import random

st.set_page_config(page_title="حب رنا", layout="centered")

# شوية ستايل رومانسي
st.markdown("""
    <style>
        .stButton button {
            font-size: 32px;
            padding: 1em 2em;
            background-color: #ff4b4b;
            color: white;
            border: none;
            border-radius: 15px;
            box-shadow: 0 0 15px pink;
            transition: 0.3s;
        }

        .stButton button:hover {
            background-color: #ff1a1a;
            box-shadow: 0 0 30px red;
            transform: scale(1.1);
        }

        .big-text {
            font-size: 60px;
            color: #ff0066;
            text-align: center;
            font-weight: bold;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.1); opacity: 1; }
            100% { transform: scale(1); opacity: 0.8; }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("### اضغطي هنا يا حياتي ❤️", unsafe_allow_html=True)

clicked = st.button(" ايوا هنا يا رنوشتي!")

if clicked:
    with st.spinner("لحظة رومانسية واحدة... 😍"):
        time.sleep(1)

    st.markdown('<div class="big-text">بحبك يا رنا وربنا يخليكي ليا يا حبيبتي❤️</div>', unsafe_allow_html=True)

    # قلوب طايرة
    heart_emojis = ['💖', '💕', '💓', '💗', '💘', '💝', '❤️']
    for _ in range(15):
        line = "".join(random.choices(heart_emojis, k=random.randint(10, 20)))
        st.markdown(f"<div style='text-align:center;font-size:24px'>{line}</div>", unsafe_allow_html=True)
        time.sleep(0.2)
