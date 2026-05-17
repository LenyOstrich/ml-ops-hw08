from flask import Flask, Response
from prometheus_client import Histogram, generate_latest
import random
import time

app = Flask(__name__)

REQUEST_TIME = Histogram(
    "model_inference_latency_seconds", "Model inference latency"
)


@app.route("/predict")
@REQUEST_TIME.time()
def predict():
    time.sleep(random.uniform(0.05, 0.3))
    return {"prediction": random.random()}


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
