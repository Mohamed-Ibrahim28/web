import streamlit as st
import time
import random

st.set_page_config(page_title="كل سنه وانتي طيبه يا رورو", layout="centered")

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

st.markdown("### اضغطي هنا يا قمرايه ❤️", unsafe_allow_html=True)

clicked = st.button("ايوا هنا يا بقره!")

if clicked:
    with st.spinner("استني يا عجوووووووزه... 😍"):
        time.sleep(1)

    st.markdown('<div class="big-text">كل سنه وانتي طيبه يا رورو وعقبال سنين كتير وانتي معانا وربنا يخليكي ليا دايما <br> احلى واحده تتم 24 سنه في الدنيا والله <br> happy birth day ya RoRo <br>على فكره بقالنا كتير مش بنتكلم زي زمان ومش بتحكيلي حاجه زي الاول بس والله مكانك في قلبي زي م هو ومش هيتغير  <br> I Love You So much ya my big sister🥰🥰🥰🥰🥰🥰🥰🥰</div>', unsafe_allow_html=True)

    # قلوب طايرة
    heart_emojis = ['💖', '💕', '💓', '💗', '💘', '💝', '❤️']
    for _ in range(15):
        line = "".join(random.choices(heart_emojis, k=random.randint(10, 20)))
        st.markdown(f"<div style='text-align:center;font-size:24px'>{line}</div>", unsafe_allow_html=True)
        time.sleep(0.2)
