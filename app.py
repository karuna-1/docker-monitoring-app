from flask import Flask
import psutil
import socket
import time

app = Flask(__name__)

@app.route("/")
def home():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    hostname = socket.gethostname()

    uptime = round(time.time() / 3600, 2)

    return f"""
<style>
body {{
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
}}

.card {{
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
}}
</style>

<h1>🚀 Docker Monitoring Dashboard</h1>

<div class="card">
<b>Hostname:</b> {hostname}
</div>

<div class="card">
<b>CPU Usage:</b> {cpu}%
</div>

<div class="card">
<b>Memory Usage:</b> {memory}%
</div>

<div class="card">
<b>Disk Usage:</b> {disk}%
</div>

<div class="card">
<b>System Uptime:</b> {uptime} hours
</div>

<p>Built using Flask + Docker</p>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)