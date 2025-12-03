from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola! Si ves esto, tu Docker en Render funciona perfectamente."

if __name__ == "__main__":
    # Render asigna un puerto dinámicamente en la variable PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
