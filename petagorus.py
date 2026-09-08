<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Pythagoras Challenge</title>

    <style>
        * {
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            }

        .game {
            width: 90%;
             background: white;
            padding: 30px;
            border-radius: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.25);
            text-align: center;
        }

        h1 {
            color: #5b4bc4;
            margin-bottom: 5px;
        }

        .subtitle {
            color: #666;
            margin-bottom: 20px;
        }

        .info {
            display: flex;
            justify-content: space-between;
            background: #f1f3ff;
            padding: 12px 20px;
            border-radius: 15px;
            margin-bottom: 20px;
            font-weight: bold;
        }

        .question {
            font-size: 22px;
            font-weight: bold;
            margin: 25px 0;
            line-height: 1.5;
        }

        .triangle {
            margin: 20px auto;
            width: 0;
            height: 0;
            border-left: 100px solid transparent;
            border-bottom: 150px solid #667eea;
        }

        .answers {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }

        button {
            border: none;
            padding: 15px;
            border-radius: 12px;
            font-size: 18px;
            cursor: pointer;
            transition: 0.2s;
        }

        .answer {
            background: #e9e7ff;
            color: #333;
        }

        .answer:hover {
            background: #c9c4ff;
            transform: scale(1.03);
        }

        .start {
            background: #5b4bc4;
            color: white;
            padding: 15px 40px;
            font-size: 20px;
        }

        .start:hover {
            background: #4637a8;
        }

        .hidden {
            display: none;
        }

        #message {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
        }

        .correct {
            color: green;
        }

        .wrong {
            color: red;
        }

        .result {
            font-size: 25px;
            margin: 20px 0;
        }

        @media (max-width: 500px) {
            .answers {
                grid-template-columns: 1fr;
            }

            .game {
                padding: 20px;
            }
        }
    </style>
</head>

<body>

<div class="game">

    <!-- หน้าเริ่มเกม -->
    <div id="startScreen">
        <h1>📐 Pythagoras Challenge</h1>
        <p class="subtitle">
            เกมทายคำตอบทฤษฎีบทพีทาโกรัส
        </p>

        <p>🎯 ตอบคำถามให้ถูกต้องเพื่อสะสมคะแนน</p>
        <p>⏱️ มีเวลาข้อละ 15 วินาที</p>

        <button class="start" onclick="startGame()">
            🎮 เริ่มเล่นเกม
        </button>
    </div>


    <!-- หน้าเกม -->
    <div id="gameScreen" class="hidden">

        <h1>📐 Pythagoras Challenge</h1>

        <div class="info">
            <span>ข้อ: <span id="questionNumber">1</span>/5</span>
            <span>คะแนน: <span id="score">0</span></span>
            <span>เวลา: <span id="timer">15</span> วิ</span>
        </div>

        <div id="question" class="question"></div>

        <div id="answers" class="answers"></div>

        <div id="message"></div>

    </div>


    <!-- หน้าสรุปผล -->
    <div id="resultScreen" class="hidden">

        <h1>🏆 Game Over!</h1>

        <div class="result">
            คะแนนของคุณ
            <br>
            <strong>
                <span id="finalScore">0</span> / 5
            </strong>
        </div>

        <p id="resultMessage"></p>

        <button class="start" onclick="startGame()">
            🔄 เล่นอีกครั้ง
        </button>

    </div>

</div>


