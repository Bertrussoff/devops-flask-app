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
    <title>DevOps Marketplace</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #f4f6f9;
            color: #1a1a2e;
        }

        /* Navbar */
        .navbar {
            background: #1a1a2e;
            padding: 14px 40px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .navbar .logo {
            font-size: 1.4em;
            font-weight: 700;
            color: #fff;
        }
        .navbar .logo span { color: #4ecca3; }
        .nav-links a {
            color: rgba(255,255,255,0.7);
            text-decoration: none;
            margin-left: 24px;
            font-size: 0.9em;
            transition: color 0.2s;
        }
        .nav-links a:hover { color: #4ecca3; }
        .nav-btn {
            background: #4ecca3;
            color: #1a1a2e !important;
            padding: 8px 18px;
            border-radius: 6px;
            font-weight: 600 !important;
        }

        /* Hero */
        .hero {
            background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
            padding: 60px 40px;
            text-align: center;
            color: white;
        }
        .hero h1 {
            font-size: 2.6em;
            font-weight: 700;
            margin-bottom: 12px;
        }
        .hero h1 span { color: #4ecca3; }
        .hero p {
            color: rgba(255,255,255,0.65);
            font-size: 1.05em;
            max-width: 560px;
            margin: 0 auto 28px;
        }
        .hero-btns { display: flex; gap: 14px; justify-content: center; }
        .btn-primary {
            background: #4ecca3;
            color: #1a1a2e;
            padding: 12px 28px;
            border-radius: 8px;
            font-weight: 700;
            text-decoration: none;
            font-size: 0.95em;
        }
        .btn-outline {
            border: 1px solid rgba(255,255,255,0.3);
            color: white;
            padding: 12px 28px;
            border-radius: 8px;
            font-weight: 600;
            text-decoration: none;
            font-size: 0.95em;
        }

        /* Stats bar */
        .stats-bar {
            background: white;
            display: flex;
            justify-content: center;
            gap: 60px;
            padding: 20px;
            border-bottom: 1px solid #eee;
        }
        .stat { text-align: center; }
        .stat .num { font-size: 1.5em; font-weight: 700; color: #0f3460; }
        .stat .label { font-size: 0.8em; color: #888; }

        /* Categories */
        .section { padding: 40px; max-width: 1100px; margin: 0 auto; }
        .section-title {
            font-size: 1.3em;
            font-weight: 700;
            margin-bottom: 20px;
            color: #1a1a2e;
        }
        .categories {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 36px;
        }
        .cat-pill {
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 50px;
            padding: 8px 18px;
            font-size: 0.85em;
            cursor: pointer;
            transition: all 0.2s;
            color: #444;
        }
        .cat-pill:hover, .cat-pill.active {
            background: #0f3460;
            color: white;
            border-color: #0f3460;
        }

        /* Product cards */
        .products {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
            gap: 20px;
        }
        .card {
            background: white;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #eee;
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: pointer;
        }
        .card:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        }
        .card-img {
            height: 130px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3em;
        }
        .card-body { padding: 16px; }
        .card-tag {
            font-size: 0.72em;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #4ecca3;
            margin-bottom: 6px;
        }
        .card-title {
            font-size: 1em;
            font-weight: 700;
            margin-bottom: 6px;
            color: #1a1a2e;
        }
        .card-desc {
            font-size: 0.82em;
            color: #888;
            margin-bottom: 14px;
            line-height: 1.5;
        }
        .card-footer {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .price { font-weight: 700; color: #0f3460; font-size: 1em; }
        .rating { font-size: 0.8em; color: #f5a623; }
        .add-btn {
            background: #0f3460;
            color: white;
            border: none;
            padding: 7px 14px;
            border-radius: 6px;
            font-size: 0.8em;
            cursor: pointer;
            font-weight: 600;
            transition: background 0.2s;
        }
        .add-btn:hover { background: #4ecca3; color: #1a1a2e; }

        /* Deploy badge */
        .deploy-badge {
            background: #1a1a2e;
            color: #4ecca3;
            text-align: center;
            padding: 10px;
            font-size: 0.8em;
            letter-spacing: 1px;
        }

        /* Footer */
        footer {
            background: #1a1a2e;
            color: rgba(255,255,255,0.4);
            text-align: center;
            padding: 24px;
            font-size: 0.82em;
            margin-top: 40px;
        }
    </style>
</head>
<body>

    <nav class="navbar">
        <div class="logo">Dev<span>Market</span></div>
        <div class="nav-links">
            <a href="#">Browse</a>
            <a href="#">Tools</a>
            <a href="#">Docs</a>
            <a href="#" class="nav-btn">Sign Up</a>
        </div>
    </nav>

    <div class="hero">
        <h1>The <span>DevOps</span> Marketplace</h1>
        <p>Discover, deploy, and manage tools for your CI/CD pipeline — all in one place.</p>
        <div class="hero-btns">
            <a href="#" class="btn-primary">Browse Tools</a>
            <a href="#" class="btn-outline">View Pipeline</a>
        </div>
    </div>

    <div class="stats-bar">
        <div class="stat"><div class="num">3</div><div class="label">VMs Running</div></div>
        <div class="stat"><div class="num">5</div><div class="label">Pipeline Stages</div></div>
        <div class="stat"><div class="num">100%</div><div class="label">Uptime</div></div>
        <div class="stat"><div class="num">v3.0</div><div class="label">Current Build</div></div>
    </div>

    <div class="section">
        <div class="section-title">Browse Categories</div>
        <div class="categories">
            <div class="cat-pill active">All</div>
            <div class="cat-pill">CI/CD</div>
            <div class="cat-pill">Containers</div>
            <div class="cat-pill">Security</div>
            <div class="cat-pill">Monitoring</div>
            <div class="cat-pill">Orchestration</div>
        </div>

        <div class="section-title">Featured Tools</div>
        <div class="products">
            <div class="card">
                <div class="card-img" style="background:#eef7ff;">⚙️</div>
                <div class="card-body">
                    <div class="card-tag">CI/CD</div>
                    <div class="card-title">Jenkins Pipeline</div>
                    <div class="card-desc">Automate your build, test and deploy workflow with ease.</div>
                    <div class="card-footer">
                        <div>
                            <div class="price">Free</div>
                            <div class="rating">★★★★★ 4.9</div>
                        </div>
                        <button class="add-btn">Install</button>
                    </div>
                </div>
            </div>
            <div class="card">
                <div class="card-img" style="background:#e8f8f4;">🐳</div>
                <div class="card-body">
                    <div class="card-tag">Containers</div>
                    <div class="card-title">Docker Engine</div>
                    <div class="card-desc">Build and run containers for consistent environments.</div>
                    <div class="card-footer">
                        <div>
                            <div class="price">Free</div>
                            <div class="rating">★★★★★ 4.8</div>
                        </div>
                        <button class="add-btn">Install</button>
                    </div>
                </div>
            </div>
            <div class="card">
                <div class="card-img" style="background:#fff4e8;">🔒</div>
                <div class="card-body">
                    <div class="card-tag">Security</div>
                    <div class="card-title">Trivy Scanner</div>
                    <div class="card-desc">Scan Docker images for vulnerabilities automatically.</div>
                    <div class="card-footer">
                        <div>
                            <div class="price">Free</div>
                            <div class="rating">★★★★☆ 4.7</div>
                        </div>
                        <button class="add-btn">Install</button>
                    </div>
                </div>
            </div>
            <div class="card">
                <div class="card-img" style="background:#f0eeff;">☸️</div>
                <div class="card-body">
                    <div class="card-tag">Orchestration</div>
                    <div class="card-title">Kubernetes K3s</div>
                    <div class="card-desc">Lightweight K8s for local and edge deployments.</div>
                    <div class="card-footer">
                        <div>
                            <div class="price">Free</div>
                            <div class="rating">★★★★★ 4.9</div>
                        </div>
                        <button class="add-btn">Coming soon</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="deploy-badge">
        🚀 Deployed via Jenkins Pipeline &nbsp;|&nbsp; 3 VMs Active &nbsp;|&nbsp; Built by Bertram
    </div>

    <footer>
        © 2026 DevMarket · Powered by Flask + Docker + Jenkins · Running on Ubuntu 24.04
    </footer>

</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
