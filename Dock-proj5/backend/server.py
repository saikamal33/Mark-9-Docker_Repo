from flask import Flask
import random

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    cpu = random.randint(10, 90)
    memory = random.randint(100, 900)
    return f"cpu_usage {cpu}\nmemory_usage {memory}", 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

