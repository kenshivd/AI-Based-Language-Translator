from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    text = data["text"]
    target_lang = data["target"]
    
    translation = translator.translate(text, dest=target_lang)
    return jsonify({"translated_text": translation.text})

if __name__ == "__main__":
    app.run(debug=True)
