from flask import Flask, jsonify
import os

app = Flask(__name__)

comando = "desligar"


@app.route("/")
def inicio():
    estado = "LIGADO" if comando == "ligar" else "DESLIGADO"

    cor = "#00eaff" if comando == "ligar" else "#ff1744"

    return f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>ESP32 CONTROLE</title>

    <style>
        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            min-height: 100vh;
            background:
                radial-gradient(circle at top, #10243d 0%, #050a12 45%, #020408 100%);
            font-family: Arial, sans-serif;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}

        .painel {{
            width: 100%;
            max-width: 480px;
            background: rgba(8, 15, 25, 0.95);
            border: 1px solid #1d5575;
            border-radius: 25px;
            padding: 35px 25px;
            text-align: center;
            box-shadow:
                0 0 25px rgba(0, 200, 255, 0.15),
                inset 0 0 25px rgba(0, 150, 255, 0.05);
        }}

        h1 {{
            margin: 0 0 8px;
            font-size: 30px;
            letter-spacing: 3px;
            color: #00eaff;
            text-shadow: 0 0 12px rgba(0, 234, 255, 0.7);
        }}

        .subtitulo {{
            color: #7d9aaa;
            font-size: 14px;
            margin-bottom: 30px;
        }}

        .indicador {{
            width: 90px;
            height: 90px;
            margin: 0 auto 20px;
            border-radius: 50%;
            background: {cor};
            box-shadow:
                0 0 15px {cor},
                0 0 35px {cor},
                0 0 60px {cor};
        }}

        .estado {{
            font-size: 20px;
            font-weight: bold;
            letter-spacing: 2px;
            margin-bottom: 30px;
            color: {cor};
        }}

        .botao {{
            width: 100%;
            padding: 18px;
            margin: 10px 0;
            border-radius: 14px;
            font-size: 18px;
            font-weight: bold;
            letter-spacing: 1px;
            cursor: pointer;
            color: white;
            transition: 0.2s;
        }}

        .ligar {{
            background: #063d32;
            border: 2px solid #00ff9d;
            box-shadow: 0 0 12px rgba(0, 255, 157, 0.35);
        }}

        .ligar:hover {{
            background: #075947;
            box-shadow: 0 0 25px rgba(0, 255, 157, 0.7);
        }}

        .desligar {{
            background: #48131b;
            border: 2px solid #ff1744;
            box-shadow: 0 0 12px rgba(255, 23, 68, 0.35);
        }}

        .desligar:hover {{
            background: #681b27;
            box-shadow: 0 0 25px rgba(255, 23, 68, 0.7);
        }}

        .rodape {{
            margin-top: 25px;
            color: #536b79;
            font-size: 12px;
        }}
    </style>
</head>

<body>

<div class="painel">

    <h1>ESP32 CONTROLE</h1>

    <div class="subtitulo">
        SISTEMA DE CONTROLE REMOTO
    </div>

    <div class="indicador"></div>

    <div class="estado">
        STATUS: {estado}
    </div>

    <button class="botao ligar" onclick="location.href='/ligar'">
        LIGAR LED
    </button>

    <button class="botao desligar" onclick="location.href='/desligar'">
        DESLIGAR LED
    </button>

    <div class="rodape">
        SERVIDOR ONLINE • ESP32 CONECTADO
    </div>

</div>

</body>
</html>
"""


@app.route("/ligar")
def ligar():
    global comando
    comando = "ligar"
    return inicio()


@app.route("/desligar")
def desligar():
    global comando
    comando = "desligar"
    return inicio()


@app.route("/comando")
def obter_comando():
    return jsonify({"comando": comando})


@app.route("/status")
def status():
    if comando == "ligar":
        return "ON"
    else:
        return "OFF"


if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=porta)
