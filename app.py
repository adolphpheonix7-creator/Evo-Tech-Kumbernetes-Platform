from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def health():
    return jsonify(
        status="healthy",
        service="Evo-Tech Kubernetes Platform"
    )

@app.get("/health")
def health_check():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
