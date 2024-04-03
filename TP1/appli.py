from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return "coucou"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
