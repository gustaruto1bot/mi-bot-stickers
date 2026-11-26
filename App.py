from flask import Flask, request
import os

app = Flask(__name__)
VERIFY_TOKEN = "gustavo123"

@app.route("/")
def home():
    return "BOT DE STICKERS ACTIVO!"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Token incorrecto", 403
    print(request.json)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
