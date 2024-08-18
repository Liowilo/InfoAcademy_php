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
        const timeTaken = (endTime - startTime) / 1000;  // Tiempo en segundos

        fetch('http://localhost:5000/check_answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: currentQuestion,
                answer: userAnswer.value,
                user_id: 1,  // Asume un ID de usuario fijo por ahora
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
        fetch('http://localhost:5000/get_performance?user_id=1')  // Asume un ID de usuario fijo por ahora
            .then(response => response.json())
            .then(data => {
                performanceDisplay.textContent = `Ejercicios completados: ${data.ejercicios_completados}, 
                                                  Tasa de aciertos: ${(data.tasa_aciertos * 100).toFixed(2)}%, 
                                                  Tiempo promedio: ${data.tiempo_promedio.toFixed(2)} segundos`;
            });
    });
});