from flask import Flask
import socket
import platform
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    os_info = platform.system() + " " + platform.release()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bertram's DevOps App</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                color: white;
                padding: 20px;
            }}
            .header {{
                text-align: center;
                margin-bottom: 40px;
                animation: fadeIn 1s ease;
            }}
            .header h1 {{
                font-size: 3em;
                background: linear-gradient(90deg, #f72585, #7209b7, #3a0ca3, #4cc9f0);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 10px;
            }}
            .header p {{
                color: #aaa;
                font-size: 1.1em;
            }}
            .cards {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 20px;
                width: 100%;
                max-width: 1100px;
                animation: slideUp 1s ease;
            }}
            .card {{
                background: rgba(255,255,255,0.05);
                border-radius: 16px;
                padding: 24px;
                border: 1px solid rgba(255,255,255,0.1);
                backdrop-filter: blur(10px);
                transition: transform 0.3s ease;
            }}
            .card:hover {{ transform: translateY(-5px); }}
            .card h2 {{
                font-size: 1.2em;
                margin-bottom: 16px;
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            .card .emoji {{ font-size: 1.5em; }}
            .info-row {{
                display: flex;
                justify-content: space-between;
                padding: 8px 0;
                border-bottom: 1px solid rgba(255,255,255,0.05);
                font-size: 0.9em;
            }}
            .info-row:last-child {{ border-bottom: none; }}
            .label {{ color: #aaa; }}
            .value {{ color: #4cc9f0; font-weight: bold; }}
            .badge {{
                display: inline-block;
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 0.8em;
                font-weight: bold;
            }}
            .badge-green {{ background: #06d6a0; color: #000; }}
            .badge-blue {{ background: #4cc9f0; color: #000; }}
            .badge-purple {{ background: #7209b7; color: #fff; }}
            .pipeline-step {{
                display: flex;
                align-items: center;
                gap: 10px;
                padding: 8px 0;
                border-bottom: 1px solid rgba(255,255,255,0.05);
            }}
            .pipeline-step:last-child {{ border-bottom: none; }}
            .step-dot {{
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background: #06d6a0;
                flex-shrink: 0;
            }}
            .footer {{
                margin-top: 40px;
                text-align: center;
                color: #aaa;
                font-size: 0.9em;
                animation: fadeIn 2s ease;
            }}
            .footer span {{
                background: linear-gradient(90deg, #f72585, #4cc9f0);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: bold;
                font-size: 1.1em;
            }}
            @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
            @keyframes slideUp {{ from {{ opacity: 0; transform: translateY(30px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🚀 Bertram's DevOps Lab</h1>
            <p>Running on Kubernetes · Deployed via Jenkins CI/CD</p>
        </div>

        <div class="cards">
            <!-- System Info -->
            <div class="card">
                <h2><span class="emoji">🖥️</span> System Info</h2>
                <div class="info-row">
                    <span class="label">Hostname</span>
                    <span class="value">{hostname}</span>
                </div>
                <div class="info-row">
                    <span class="label">IP Address</span>
                    <span class="value">{ip}</span>
                </div>
                <div class="info-row">
                    <span class="label">OS</span>
                    <span class="value">{os_info}</span>
                </div>
                <div class="info-row">
                    <span class="label">Timestamp</span>
                    <span class="value">{now}</span>
                </div>
            </div>

            <!-- Cluster Info -->
            <div class="card">
                <h2><span class="emoji">☸️</span> Cluster Info</h2>
                <div class="info-row">
                    <span class="label">Orchestrator</span>
                    <span class="value">k3s Kubernetes</span>
                </div>
                <div class="info-row">
                    <span class="label">Nodes</span>
                    <span class="value">3 (master + 2 workers)</span>
                </div>
                <div class="info-row">
                    <span class="label">Replicas</span>
                    <span class="value">3 Pods Running</span>
                </div>
                <div class="info-row">
                    <span class="label">Service Port</span>
                    <span class="value">NodePort :30000</span>
                </div>
                <div class="info-row">
                    <span class="label">Status</span>
                    <span class="badge badge-green">✅ Healthy</span>
                </div>
            </div>

            <!-- Pipeline Status -->
            <div class="card">
                <h2><span class="emoji">⚙️</span> CI/CD Pipeline</h2>
                <div class="pipeline-step">
                    <div class="step-dot"></div>
                    <span>Clone Code from GitHub</span>
                    <span class="badge badge-green" style="margin-left:auto">Done</span>
                </div>
                <div class="pipeline-step">
                    <div class="step-dot"></div>
                    <span>Build Docker Image</span>
                    <span class="badge badge-green" style="margin-left:auto">Done</span>
                </div>
                <div class="pipeline-step">
                    <div class="step-dot"></div>
                    <span>Trivy Security Scan</span>
                    <span class="badge badge-green" style="margin-left:auto">Done</span>
                </div>
                <div class="pipeline-step">
                    <div class="step-dot"></div>
                    <span>Import to k3s Nodes</span>
                    <span class="badge badge-green" style="margin-left:auto">Done</span>
                </div>
                <div class="pipeline-step">
                    <div class="step-dot"></div>
                    <span>Deploy to Kubernetes</span>
                    <span class="badge badge-green" style="margin-left:auto">Done</span>
                </div>
            </div>

            <!-- Greeting -->
            <div class="card">
                <h2><span class="emoji">👋</span> Welcome</h2>
                <div class="info-row">
                    <span class="label">Project</span>
                    <span class="value">DevOps Flask App</span>
                </div>
                <div class="info-row">
                    <span class="label">Stack</span>
                    <span class="value">Flask + Docker + k3s</span>
                </div>
                <div class="info-row">
                    <span class="label">CI/CD</span>
                    <span class="value">Jenkins + GitHub</span>
                </div>
                <div class="info-row">
                    <span class="label">Monitoring</span>
                    <span class="badge badge-purple">Coming Soon</span>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>✨ Built with ❤️ by <span>Bertram</span> · {now}</p>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
