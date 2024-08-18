<?php
session_start();
include("./connection.php");
include("./functions.php");

$user_data = check_login($con);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@4.3.0/fonts/remixicon.css" rel="stylesheet" />
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <link rel="stylesheet" href="./assets/css/navbar.css">
    <link rel="stylesheet" href="./assets/css/ejercicios.css">
    <title>Ejercicios HTML</title>
</head>

<body>
    <?php include './components/navbar.php'; ?>

    <div class="container mt-5">
        <div class="row">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <h3 class="card-title text-white">Ejercicio:</h3>
                        <div id="exercise-prompt" class="card-text text-white"></div>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <h3 class="card-title text-white">Tu respuesta:</h3>
                        <textarea id="user-answer" class="form-control" rows="10"></textarea>
                        <button id="check-answer" class="btn btn-primary mt-3">Revisar respuesta</button>
                        <div id="feedback" class="mt-3"></div>
                        <button id="get-performance" class="btn btn-secondary mt-3">Ver rendimiento</button>
                        <div id="performance-display" class="mt-3"></div>
                        <div id="feedback" class="mt-3"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const exercisePrompt = document.getElementById('exercise-prompt');
            const userAnswer = document.getElementById('user-answer');
            const checkAnswerBtn = document.getElementById('check-answer');
            const feedback = document.getElementById('feedback');
            const performanceBtn = document.getElementById('get-performance');
            const performanceDisplay = document.getElementById('performance-display');

            let currentQuestion = '';
            let startTime;

            function getNewQuestion() {
                fetch('http://localhost:5000/get_question')
                    .then(response => response.json())
                    .then(data => {
                        currentQuestion = data.question;
                        exercisePrompt.textContent = currentQuestion;
                        startTime = new Date();
                        userAnswer.value = '';
                    });
            }

            getNewQuestion();

            checkAnswerBtn.addEventListener('click', function() {
                const endTime = new Date();
                const timeTaken = (endTime - startTime) / 1000; // Tiempo en segundos

                fetch('http://localhost:5000/check_answer', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            question: currentQuestion,
                            answer: userAnswer.value,
                            user_id: 1, // Asume un ID de usuario fijo por ahora
                            time_taken: timeTaken
                        }),
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.is_correct) {
                            feedback.textContent = '¡Correcto!';
                            feedback.style.color = 'green';
                        } else {
                            feedback.textContent = `Incorrecto. La respuesta correcta es: ${data.correct_answer}`;
                            feedback.style.color = 'red';
                        }
                        getNewQuestion();
                    });
            });

            performanceBtn.addEventListener('click', function() {
                fetch('http://localhost:5000/get_performance?user_id=1') // Asume un ID de usuario fijo por ahora
                    .then(response => response.json())
                    .then(data => {
                        performanceDisplay.textContent = `Ejercicios completados: ${data.ejercicios_completados}, 
                                                  Tasa de aciertos: ${(data.tasa_aciertos * 100).toFixed(2)}%, 
                                                  Tiempo promedio: ${data.tiempo_promedio.toFixed(2)} segundos`;
                    });
            });
        });
    </script>
</body>

</html>