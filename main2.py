import streamlit as st
from PIL import Image
import os
import base64

# إعدادات الصفحة
st.set_page_config(
    page_title="لرنوشتي حبيبتي",
    page_icon="❤️",
    layout="centered"
)

# CSS مخصص للثيم الرومانسي
def set_romantic_theme():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: linear-gradient(to right, #ffafbd, #ffc3a0);
            color: #5d001e;
        }
        .stButton>button {
            background-color: #d4a5a5;
            color: #5d001e;
            border: 2px solid #5d001e;
            border-radius: 20px;
            padding: 10px 24px;
            font-size: 18px;
            font-weight: bold;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #5d001e;
            color: #ffafbd;
            border: 2px solid #d4a5a5;
        }
        .title {
            font-family: 'Arial', sans-serif;
            color: #5d001e;
            text-align: center;
            font-size: 36px;
            margin-bottom: 30px;
        }
        .heart {
            color: #e75480;
            font-size: 24px;
        }
        .audio-container {
            display: none; /* لإخفاء مشغل الصوت الافتراضي */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_romantic_theme()

# العنوان الرئيسي
st.markdown('<h1 class="title">لرنوشتي حبيبتي <span class="heart">❤️</span></h1>', unsafe_allow_html=True)

# حالة التطبيق
if 'show_second_button' not in st.session_state:
    st.session_state.show_second_button = False
if 'show_image' not in st.session_state:
    st.session_state.show_image = False

# الزر الأول
if st.button('اضغطي هنا يارنوشتي ❤️'):
    st.session_state.show_second_button = True
    st.balloons()
    st.success('براااااحه يابتتتتتتت')

# الزر الثاني يظهر بعد النقر على الأول
if st.session_state.show_second_button:
    if st.button('اضغطي هنا كمان معلش هتعب صوابعك القمر 💖'):
        st.session_state.show_image = True
        st.markdown('<h2 style="text-align: center; color: #5d001e;"> مزتي الحلوه الي مش هتزعل ولا هتتضايق وهتفك عشاني صح؟</h2>', unsafe_allow_html=True)

# عرض الصورة والمحتوى بعد النقر على الزر الثاني
if st.session_state.show_image:
    try:
        # تحميل الصورة المحلية
        image_path = "WhatsApp Image 2025-05-18 at 3.15.07 PM.jpeg"
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption='رنوشتي حبيبتي', use_column_width=True)
        else:
            st.error("لم يتم العثور على الصورة المطلوبة")
        
        # تشغيل أغنية رومانسية في الخلفية
        audio_path = r"F:\Mido\fun\web\romantic_song.m4a"
        if os.path.exists(audio_path):
            # قراءة الملف الصوتي
            with open(audio_path, 'rb') as audio_file:            
                audio_bytes = audio_file.read()

            st.markdown('''<h2 style="text-align: center; color: #5d001e;"> 
                        يا قمر يا أحلى حاجة في حياتي..

يا اللي ضحكتك بتخليني أنسى كل هموم الدنيا..

والله يا حبيبتي لو عينيكي شافت قد إيه قلبي بيوجعني لما تكوني زعلانة..
                        
مش عارف أعيش يوم من غير ما أشوف ضحكتك الحلوة دي..

كل حاجة في حياتي بقت حلوه بس لأنك فيها..
                        
حتى لو قولتي السما مش زرقاء، هقولك "أكيد رنوشتي صح" 😂❤️

بس متبقيش زعلانة.. أنا هنا.. دايمًا جنبك..
                        
"إنتي حبيبتي، غرامي، وعمري كله".. ❤️ </h2>''', unsafe_allow_html=True)
            # JavaScript لتشغيل الصوت تلقائياً من الثانية 34


            st.markdown('<h2 style="text-align: center; color: #5d001e;"> الاغنيه دي اقل حاجه ممكن تعبر عن الي جوايا وكل كلمه بجد فيها جوايا  </h2>', unsafe_allow_html=True)
            autoplay_audio = f"""
            <audio id="romanticAudio" controls autoplay style="display:none">
                <source src="data:audio/m4a;base64,{base64.b64encode(audio_bytes).decode()}" type="audio/m4a">
            </audio>
            <script>
                document.addEventListener('DOMContentLoaded', function() {{
                    var audio = document.getElementById('romanticAudio');
                    audio.currentTime = 34; // البدء من الثانية 34
                    audio.play();
                }});
            </script>
            """
            st.markdown(autoplay_audio, unsafe_allow_html=True)
            
            # مشغل صوتي ظاهر للتحكم إذا لزم الأمر
            st.markdown('''
            <style>
            .stAudio {
                width: 100%;
                max-width: 600px;
                margin: 20px auto;
            }
            </style>
            ''', unsafe_allow_html=True)
            
            st.audio(audio_bytes, format='audio/m4a', start_time=34)

        else:
            st.warning(f"لم يتم العثور على الملف الصوتي في المسار: {audio_path}")
            
        st.markdown('<h2 style="text-align: center; color: #5d001e;"> يارب اكون فرحتك ورسمت الابتسامه على وشك ياروحي بحبك اويييي </h2>', unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"حدث خطأ: {str(e)}")