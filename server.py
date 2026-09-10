from flask import Flask, jsonify
import os

app = Flask(__name__)

comando = "desligar"

@app.route("/")
def inicio():
    return "SERVIDOR ESP32 ONLINE"

@app.route("/ligar")
def ligar():
    global comando
    comando = "ligar"
    return jsonify({"comando": comando})

@app.route("/desligar")
def desligar():
    global comando
    comando = "desligar"
    return jsonify({"comando": comando})

@app.route("/comando")
def obter_comando():
    return jsonify({"comando": comando})

if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=porta)
