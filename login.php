<?php
session_start();
include("connection.php");
include("functions.php");

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    if (isset($_POST['form_type']) && $_POST['form_type'] == 'register') {
        // Registro
        $user_name_register = $_POST['user_name_register'];
        $email_register = $_POST['email_register'];
        $password_register = $_POST['password_register'];

        if (!empty($user_name_register) && !empty($email_register) && !empty($password_register) && !is_numeric($user_name_register)) {
            // Primero, verifica si el correo ya existe
            $check_email_query = "SELECT * FROM users WHERE email = ?";
            $check_stmt = mysqli_prepare($con, $check_email_query);
            mysqli_stmt_bind_param($check_stmt, "s", $email_register);
            mysqli_stmt_execute($check_stmt);
            mysqli_stmt_store_result($check_stmt);

            if (mysqli_stmt_num_rows($check_stmt) > 0) {
                // El correo ya existe
                echo "<script>alert('Este correo electrónico ya está registrado.');</script>";
            } else {
                // El correo no existe, proceder con el registro
                $user_id = random_num(20);
                $hashed_password = password_hash($password_register, PASSWORD_DEFAULT);

                // Using prepared statements to prevent SQL injection
                $query = "INSERT INTO users (user_id, user_name, email, password) VALUES (?, ?, ?, ?)";
                if ($stmt = mysqli_prepare($con, $query)) {
                    mysqli_stmt_bind_param($stmt, "ssss", $user_id, $user_name_register, $email_register, $hashed_password);
                    if (mysqli_stmt_execute($stmt)) {
                        echo "<script>
                            alert('¡Cuenta creada exitosamente!');
                            window.location.href = 'login.php';
                          </script>";
                        exit();
                    } else {
                        echo "<script>alert('Error al ejecutar la consulta: " . mysqli_stmt_error($stmt) . "');</script>";
                    }
                    mysqli_stmt_close($stmt);
                } else {
                    echo "<script>alert('Error al preparar la declaración: " . mysqli_error($con) . "');</script>";
                }
            }
            mysqli_stmt_close($check_stmt);
        } else {
            echo "<script>alert('Por favor ingresa datos válidos.');</script>";
        }
    } elseif (isset($_POST['form_type']) && $_POST['form_type'] == 'login') {
        // Login
        $email_login = $_POST['email_login'];
        $password_login = $_POST['password_login'];

        if (!empty($email_login) && !empty($password_login)) {
            // Using prepared statements to prevent SQL injection
            $query = "SELECT * FROM users WHERE email = ?";
            if ($stmt = mysqli_prepare($con, $query)) {
                mysqli_stmt_bind_param($stmt, "s", $email_login);
                if (mysqli_stmt_execute($stmt)) {
                    $result = mysqli_stmt_get_result($stmt);
                    if ($result && mysqli_num_rows($result) > 0) {
                        $user_data = mysqli_fetch_assoc($result);
                        if (password_verify($password_login, $user_data['password'])) {
                            $_SESSION['user_id'] = $user_data['user_id'];
                            header("Location: index_cursos.php");
                            exit();
                        } else {
                            echo "<script>alert('Contraseña incorrecta.');</script>";
                        }
                    } else {
                        echo "<script>alert('Correo electrónico no registrado.');</script>";
                    }
                } else {
                    echo "<script>alert('Error al ejecutar la consulta: " . mysqli_stmt_error($stmt) . "');</script>";
                }
                mysqli_stmt_close($stmt);
            } else {
                echo "<script>alert('Error al preparar la declaración: " . mysqli_error($con) . "');</script>";
            }
        } else {
            echo "<script>alert('Por favor ingresa datos válidos.');</script>";
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@4.3.0/fonts/remixicon.css" rel="stylesheet" />
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <link rel="stylesheet" href="./assets/css/login.css">
    <title>Iniciar sesión || Registrarse</title>
</head>

<body>

    <div class="container fade-in" id="container">
        <div class="form-container sign-up">
            <form method="POST">
                <h1>Crear Cuenta</h1>
                <input type="hidden" name="form_type" value="register">
                <input id="text" type="text" name="user_name_register" placeholder="Nombre">
                <input id="text" type="email" name="email_register" placeholder="Correo Electronico">
                <input type="password" name="password_register" placeholder="Contraseña">
                <button id="button_register" type="submit">Registrarse</button>
            </form>
        </div>
        <div class="form-container sign-in">
            <form method="POST">
                <h1>Ingresar</h1>
                <input type="hidden" name="form_type" value="login">
                <input id="text" type="email" name="email_login" placeholder="Correo electrónico">
                <input id="text" type="password" name="password_login" placeholder="Contraseña">
                <a href="#">Olvidaste tu Contraseña?</a>
                <button id="button_login" type="submit">Ingresar</button>
            </form>
        </div>
        <div class="toggle-container">
            <div class="toggle">
                <div class="toggle-panel toggle-left">
                    <h1>Bienvenido de Vuelta!</h1>
                    <p>Ingresa a tu cuenta para entrar a la página 💻</p>
                    <button class="hidden" id="login">Ingresar</button>
                </div>
                <div class="toggle-panel toggle-right">
                    <h1>Hola, programador!</h1>
                    <p>Registrate con tus datos personales para acceder a los cursos 🦁👉</p>
                    <button class="hidden" id="register">Registrate</button>
                </div>
            </div>
        </div>
    </div>

    <script src="./assets/js/login.js"></script>
    <script src="./assets/js/main.js"></script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
</body>

</html>