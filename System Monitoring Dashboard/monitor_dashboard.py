from flask import Flask, render_template
import psutil
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def generate_system_metrics():
    """
    Collect system metrics using psutil.
    """
    metrics = {
        'cpu': psutil.cpu_percent(interval=1),
        'memory': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent
    }
    return metrics

def create_chart(metrics):
    """
    Generate a bar chart for system metrics.
    """
    # Data for plotting
    labels = ['CPU Usage', 'Memory Usage', 'Disk Usage']
    values = [metrics['cpu'], metrics['memory'], metrics['disk']]
    colors = ['#FF5733', '#33FF57', '#3357FF']

    # Plot the bar chart
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=colors)
    plt.ylim(0, 100)
    plt.ylabel('Usage (%)')
    plt.title('System Health Metrics')

    # Save the chart to a bytes buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    return chart_data

@app.route('/')
def dashboard():
    """
    Render the system monitoring dashboard.
    """
    metrics = generate_system_metrics()
    chart_data = create_chart(metrics)
    return render_template('dashboard.html', metrics=metrics, chart_data=chart_data)

if __name__ == '__main__':
    app.run(debug=True)