<script>

    // =========================
    // ข้อมูลคำถาม
    // =========================

    const questions = [
        {
            question: "สามเหลี่ยมมุมฉากมีด้านประกอบมุมฉากยาว 3 และ 4 หน่วย ด้านตรงข้ามมุมฉากยาวเท่าไร?",
            answers: ["5", "6", "7", "8"],
            correct: "5"
        },

        {
            question: "ถ้าด้านประกอบมุมฉากยาว 5 และ 12 หน่วย ด้านตรงข้ามมุมฉากยาวเท่าไร?",
            answers: ["10", "11", "13", "15"],
            correct: "13"
        },

        {
            question: "สามเหลี่ยมมุมฉากมีด้านตรงข้ามมุมฉากยาว 10 และอีกด้านหนึ่งยาว 6 หน่วย อีกด้านยาวเท่าไร?",
            answers: ["7", "8", "9", "10"],
            correct: "8"
        },

        {
            question: "ข้อใดคือสูตรทฤษฎีบทพีทาโกรัส?",
            answers: [
                "a² + b² = c²",
                "a + b = c",
                "a² - b² = c",
                "2a + 2b = c"
            ],
            correct: "a² + b² = c²"
        },

        {
            question: "ด้านของสามเหลี่ยมมุมฉากยาว 8, 15 และ 17 หน่วย ด้านใดเป็นด้านตรงข้ามมุมฉาก?",
            answers: ["8", "15", "17", "ทั้งสามด้าน"],
            correct: "17"
        }
    ];


    // =========================
    // ตัวแปรของเกม
    // =========================

    let currentQuestion = 0;
    let score = 0;
    let timeLeft = 15;
    let timer;


    // =========================
    // เริ่มเกม
    // =========================

    function startGame() {

        currentQuestion = 0;
        score = 0;

        document.getElementById("score").textContent = score;

        document.getElementById("startScreen")
            .classList.add("hidden");

        document.getElementById("resultScreen")
            .classList.add("hidden");

        document.getElementById("gameScreen")
            .classList.remove("hidden");

        showQuestion();
    }


    // =========================
    // แสดงคำถาม
    // =========================

    function showQuestion() {

        clearInterval(timer);

        timeLeft = 15;

        document.getElementById("timer").textContent = timeLeft;

        document.getElementById("questionNumber").textContent =
            currentQuestion + 1;

        const q = questions[currentQuestion];

        document.getElementById("question").textContent =
            q.question;

        const answersDiv =
            document.getElementById("answers");

        answersDiv.innerHTML = "";

        document.getElementById("message").textContent = "";

        // สร้างปุ่มคำตอบ
        q.answers.forEach(answer => {

            const button = document.createElement("button");

            button.textContent = answer;

            button.className = "answer";

            button.onclick = function() {
                checkAnswer(answer);
            };

            answersDiv.appendChild(button);
        });

        startTimer();
    }


    // =========================
    // ระบบจับเวลา
    // =========================

    function startTimer() {

        timer = setInterval(function() {

            timeLeft--;

            document.getElementById("timer").textContent =
                timeLeft;

            if (timeLeft <= 0) {

                clearInterval(timer);

                alert("⏰ หมดเวลา!");

                nextQuestion();
            }

        }, 1000);
    }


    // =========================
    // ตรวจคำตอบ
    // =========================

    function checkAnswer(answer) {

        clearInterval(timer);

        const correctAnswer =
            questions[currentQuestion].correct;

        // IF - ELSE
        if (answer === correctAnswer) {

            score++;

            document.getElementById("score").textContent =
                score;

            document.getElementById("message").innerHTML =
                "✅ ถูกต้อง! +1 คะแนน";

            document.getElementById("message").className =
                "correct";

            alert("🎉 ตอบถูก! ได้ +1 คะแนน");

        } else {

            document.getElementById("message").innerHTML =
                "❌ ผิด! คำตอบคือ " + correctAnswer;

            document.getElementById("message").className =
                "wrong";

            alert("❌ ตอบผิด!");
        }

        // ปิดปุ่มคำตอบ
        const buttons =
            document.querySelectorAll(".answer");

        buttons.forEach(button => {
            button.disabled = true;
        });

        setTimeout(nextQuestion, 1000);
    }


    // =========================
    // ไปข้อถัดไป
    // =========================

    function nextQuestion() {

        currentQuestion++;

        if (currentQuestion < questions.length) {

            showQuestion();

        } else {

            endGame();
        }
    }


    // =========================
    // จบเกม + IF ELSE ประเมินผล
    // =========================

    function endGame() {

        clearInterval(timer);

        document.getElementById("gameScreen")
            .classList.add("hidden");

        document.getElementById("resultScreen")
            .classList.remove("hidden");

        document.getElementById("finalScore").textContent =
            score;

        let message = "";

        // IF - ELSE
        if (score === 5) {

            message =
                "🏆 ระดับเทพ! คุณเข้าใจทฤษฎีบทพีทาโกรัสดีมาก!";

        } else if (score >= 3) {

            message =
                "🔥 เก่งมาก! แต่ยังฝึกเพิ่มได้อีกนิด";

        } else if (score >= 1) {

            message =
                "💪 พยายามอีกนิด แล้วจะเก่งขึ้นแน่นอน!";

        } else {

            message =
                "📚 ลองทบทวนทฤษฎีบทพีทาโกรัสแล้วเล่นใหม่!";
        }

        document.getElementById("resultMessage").textContent =
            message;
    }

st.write("นายธีรภัทร ยามวงศ์ ชั้น ม.4/2 เลขที่ 4
นายอินทรัตน์  สิงห์แก้ว เลขที่6 
นายสิรภพ ฝั้นถาวร เลขที่12 
นายตฤนภัทร แสงปรีดานนท์ เลขที่39")
