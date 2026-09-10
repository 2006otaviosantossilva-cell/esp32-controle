from flask import Flask, jsonify
import os

app = Flask(__name__)

comando = "desligar"


@app.route("/")
def inicio():
    estado = "LIGADO" if comando == "ligar" else "DESLIGADO"

    return f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Controle ESP32</title>

<style>
body {{
    margin: 0;
    min-height: 100vh;
    background: #080b12;
    color: white;
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
}}

.container {{
    width: 90%;
    max-width: 450px;
    padding: 35px;
    text-align: center;
    border: 1px solid #273244;
    border-radius: 25px;
    background: #10151f;
    box-shadow: 0 0 30px rgba(0,150,255,0.15);
}}

h1 {{
    margin-bottom: 30px;
    letter-spacing: 2px;
}}

.indicador {{
    width: 35px;
    height: 35px;
    border-radius: 50%;
    margin: 0 auto 15px;
    background: {"#00eaff" if comando == "ligar" else "#ff1744"};
    box-shadow: 0 0 25px {"#00eaff" if comando == "ligar" else "#ff1744"};
}}

.status {{
    font-size: 22px;
    margin-bottom: 30px;
    font-weight: bold;
}}

button {{
    width: 100%;
    padding: 18px;
    margin: 10px 0;
    border-radius: 15px;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    color: white;
    background: transparent;
}}

.ligar {{
    border: 2px solid #00eaff;
    box-shadow: 0 0 15px rgba(0,234,255,0.3);
}}

.desligar {{
    border: 2px solid #ff1744;
    box-shadow: 0 0 15px rgba(255,23,68,0.3);
}}

button:hover {{
    transform: scale(1.02);
}}
</style>
</head>

<body>

<div class="container">

<h1>CONTROLE ESP32</h1>

<div class="indicador"></div>

<div class="status">
{estado}
</div>

<a href="/ligar">
<button class="ligar">LIGAR LED</button>
</a>

<a href="/desligar">
<button class="desligar">DESLIGAR LED</button>
</a>

</div>

</body>
</html>
"""


@app.route("/ligar")
def ligar():
    global comando
    comando = "ligar"
    return """
    <script>
    window.location.href="/";
    </script>
    """


@app.route("/desligar")
def desligar():
    global comando
    comando = "desligar"
    return """
    <script>
    window.location.href="/";
    </script>
    """


@app.route("/comando")
def obter_comando():
    return jsonify({"comando": comando})


@app.route("/status")
def status():
    return "ON" if comando == "ligar" else "OFF"


if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=porta)
