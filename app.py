from flask import Flask, jsonify, request

app = Flask(__name__)

APP_VERSION = "1.0.0"


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "student-ml-api",
        "version": APP_VERSION
    })


@app.post("/predict")
def predict():
    data = request.get_json(silent=True)

    if not data or "value" not in data:
        return jsonify({
            "error": "value is required"
        }), 400

    value = data["value"]

    if not isinstance(value, (int, float)):
        return jsonify({
            "error": "value must be numeric"
        }), 400

    prediction = value * 2

    return jsonify({
        "input": value,
        "prediction": prediction
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)