from flask import Flask, render_template
import psutil
import time

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Collect system metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    network = psutil.net_io_counters()
    bytes_sent = network.bytes_sent
    bytes_received = network.bytes_recv
    process_count = len(psutil.pids())
    uptime_seconds = time.time() - psutil.boot_time()
    uptime = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

    # Pass data to the template
    return render_template('dashboard.html',
                           cpu=cpu_usage,
                           memory=memory_usage,
                           disk=disk_usage,
                           sent=bytes_sent,
                           received=bytes_received,
                           processes=process_count,
                           uptime=uptime)

if __name__ == '__main__':
    app.run(debug=True)
