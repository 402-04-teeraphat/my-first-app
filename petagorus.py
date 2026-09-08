import time

# ข้อมูลคำถาม
questions = [
    {
        "question": "สามเหลี่ยมมุมฉากมีด้านประกอบมุมฉากยาว 3 และ 4 หน่วย ด้านตรงข้ามมุมฉากยาวเท่าไร?",
        "answers": ["1. 5", "2. 6", "3. 7", "4. 8"],
        "correct": "1"
    },
    {
        "question": "ถ้าด้านประกอบมุมฉากยาว 5 และ 12 หน่วย ด้านตรงข้ามมุมฉากยาวเท่าไร?",
        "answers": ["1. 10", "2. 11", "3. 13", "4. 15"],
        "correct": "3"
    },
    {
        "question": "สามเหลี่ยมมุมฉากมีด้านตรงข้ามมุมฉากยาว 10 และอีกด้านหนึ่งยาว 6 หน่วย อีกด้านยาวเท่าไร?",
        "answers": ["1. 7", "2. 8", "3. 9", "4. 10"],
        "correct": "2"
    },
    {
        "question": "ข้อใดคือสูตรทฤษฎีบทพีทาโกรัส?",
        "answers": ["1. a² + b² = c²", "2. a + b = c", "3. a² - b² = c", "4. 2a + 2b = c"],
        "correct": "1"
    },
    {
        "question": "ด้านของสามเหลี่ยมมุมฉากยาว 8, 15 และ 17 หน่วย ด้านใดเป็นด้านตรงข้ามมุมฉาก?",
        "answers": ["1. 8", "2. 15", "3. 17", "4. ทั้งสามด้าน"],
        "correct": "3"
    }
]

def start_game():
    score = 0
    total_questions = len(questions)

    print("=" * 40)
    print("📐 Pythagoras Challenge")
    print("เกมทายคำตอบทฤษฎีบทพีทาโกรัส")
    print("=" * 40)
    print("🎯 ตอบคำถามโดยการพิมพ์หมายเลขข้อ 1-4")
    print()

    for idx, q in enumerate(questions, 1):
        print(f"\nข้อ {idx}/{total_questions}: {q['question']}")
        for ans in q["answers"]:
            print(f"  {ans}")
        
        user_answer = input("\nคำตอบของคุณ (1-4): ").strip()

        if user_answer == q["correct"]:
            print("✅ ถูกต้อง! +1 คะแนน")
            score += 1
        else:
            print(f"❌ ผิด! คำตอบที่ถูกต้องคือข้อ {q['correct']}")

    # สรุปผล
    print("\n" + "=" * 40)
    print(f"🏆 Game Over! คะแนนของคุณ: {score} / {total_questions}")
    print("=" * 40)

    if score == 5:
        print("🏆 ระดับเทพ! คุณเข้าใจทฤษฎีบทพีทาโกรัสดีมาก!")
    elif score >= 3:
        print("🔥 เก่งมาก! แต่ยังฝึกเพิ่มได้อีกนิด")
    elif score >= 1:
        print("💪 พยายามอีกนิด แล้วจะเก่งขึ้นแน่นอน!")
    else:
        print("📚 ลองทบทวนทฤษฎีบทพีทาโกรัสแล้วเล่นใหม่!")

if __name__ == "__main__":
    start_game()
