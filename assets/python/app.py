from flask import Flask
from flask_cors import CORS

# Importa los blueprints
from html_ejercicios import html_bp
from css_ejercicios import css_bp
from javascript_ejercicios import js_bp
from python_ejercicios import python_bp

app = Flask(__name__)
CORS(app)  # Aplica CORS a toda la aplicación

# Registra los blueprints
app.register_blueprint(html_bp, url_prefix='/html')
app.register_blueprint(css_bp, url_prefix='/css')
app.register_blueprint(js_bp, url_prefix='/js')
app.register_blueprint(python_bp, url_prefix='/python')

@app.route('/')
def home():
    return "Bienvenido a la plataforma de ejercicios de programación"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)