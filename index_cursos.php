<?php
session_start();
include("connection.php");
include("functions.php");

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
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/themes/prism-tomorrow.min.css" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/components/prism-markup.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/components/prism-css.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/components/prism-javascript.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12/lib/typed.min.js"></script>
    <link rel="stylesheet" href="./assets/css/footer.css">
    <link rel="stylesheet" href="./assets/css/course-style.css">
    <title>InfoAcademy Cursos</title>
</head>

<body>

    <?php include './components/navbar.php'; ?>

    <!--Cursos Navbar -->
    <nav class="navbar second-navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav mx-auto">
                    <li class="nav-item"><a class="nav-link" href="#">HTML</a></li>
                    <li class="nav-item"><a class="nav-link" href="#">CSS</a></li>
                    <li class="nav-item"><a class="nav-link" href="#">JAVASCRIPT</a></li>
                    <li class="nav-item"><a class="nav-link" href="#">PYTHON</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section">
        <div id="particles-js"></div>
        <div class="container text-center d-flex flex-column justify-content-center align-items-center">
            <h1 class="display-4">Aprende a programar...</h1>
            <p class="lead">Adéntrate en InfoAcademy para ser un mejor programador.</p>
            <form class="d-flex justify-content-center search-form">
                <input class="form-control me-2 search-input" type="search" placeholder="Busca tutoriales, e.j HTML" aria-label="Search">
                <button class="btn btn-success search-button" type="submit">Buscar</button>
            </form>
        </div>
    </section>

    <!-- Main Content Section -->

    <!-- HMTL -->
    <section class="main-content html-section">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-md-6 text-center">
                    <h1 class="display-1 fw-bold">HTML<i class="ri-html5-fill"></i></h1>
                    <p>El lenguaje para construir páginas web🛠</p>
                    <a href="#" class="btn btn-success rounded-pill mb-2">Aprende HTML</a>
                    <br>
                    <a href="#" class="btn btn-warning text-white rounded-pill mb-2">Ejercicios con HTML</a>
                    <br>
                    <a href="#" class="btn btn-dark rounded-pill mb-2">Referencia HTML</a>
                    <br>
                </div>
                <div class="col-md-6">
                    <div class="bg-dark text-light p-3 rounded">
                        <h5 class="text-white">HTML Ejemplo:</h5>
                        <pre><code id="typed" class="language-markup"></code></pre>
                        <a href="#" class="btn btn-success mt-3">Pruébalo tú mismo...</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CSS -->
    <section class="main-content css-section">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-md-6 text-center">
                    <h1 class="display-1 fw-bold">CSS<i class="ri-css3-fill"></i></h1>
                    <p>El lenguaje para estilizar páginas web🖌</p>
                    <a href="#" class="btn btn-success rounded-pill mb-2">Aprende CSS</a>
                    <br>
                    <a href="#" class="btn btn-warning text-white rounded-pill mb-2">Ejercicios con CSS</a>
                    <br>
                    <a href="#" class="btn btn-dark rounded-pill mb-2">Referencia CSS</a>
                    <br>
                </div>
                <div class="col-md-6">
                    <div class="bg-dark text-light p-3 rounded">
                        <h5 class="text-white">CSS Ejemplo:</h5>
                        <pre><code class="language-css">body {
    background-color: lightblue;
}

h1 {
    color: white;
    text-align: center;
}

p {
    font-family: verdana;
}</code></pre>
                        <a href="#" class="btn btn-success mt-3">Pruébalo tú mismo...</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- JAVASCRIPT -->
    <section class="main-content js-section">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-md-6 text-center">
                    <h1 class="display-1 fw-bold">JavaScript<i class="ri-javascript-fill"></i></h1>
                    <p>El lenguaje para dar vida a las páginas web❤</p>
                    <a href="#" class="btn btn-success rounded-pill mb-2">Aprende JavaScript</a>
                    <br>
                    <a href="#" class="btn btn-warning text-white rounded-pill mb-2">Ejercicios con JavaScript</a>
                    <br>
                    <a href="#" class="btn btn-dark rounded-pill mb-2">Referencia JavaScript</a>
                    <br>
                </div>
                <div class="col-md-6">
                    <div class="bg-dark text-light p-3 rounded">
                        <h5 class="text-white">JavaScript Ejemplo:</h5>
                        <pre><code class="language-javascript">function sumar(a, b) {
    return a + b;
}

let resultado = sumar(5, 3);
console.log("El resultado es: " + resultado); // El resultado es: 8
</code></pre>
                        <a href="#" class="btn btn-success mt-3">Pruébalo tú mismo...</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- PYTHON -->
    <section class="main-content python-section">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-md-6 text-center">
                    <h1 class="display-1 fw-bold">Python<i class="ri-terminal-box-fill"></i></i></h1>
                    <p>El lenguaje para ideal para la ciencia de datos🔬📚📈</p>
                    <a href="#" class="btn btn-success rounded-pill mb-2">Aprende Python</a>
                    <br>
                    <a href="#" class="btn btn-warning text-white rounded-pill mb-2">Ejercicios con Python</a>
                    <br>
                    <a href="#" class="btn btn-dark rounded-pill mb-2">Referencia Python</a>
                    <br>
                </div>
                <div class="col-md-6">
                    <div class="bg-dark text-light p-3 rounded">
                        <h5 class="text-white">Python Ejemplo:</h5>
                        <pre><code class="language-python"># Definición de una función para sumar dos números
def sumar(a, b):
    """
    Esta función recibe dos números como parámetros
    y devuelve su suma.
    """
    resultado = a + b
    return resultado

# Definición de variables
numero1 = 5
numero2 = 3

# Llamada a la función y almacenamiento del resultado
suma = sumar(numero1, numero2)

# Impresión del resultado en la consola
print(f"La suma de {numero1} y {numero2} es: {suma}")

</code></pre>
                        <a href="#" class="btn btn-success mt-3">Pruébalo tú mismo...</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <?php include './components/footer.php'; ?>
    <script>
        Prism.highlightAll();
    </script>

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="./assets/js/main.js"></script>
    <script src="./assets/js/particles.js"></script>
    <script src="./assets/js/typed.js"></script>
</body>

</html>