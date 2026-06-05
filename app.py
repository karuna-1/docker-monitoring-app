from flask import Flask
import psutil
import socket

app = Flask(__name__)

@app.route("/")
def home():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    hostname = socket.gethostname()

    return f"""
<h1>🚀 Docker Monitoring Dashboard</h1>

<hr>

<h3>System Information</h3>

<p><b>Hostname:</b> {hostname}</p>
<p><b>CPU Usage:</b> {cpu}%</p>
<p><b>Memory Usage:</b> {memory}%</p>
<p><b>Disk Usage:</b> {disk}%</p>

<hr>

<p>Built using Flask + Docker</p>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)