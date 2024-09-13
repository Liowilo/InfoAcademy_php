<!-- navbar.php -->
<nav class="navbar navbar-expand-lg sticky-top" style="background-color: #212f45;">
    <div class="container-fluid">
        <a class="navbar-brand logos-left" href="#">
            <img src="./assets/images/logoUNAM.webp" alt="" width="50" height="auto">
            <img src="./assets/images/logoInformatica.webp" alt="" width="55" height="auto">
            <img src="./assets/images/InfoAcademy_transparent.webp" width="85" height="auto" alt="">
        </a>
        <button class="navbar-toggler bg-white" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="user-name">
                    <p>Hola!, <?php echo $user_data['user_name']; ?> ^-^ </p>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Tutoriales
                        <i class="ri-video-fill"></i>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="#">HTML</a></li>
                        <li><a class="dropdown-item" href="#">CSS</a></li>
                        <li><a class="dropdown-item" href="#">JavaScript</a></li>
                        <li><a class="dropdown-item" href="#">Python</a></li>
                        <li>
                            <hr class="dropdown-divider">
                        </li>
                        <li><a class="dropdown-item" href="#">Something else here</a></li>
                    </ul>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Ejercicios
                        <i class="ri-code-box-fill"></i>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="/infoAcademy_php/html_ejercicios.php">HTML</a></li>
                        <li><a class="dropdown-item" href="/infoAcademy_php/css_ejercicios.php">CSS</a></li>
                        <li><a class="dropdown-item" href="/infoAcademy_php/javascript_ejercicios.php">JavaScript</a></li>
                        <li><a class="dropdown-item" href="/infoAcademy_php/python_ejercicios.php">Python</a></li>
                    </ul>
                </li>
            </ul>
            <a href="logout.php" class="btn btn-brand ms-lg-3">Cerrar sesión</a>
        </div>
    </div>
</nav>