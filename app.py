from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

# Load models and tokenizers
models = {
    "Hindi": {
        "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hi"),
        "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-hi"),
    },
    "French": {
        "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fr"),
        "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-fr"),
    },
}

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    target_language = data.get("target_language", "Hindi")
    if target_language not in models:
        return jsonify({"error": "Unsupported language"}), 400

    tokenizer = models[target_language]["tokenizer"]
    model = models[target_language]["model"]
    inputs = tokenizer.encode(text, return_tensors="pt", truncation=True)
    outputs = model.generate(inputs, max_length=50)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"translated_text": translated_text})

if __name__ == '__main__':
    app.run(debug=True)
