# Import the necessary libraries
import psutil  # A library for system monitoring (CPU and memory usage)
from flask import Flask, render_template  # Import Flask for web application and render_template for rendering HTML templates

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Get CPU and memory usage metrics using psutil
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    Message = None

    # Check if CPU or memory usage is greater than 80%
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"

    # Render an HTML template (index.html) and pass the CPU and memory metrics as well as the message
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message)

# Start the Flask application if this script is run directly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
