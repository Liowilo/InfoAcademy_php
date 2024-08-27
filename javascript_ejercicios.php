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
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/codemirror.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/theme/dracula.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/mode/javascript/javascript.min.js"></script>
    <link rel="stylesheet" href="./assets/css/navbar.css">
    <link rel="stylesheet" href="./assets/css/ejercicios.css">
    <title>Ejercicios JavaScript</title>
</head>

<body>
    <?php include './components/navbar.php'; ?>

    <div class="container mt-5">
        <div class="row">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <h3 class="card-title text-white">Ejercicio JavaScript:</h3>
                        <div id="exercise-prompt" class="card-text text-white"></div>
                        <div id="difficulty-display" class="mt-2 text-white"></div>
                        <div class="mt-3">
                            <label for="difficulty-select" class="form-label text-white">Seleccionar dificultad:</label>
                            <select id="difficulty-select" class="form-select">
                                <option value="">Todas las dificultades</option>
                                <option value="1">Fácil</option>
                                <option value="2">Medio</option>
                                <option value="3">Difícil</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <h3 class="card-title text-white">Tu respuesta JavaScript:</h3>
                        <textarea id="user-answer" class="form-control"></textarea>
                        <button id="check-answer" class="btn btn-primary mt-3">Revisar respuesta</button>
                        <div id="feedback" class="mt-3"></div>
                        <button id="get-performance" class="btn btn-secondary mt-3">Ver rendimiento</button>
                        <div id="performance-display" class="mt-3"></div>
                        <div id="recommendation-display" style="display: none;" class="text-white"></div>
                        <button id="test-connection" class="btn btn-secondary mt-3">Probar conexión con el servidor</button>
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
            const difficultyDisplay = document.getElementById('difficulty-display');
            const difficultySelect = document.getElementById('difficulty-select');
            const userAnswer = document.getElementById('user-answer');
            const checkAnswerBtn = document.getElementById('check-answer');
            const feedback = document.getElementById('feedback');
            const performanceBtn = document.getElementById('get-performance');
            const performanceDisplay = document.getElementById('performance-display');
            const recommendationDisplay = document.getElementById('recommendation-display');

            let currentQuestion = '';
            let currentQuestionId = '';
            let startTime;

            const editor = CodeMirror.fromTextArea(userAnswer, {
                mode: "javascript",
                theme: "dracula",
                lineNumbers: true,
                autoCloseBrackets: true,
                matchBrackets: true,
                indentUnit: 2,
                tabSize: 2,
                indentWithTabs: false,
                extraKeys: {
                    "Ctrl-Space": "autocomplete"
                }
            });

            function typeWriter(element, text, speed = 50) {
                let i = 0;
                element.textContent = '';

                function type() {
                    if (i < text.length) {
                        element.textContent += text.charAt(i);
                        i++;
                        setTimeout(type, speed);
                    }
                }
                type();
            }

            function getNewQuestion() {
                const difficulty = difficultySelect.value;
                let url = 'http://localhost:5000/get_js_question';
                if (difficulty) {
                    url += `?difficulty=${difficulty}`;
                }
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        currentQuestionId = data.id;
                        currentQuestion = data.question;
                        typeWriter(exercisePrompt, currentQuestion);
                        difficultyDisplay.textContent = `Dificultad: ${getDifficultyText(data.difficulty)}`;
                        startTime = new Date();
                        editor.setValue(''); // Iniciar con el editor vacío
                        feedback.textContent = '';

                        editor.setOption('readOnly', true);
                        checkAnswerBtn.disabled = true;

                        setTimeout(() => {
                            editor.setOption('readOnly', false);
                            checkAnswerBtn.disabled = false;
                            editor.focus();
                        }, currentQuestion.length * 50 + 100);
                    });
            }

            function getDifficultyText(difficulty) {
                switch (difficulty) {
                    case 1:
                        return 'Fácil';
                    case 2:
                        return 'Medio';
                    case 3:
                        return 'Difícil';
                    default:
                        return 'Desconocido';
                }
            }

            function getRecommendation() {
                fetch(`http://localhost:5000/get_recommendation?user_id=<?php echo $user_data['id']; ?>`)
                    .then(response => response.json())
                    .then(data => {
                        if (data.error) {
                            console.error('Error:', data.error);
                        } else {
                            recommendationDisplay.textContent = `Recomendación: Enfócate en practicar ${data.recommendation}`;
                            recommendationDisplay.style.display = 'block';
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
            }

            getNewQuestion();
            getRecommendation();

            difficultySelect.addEventListener('change', getNewQuestion);

            checkAnswerBtn.addEventListener('click', function() {
                const endTime = new Date();
                const timeTaken = (endTime - startTime) / 1000; // Tiempo en segundos

                fetch('http://localhost:5000/check_js_answer', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            question_id: currentQuestionId,
                            answer: editor.getValue().trim(),
                            user_id: <?php echo $user_data['id']; ?>,
                            time_taken: timeTaken,
                            language_id: 3 // 3 para JavaScript
                        }),
                    })
                    .then(async response => {
                        const responseText = await response.text();
                        console.log('Respuesta completa del servidor:', responseText);
                        let data;
                        try {
                            data = JSON.parse(responseText);
                        } catch (error) {
                            console.error('Error parsing JSON:', responseText);
                            throw new Error('Respuesta del servidor no válida: ' + responseText);
                        }
                        if (!response.ok) {
                            throw new Error(JSON.stringify(data));
                        }
                        return data;
                    })
                    .then(data => {
                        let feedbackHtml = '';
                        if (data.error) {
                            if (data.error === "Error de sintaxis en el código") {
                                feedbackHtml = `<h4 style="color: red;">Error de sintaxis</h4>
                            <p>Tu código contiene errores de sintaxis. Por favor, revisa tu código y asegúrate de que sea JavaScript válido.</p>`;
                            } else {
                                feedbackHtml = `<h4 style="color: red;">Error: ${data.error}</h4>`;
                            }
                            if (data.details) {
                                feedbackHtml += `<details>
                                <summary>Detalles técnicos</summary>
                                <pre>${data.details}</pre>
                              </details>`;
                            }
                        } else if (data.is_correct) {
                            feedbackHtml = '<h4 style="color: green;">¡Correcto! Todos los casos de prueba pasaron.</h4>';
                        } else {
                            feedbackHtml = '<h4 style="color: red;">Incorrecto. Algunos casos de prueba fallaron.</h4>';
                        }

                        if (data.test_results) {
                            feedbackHtml += '<h5>Resultados detallados:</h5><ul>';
                            data.test_results.forEach((result, index) => {
                                if (result.error) {
                                    feedbackHtml += `<li style="color: red;">Error en el caso de prueba ${index + 1}: ${result.error}</li>`;
                                } else {
                                    const color = result.passed ? 'green' : 'red';
                                    feedbackHtml += `<li style="color: ${color};">
                    Caso de prueba ${index + 1}: 
                    Input: ${result.input}, 
                    Resultado esperado: ${result.expected}, 
                    Tu resultado: ${result.result}
                </li>`;
                                }
                            });
                            feedbackHtml += '</ul>';
                        }

                        feedback.innerHTML = feedbackHtml;
                    })
                    .catch(error => {
                        console.error('Error detallado:', error);
                        let errorMessage = 'Error desconocido';
                        let errorDetails = '';
                        try {
                            const errorData = JSON.parse(error.message);
                            errorMessage = errorData.error || errorMessage;
                            errorDetails = JSON.stringify(errorData, null, 2);
                        } catch (e) {
                            errorMessage = error.message;
                        }
                        feedback.innerHTML = `<h4 style="color: red;">Error al procesar la respuesta: ${errorMessage}</h4>
                          <details>
                            <summary>Detalles técnicos</summary>
                            <pre>${errorDetails}</pre>
                          </details>
                          <p>Por favor, intenta de nuevo. Si el problema persiste, contacta al soporte técnico.</p>`;
                    });
            });

            performanceBtn.addEventListener('click', function() {
                fetch(`http://localhost:5000/get_js_performance?user_id=<?php echo $user_data['id']; ?>`)
                    .then(response => response.json())
                    .then(data => {
                        if (data.error) {
                            performanceDisplay.textContent = `Error: ${data.error}`;
                            performanceDisplay.style.color = 'red';
                        } else {
                            const ejerciciosCompletados = data.ejercicios_completados || 0;
                            const tasaAciertos = (data.tasa_aciertos != null) ? (data.tasa_aciertos * 100).toFixed(2) : 'N/A';
                            const tiempoPromedio = (data.tiempo_promedio != null) ? data.tiempo_promedio.toFixed(2) : 'N/A';

                            performanceDisplay.innerHTML = `
                                <div style="color: white; text-align: left;">
                                    Ejercicios completados: ${ejerciciosCompletados}<br>
                                    Tasa de aciertos: ${tasaAciertos}%<br>
                                    Tiempo promedio: ${tiempoPromedio} segundos
                                </div>
                            `;
                        }
                        performanceDisplay.style.display = 'block';
                        performanceDisplay.style.opacity = '1';

                        setTimeout(() => {
                            performanceDisplay.classList.add('fade-out');
                            setTimeout(() => {
                                performanceDisplay.style.display = 'none';
                                performanceDisplay.classList.remove('fade-out');
                            }, 1000);
                        }, 4000);
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        performanceDisplay.textContent = 'Error al obtener el rendimiento';
                        performanceDisplay.style.color = 'red';
                        performanceDisplay.style.display = 'block';
                        performanceDisplay.style.opacity = '1';

                        setTimeout(() => {
                            performanceDisplay.classList.add('fade-out');
                            setTimeout(() => {
                                performanceDisplay.style.display = 'none';
                                performanceDisplay.classList.remove('fade-out');
                            }, 1000);
                        }, 4000);
                    });
            });
        });

        document.getElementById('test-connection').addEventListener('click', function() {
            fetch('http://localhost:5000/test')
                .then(response => response.json())
                .then(data => {
                    alert(data.message);
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Error al conectar con el servidor: ' + error.message);
                });
        });
    </script>
</body>

</html>