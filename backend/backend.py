from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from healthcheck import HealthCheck

app = Flask(__name__)
metrics = PrometheusMetrics(app)
health = HealthCheck()

@app.route('/')
def index():
	return "Hello, World!", 200

app.add_url_rule('/healthcheck', 'healthcheck', view_func=lambda: health.run())
app.run(debug=False,host='0.0.0.0')


