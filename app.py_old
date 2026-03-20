from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Lab</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        .container {
            text-align: center;
            padding: 40px;
            background: rgba(255,255,255,0.05);
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
            max-width: 700px;
            width: 90%;
        }
        .badge {
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            padding: 6px 18px;
            border-radius: 50px;
            font-size: 13px;
            letter-spacing: 2px;
            text-transform: uppercase;
            display: inline-block;
            margin-bottom: 20px;
        }
        h1 {
            font-size: 3em;
            font-weight: 700;
            margin-bottom: 10px;
            background: linear-gradient(90deg, #00c6ff, #0072ff, #a855f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            font-size: 1.1em;
            color: rgba(255,255,255,0.6);
            margin-bottom: 40px;
        }
        .cards {
            display: flex;
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 40px;
        }
        .card {
            background: rgba(255,255,255,0.07);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            padding: 20px;
            width: 150px;
            transition: transform 0.2s;
        }
        .card:hover { transform: translateY(-5px); }
        .card .icon { font-size: 2em; margin-bottom: 8px; }
        .card .label { font-size: 0.85em; color: rgba(255,255,255,0.5); }
        .card .value { font-size: 1em; font-weight: 600; }
        .status {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(0,255,100,0.1);
            border: 1px solid rgba(0,255,100,0.3);
            padding: 10px 24px;
            border-radius: 50px;
            font-size: 0.95em;
            color: #00ff64;
        }
        .dot {
            width: 8px; height: 8px;
            background: #00ff64;
            border-radius: 50%;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }
        .footer {
            margin-top: 30px;
            font-size: 0.8em;
            color: rgba(255,255,255,0.3);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="badge">🚀 DevOps Lab</div>
        <h1>Hello, Bertram!</h1>
        <p class="subtitle">Your CI/CD Pipeline is fully operational</p>
        <div class="cards">
            <div class="card">
                <div class="icon">🐳</div>
                <div class="value">Docker</div>
                <div class="label">Container</div>
            </div>
            <div class="card">
                <div class="icon">⚙️</div>
                <div class="value">Jenkins</div>
                <div class="label">CI/CD</div>
            </div>
            <div class="card">
                <div class="icon">🔒</div>
                <div class="value">Trivy</div>
                <div class="label">Security</div>
            </div>
            <div class="card">
                <div class="icon">🐙</div>
                <div class="value">GitHub</div>
                <div class="label">Source</div>
            </div>
        </div>
        <div class="status">
            <div class="dot"></div>
            All Systems Operational — Version 3.0.0
        </div>
        <div class="footer">Deployed via Jenkins Pipeline • Hosted on Ubuntu VM • Built with ❤️</div>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
