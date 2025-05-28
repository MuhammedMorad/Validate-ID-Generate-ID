import streamlit as st
from datetime import date
import random

st.set_page_config(page_title="Validate ID & Generate ID", layout="wide", page_icon="img/icon.ico")

# Title of the report
st.title("Validate ID & Generate ID ")
st.markdown(
    """
This project is an Egyptian National ID Validator and Generator built using Streamlit. It allows users to:

- **Validate** a 14-digit Egyptian National ID by analyzing personal information such as birth date, gender, and governorate.
- **Generate** a valid National ID based on user-provided birth date, gender, and governorate.
    """, unsafe_allow_html=True)

# Language options
tabs = {"en": "English", "ar": "العربية"}
lang = st.sidebar.selectbox("Select Language / اختر اللغة", options=list(tabs.keys()), format_func=lambda x: tabs[x])

# Add Font Awesome
st.markdown( 
"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"> 
""", 
unsafe_allow_html=True
)

# Text translations
i18n = {
    "title": {"en": "National ID Validator & Analyzer 🇪🇬", "ar": "مدقق ومحلل الرقم القومي 🇪🇬"},
    "tab_validate": {"en": "Validate ID", "ar": "التحقق من الرقم"},
    "tab_generate": {"en": "Generate ID", "ar": "إنشاء رقم"},
    "description": {
        "en": "Enter your 14-digit Egyptian National ID to validate and analyze personal information.",
        "ar": "أدخل الرقم القومي المكون من 14 رقمًا للتحقق وتحليل المعلومات الشخصية."
    },
    "input_label": {"en": "National ID Number:", "ar": "الرقم القومي:"},
    "button": {"en": "Validate and Analyze", "ar": "تحقق وحلل"},
    "success": {"en": "✅ National ID is valid.", "ar": "✅ الرقم القومي صالح."},
    "error_prefix": {"en": "🚫", "ar": "🚫"},
    "personal_info": {"en": "Personal Information:", "ar": "المعلومات الشخصية:"},
    "birth_date": {"en": "Birth Date", "ar": "تاريخ الميلاد"},
    "age": {"en": "Age", "ar": "العمر"},
    "gender": {"en": "Gender", "ar": "الجنس"},
    "governorate": {"en": "Governorate", "ar": "المحافظة"},
    "date_input": {"en": "Select Birth Date:", "ar": "اختر تاريخ الميلاد:"},
    "gender_input": {"en": "Select Gender:", "ar": "اختر الجنس:"},
    "governorate_input": {"en": "Select Governorate:", "ar": "اختر المحافظة:"},
    "generate_button": {"en": "Generate National ID", "ar": "إنشاء الرقم القومي"},
    "generated_id": {"en": "Generated National ID:", "ar": "الرقم القومي المولد:"},
    "footer":  {
        "en": """
        Developed By ❤️ Eng. Muhammed Mustafa Morad.  
        <a href='https://www.linkedin.com/in/muhammedmorad/' target='_blank'>
        <i class='fab fa-linkedin'></i> LinkedIn</a> | 
        <a href='https://www.facebook.com/mohamed.m.morad.811060/' target='_blank'>
        <i class='fab fa-facebook'></i> Facebook</a> | 
        <a href='https://github.com/MuhammedMorad' target='_blank'>
        <i class='fab fa-github'></i> GitHub</a> | 
        <a href='https://wa.me/201234567890' target='_blank'>
        <i class='fab fa-whatsapp'></i> WhatsApp</a>
        """,
        "ar": """
        تم التطوير بواسطة المهندس محمد مصطفى مراد ❤️  
        <a href='https://www.linkedin.com/in/muhammedmorad/' target='_blank'>
        <i class='fab fa-linkedin'></i> لينكدإن</a> | 
        <a href='https://www.facebook.com/mohamed.m.morad.811060/' target='_blank'>
        <i class='fab fa-facebook'></i> فيسبوك</a> | 
        <a href='https://github.com/MuhammedMorad' target='_blank'>
        <i class='fab fa-github'></i> جيت هاب</a> | 
        <a href='https://wa.me/201276717527' target='_blank'>
        <i class='fab fa-whatsapp'></i> واتساب</a>
        """
    }
}



# Governorate codes and values (corrected to two-digit strings)
gov_codes = ['01','02','03','04','11','12','13','14','15','16','17','18','19','21','22','23','24','25','26','27','28','29','31','32','33','34','35','88']
gov_info = {
    1: {"en":"Cairo","ar":"القاهرة"}, 2: {"en":"Alexandria","ar":"الإسكندرية"},
    3: {"en":"Port Said","ar":"بورسعيد"}, 4: {"en":"Suez","ar":"السويس"},
    11:{"en":"Damietta","ar":"دمياط"}, 12:{"en":"Dakahlia","ar":"الدقهلية"},
    13:{"en":"Eastern","ar":"الشرقية"}, 14:{"en":"Qalyubia","ar":"القليوبية"},
    15:{"en":"Kafr El-Sheikh","ar":"كفر الشيخ"}, 16:{"en":"Western","ar":"الغربية"},
    17:{"en":"Menoufia","ar":"المنوفية"}, 18:{"en":"Behera","ar":"البحيرة"},
    19:{"en":"Ismailia","ar":"الإسماعيلية"}, 21:{"en":"Giza","ar":"الجيزة"},
    22:{"en":"Beni-Suef","ar":"بني سويف"}, 23:{"en":"Fayoum","ar":"الفيوم"},
    24:{"en":"Menia","ar":"المنيا"}, 25:{"en":"Asyout","ar":"أسيوط"},
    26:{"en":"Suhag","ar":"سوهاج"}, 27:{"en":"Qena","ar":"قنا"},
    28:{"en":"Aswan","ar":"أسوان"}, 29:{"en":"Luxor","ar":"الأقصر"},
    31:{"en":"Red Sea","ar":"البحر الأحمر"}, 32:{"en":"ElWadi ElGidid","ar":"الوادي الجديد"},
    33:{"en":"Matrouh","ar":"مطروح"}, 34:{"en":"North Sinai","ar":"شمال سيناء"},
    35:{"en":"South Sinai","ar":"جنوب سيناء"}, 88:{"en":"Outside the Republic","ar":"خارج الجمهورية"}
}

# Validation function
def validate_national_id(national_id: str):
    national_id = national_id.replace(" ", "")
    if not national_id.isdigit():
        return False, {"en": "Invalid input. Please enter digits only.", "ar": "إدخال غير صالح. الرجاء إدخال أرقام فقط."}[lang]
    if len(national_id) > 14:
        return False, {"en": "Invalid National ID number: greater than 14 digits. Please check the number.", "ar": "الرقم القومي غير صالح: الرقم الذي ادخلتة اكبر من 14 رقم , يرجي التاكد من الرقم ."}[lang]
    if len(national_id) < 14:
        return False, {"en": "Invalid National ID number: Less than 14 digits. Please check the number..", "ar": "الرقم القومي غير صالح: الرقم الذي ادخلتة اصغر من 14 رقم , يرجي التاكد من الرقم ."}[lang]
    if national_id[0] not in ['2', '3']:
        return False, {"en": "Invalid National ID number: Incorrect format for date of birth.", "ar": "الرقم القومي غير صالح: صيغة تاريخ الميلاد غير صحيحة."}[lang]
    gov_code = national_id[7:9]
    if gov_code not in gov_codes:
        return False, {"en": "Invalid National ID number: Incorrect Governorate code.", "ar": "الرقم القومي غير صالح: رمز المحافظة غير صحيح."}[lang]
    return True, {"en": "National ID is valid.", "ar": "الرقم القومي صالح."}[lang]

# Analysis function
def analysis_national_id(national_id: str):
    yy, mm, dd = int(national_id[1:3]), int(national_id[3:5]), int(national_id[5:7])
    year = yy + (2000 if national_id[0]=='3' else 1900)
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (mm, dd))
    code = int(national_id[7:9])
    gov = gov_info.get(code, {"en":"Unknown","ar":"غير معروف"})[lang]
    gender = "Male" if int(national_id[12])%2 else "Female"
    gender_trans = {"en": gender, "ar": "ذكر" if gender=="Male" else "أنثى"}[lang]
    return {"birth_date": f"{dd:02d}/{mm:02d}/{year}", "age": age, "gender": gender_trans, "governorate": gov}

# ID generation function (no serial/random)
def generate_national_id(birth_date: date, gender: str, gov_code: str):
    year = birth_date.year
    century = '3' if year >= 2000 else '2'
    yy = f"{year%100:02d}"
    mm = f"{birth_date.month:02d}"
    dd = f"{birth_date.day:02d}"
    gov = gov_code
    gender_digit = '1' if gender=='Male' else '0'
    return century + yy + mm + dd + gov + gender_digit

# Streamlit UI with tabs
t1, t2 = st.tabs([i18n['tab_validate'][lang], i18n['tab_generate'][lang]])

with t1:
    st.header(i18n['tab_validate'][lang])
    st.write(i18n['description'][lang])
    id_input = st.text_input(i18n['input_label'][lang], key='val')
    if st.button(i18n['button'][lang], key='val_btn'):
        valid, msg = validate_national_id(id_input)
        if valid:
            res = analysis_national_id(id_input)
            st.success(i18n['success'][lang])
            st.write(i18n['personal_info'][lang])
            st.write(f"- {i18n['birth_date'][lang]}: {res['birth_date']}")
            st.write(f"- {i18n['age'][lang]}: {res['age']}")
            st.write(f"- {i18n['gender'][lang]}: {res['gender']}")
            st.write(f"- {i18n['governorate'][lang]}: {res['governorate']}")
        else:
            st.error(f"{i18n['error_prefix'][lang]} {msg}")

with t2:
    min_date = date(1900, 1, 1)
    max_date = date(2025, 12, 31)
    st.header(i18n['tab_generate'][lang])
    bd = st.date_input(
        i18n['date_input'][lang],
        value=date.today(),
        min_value=min_date,
        max_value=max_date,
        key='gen_date'
    )
    gender_opt = st.selectbox(i18n['gender_input'][lang], options=['Male','Female'], format_func=lambda x: {'Male':{'en':'Male','ar':'ذكر'}[lang], 'Female':{'en':'Female','ar':'أنثى'}[lang]}[x], key='gen_gender')
    gov_select = st.selectbox(i18n['governorate_input'][lang], options=gov_codes, format_func=lambda x: gov_info[int(x)][lang], key='gen_gov')
    if st.button(i18n['generate_button'][lang], key='gen_btn'):
        new_id = generate_national_id(bd, gender_opt, gov_select)
        st.success(f"{i18n['generated_id'][lang]} {new_id}")

st.markdown("---")
st.markdown(i18n['footer'][lang], unsafe_allow_html=True)


