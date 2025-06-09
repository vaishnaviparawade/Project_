from flask import Flask, request
import logging
from prometheus_flask_exporter import PrometheusMetrics
from jaeger_client import Config
from flask import jsonify

app = Flask(__name__)
metrics = PrometheusMetrics(app)
logging.basicConfig(level=logging.INFO)

# Initialize Jaeger tracer
def init_jaeger_tracer(service_name='python-app'):
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'logging': True,
        },
        service_name=service_name,
    )
    return config.initialize_tracer()

tracer = init_jaeger_tracer()

@app.route('/')
def home():
    with tracer.start_span('home') as span:
        app.logger.info("Home page accessed")
        return "Hello from Observability Demo App!"

@app.route('/api/data')
def data():
    with tracer.start_span('data') as span:
        app.logger.info("Data endpoint hit")
        return jsonify({'data': 'This is some sample data'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)