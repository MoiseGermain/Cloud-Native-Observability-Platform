from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Enable Prometheus metrics
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "DevOps CI/CD Pipeline Running"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
