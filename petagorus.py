import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Pythagoras Challenge", page_icon="📐")

st.title("📐 Pythagoras Challenge")
st.write("เกมทายคำตอบทฤษฎีบทพีทาโกรัส")

# ข้อมูลคำถาม
questions = [
    {
        "question": "1. สามเหลี่ยมมุมฉากมีด้านประกอบมุมฉากยาว 3 และ 4 หน่วย ด้านตรงข้ามมุมฉากยาวเท่าไร?",
        "options": ["5", "6", "7", "8"],
        "correct": "5"
    },
    {
        "question": "2. ถ้าด้านประกอบมุมฉากยาว 5 และ 12 หน่วย ด้านตรงข้ามมุมฉากยาวเท่าไร?",
        "options": ["10", "11", "13", "15"],
        "correct": "13"
    },
    {
        "question": "3. สามเหลี่ยมมุมฉากมีด้านตรงข้ามมุมฉากยาว 10 และอีกด้านหนึ่งยาว 6 หน่วย อีกด้านยาวเท่าไร?",
        "options": ["7", "8", "9", "10"],
        "correct": "8"
    },
    {
        "question": "4. ข้อใดคือสูตรทฤษฎีบทพีทาโกรัส?",
        "options": ["a² + b² = c²", "a + b = c", "a² - b² = c", "2a + 2b = c"],
        "correct": "a² + b² = c²"
    },
    {
        "question": "5. ด้านของสามเหลี่ยมมุมฉากยาว 8, 15 และ 17 หน่วย ด้านใดเป็นด้านตรงข้ามมุมฉาก?",
        "options": ["8", "15", "17", "ทั้งสามด้าน"],
        "correct": "17"
    }
]

# ใช้ st.form เพื่อรวบรวมคำตอบและส่งทีเดียว
with st.form("quiz_form"):
    user_answers = []
    
    for idx, q in enumerate(questions):
        st.subheader(q["question"])
        choice = st.radio(
            "เลือกคำตอบ:",
            q["options"],
            key=f"q_{idx}",
            index=None
        )
        user_answers.append(choice)
        st.write("---")

    submitted = st.form_submit_button("ส่งคำตอบ 🎯")

if submitted:
    score = 0
    st.header("🏆 สรุปผลคะแนน")
    
    for idx, q in enumerate(questions):
        user_ans = user_answers[idx]
        if user_ans == q["correct"]:
            score += 1
            st.success(f"ข้อ {idx+1}: ถูกต้อง! (คำตอบ: {q['correct']})")
        else:
            st.error(f"ข้อ {idx+1}: ผิด! คุณตอบ '{user_ans if user_ans else 'ไม่ได้เลือก'}' (คำตอบที่ถูกต้อง: {q['correct']})")
            
    st.subheader(f"คะแนนรวมของคุณ: {score} / {len(questions)}")
    
    if score == 5:
        st.balloons()
        st.info("🏆 ระดับเทพ! คุณเข้าใจทฤษฎีบทพีทาโกรัสดีมาก!")
    elif score >= 3:
        st.info("🔥 เก่งมาก! แต่ยังฝึกเพิ่มได้อีกนิด")
    else:
        st.info("📚 ลองทบทวนทฤษฎีบทพีทาโกรัสแล้วลองใหม่อีกครั้ง!")
