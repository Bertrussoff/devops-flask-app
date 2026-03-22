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
    <title>FlipDevOps</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: #f1f3f6; color: #212121; }

        /* Navbar */
        .navbar {
            background: #2874f0;
            padding: 0 40px;
            display: flex;
            align-items: center;
            gap: 20px;
            height: 56px;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
        .logo { color: white; font-size: 1.3em; font-weight: 800; letter-spacing: -0.5px; }
        .logo span { color: #ffe500; font-style: italic; font-size: 0.55em; display: block; margin-top: -6px; font-weight: 400; }
        .search-bar {
            flex: 1;
            display: flex;
            background: white;
            border-radius: 4px;
            overflow: hidden;
            max-width: 580px;
        }
        .search-bar input {
            flex: 1;
            border: none;
            outline: none;
            padding: 10px 16px;
            font-size: 0.9em;
        }
        .search-bar button {
            background: #2874f0;
            border: none;
            padding: 0 20px;
            color: white;
            font-weight: 600;
            cursor: pointer;
            font-size: 0.9em;
        }
        .nav-links { display: flex; gap: 24px; margin-left: auto; }
        .nav-links a {
            color: white;
            text-decoration: none;
            font-size: 0.88em;
            font-weight: 500;
            white-space: nowrap;
        }
        .nav-btn {
            background: white;
            color: #2874f0 !important;
            padding: 6px 20px;
            border-radius: 3px;
            font-weight: 700 !important;
        }
        .cart-btn { display: flex; align-items: center; gap: 6px; }

        /* Banner */
        .banner {
            background: linear-gradient(120deg, #2874f0, #0057c2);
            color: white;
            padding: 24px 40px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .banner h2 { font-size: 1.8em; font-weight: 800; }
        .banner p { color: rgba(255,255,255,0.8); font-size: 0.9em; margin-top: 6px; }
        .banner-badge {
            background: #ffe500;
            color: #212121;
            padding: 8px 20px;
            border-radius: 4px;
            font-weight: 800;
            font-size: 0.9em;
        }

        /* Category strip */
        .cat-strip {
            background: white;
            display: flex;
            gap: 0;
            overflow-x: auto;
            border-bottom: 1px solid #eee;
            padding: 0 20px;
        }
        .cat-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 14px 20px;
            cursor: pointer;
            font-size: 0.78em;
            font-weight: 600;
            color: #212121;
            white-space: nowrap;
            border-bottom: 3px solid transparent;
            transition: all 0.2s;
        }
        .cat-item:hover, .cat-item.active { color: #2874f0; border-bottom-color: #2874f0; }
        .cat-icon { font-size: 2em; margin-bottom: 4px; }

        /* Main layout */
        .main { max-width: 1200px; margin: 16px auto; padding: 0 16px; }

        /* Deal of the day */
        .section-header {
            background: white;
            padding: 14px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid #f0f0f0;
            border-radius: 4px 4px 0 0;
        }
        .section-title { font-size: 1.1em; font-weight: 700; color: #212121; }
        .deal-timer { color: #ff6161; font-weight: 700; font-size: 0.85em; }
        .view-all {
            color: #2874f0;
            font-size: 0.85em;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
        }

        /* Product grid */
        .products-wrap { background: white; border-radius: 0 0 4px 4px; margin-bottom: 16px; }
        .products {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 1px;
            background: #f1f3f6;
        }
        .card {
            background: white;
            padding: 20px 16px;
            cursor: pointer;
            transition: box-shadow 0.2s;
            text-align: center;
        }
        .card:hover { box-shadow: 0 4px 20px rgba(0,0,0,0.12); z-index: 1; position: relative; }
        .card-img {
            font-size: 3.5em;
            margin-bottom: 12px;
            height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card-title { font-size: 0.88em; color: #212121; margin-bottom: 4px; font-weight: 500; }
        .card-desc { font-size: 0.78em; color: #878787; margin-bottom: 10px; line-height: 1.4; }
        .card-price { font-size: 1.1em; font-weight: 700; color: #212121; }
        .card-original { font-size: 0.78em; color: #878787; text-decoration: line-through; margin-left: 6px; }
        .card-discount { font-size: 0.78em; color: #388e3c; font-weight: 600; margin-left: 6px; }
        .card-rating {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            background: #388e3c;
            color: white;
            padding: 2px 8px;
            border-radius: 3px;
            font-size: 0.75em;
            font-weight: 600;
            margin-bottom: 8px;
        }
        .assured {
            color: #2874f0;
            font-size: 0.72em;
            font-weight: 700;
            border: 1px solid #2874f0;
            padding: 1px 5px;
            border-radius: 2px;
            display: inline-block;
            margin-bottom: 8px;
        }
        .add-btn {
            background: #ff9f00;
            color: white;
            border: none;
            padding: 8px 18px;
            border-radius: 3px;
            font-size: 0.82em;
            font-weight: 700;
            cursor: pointer;
            margin-top: 8px;
            transition: background 0.2s;
            width: 100%;
        }
        .add-btn:hover { background: #e8900a; }
        .buy-btn {
            background: #fb641b;
            color: white;
            border: none;
            padding: 8px 18px;
            border-radius: 3px;
            font-size: 0.82em;
            font-weight: 700;
            cursor: pointer;
            margin-top: 6px;
            width: 100%;
            transition: background 0.2s;
        }
        .buy-btn:hover { background: #e05615; }

        /* Banner strip */
        .banner-strip {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-bottom: 16px;
        }
        .mini-banner {
            background: white;
            border-radius: 4px;
            padding: 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
        }
        .mini-banner h3 { font-size: 1em; font-weight: 700; color: #212121; }
        .mini-banner p { font-size: 0.8em; color: #878787; margin-top: 4px; }
        .mini-banner .icon { font-size: 3em; }

        /* Footer */
        footer {
            background: #172337;
            color: rgba(255,255,255,0.6);
            padding: 32px 40px;
            margin-top: 20px;
        }
        .footer-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto 20px;
        }
        .footer-col h4 { color: #878787; font-size: 0.78em; font-weight: 700; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px; }
        .footer-col a { display: block; color: rgba(255,255,255,0.6); font-size: 0.82em; margin-bottom: 8px; text-decoration: none; }
        .footer-col a:hover { color: white; }
        .footer-bottom { text-align: center; font-size: 0.78em; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; max-width: 1200px; margin: 0 auto; }
    </style>
</head>
<body>

    <nav class="navbar">
        <div class="logo">FlipDevOps <span>Explore Plus</span></div>
        <div class="search-bar">
            <input type="text" placeholder="Search for DevOps tools, pipelines and more...">
            <button>🔍 Search</button>
        </div>
        <div class="nav-links">
            <a href="#" class="nav-btn">Login</a>
            <a href="#">Become a Seller</a>
            <a href="#">More ▾</a>
            <a href="#" class="cart-btn">🛒 Cart</a>
        </div>
    </nav>

    <div class="banner">
        <div>
            <h2>⚡ Big Billion DevOps Sale</h2>
            <p>Automate everything · Deploy anywhere · Scale infinitely</p>
        </div>
        <div class="banner-badge">🚀 Pipeline Live!</div>
    </div>

    <div class="cat-strip">
        <div class="cat-item active"><div class="cat-icon">⚙️</div>CI/CD</div>
        <div class="cat-item"><div class="cat-icon">🐳</div>Containers</div>
        <div class="cat-item"><div class="cat-icon">☸️</div>Kubernetes</div>
        <div class="cat-item"><div class="cat-icon">🔒</div>Security</div>
        <div class="cat-item"><div class="cat-icon">📊</div>Monitoring</div>
        <div class="cat-item"><div class="cat-icon">🌐</div>Networking</div>
        <div class="cat-item"><div class="cat-icon">💾</div>Storage</div>
        <div class="cat-item"><div class="cat-icon">🤖</div>Automation</div>
    </div>

    <div class="main">

        <div class="banner-strip">
            <div class="mini-banner">
                <div>
                    <h3>Jenkins Pipeline</h3>
                    <p>Auto deploy on every push</p>
                    <p style="color:#388e3c;font-weight:700;font-size:0.85em;margin-top:8px;">✅ Currently Active</p>
                </div>
                <div class="icon">⚙️</div>
            </div>
            <div class="mini-banner">
                <div>
                    <h3>3 VMs Running</h3>
                    <p>master · node1 · node2</p>
                    <p style="color:#388e3c;font-weight:700;font-size:0.85em;margin-top:8px;">✅ All Systems Go</p>
                </div>
                <div class="icon">🖥️</div>
            </div>
        </div>

        <div class="products-wrap">
            <div class="section-header">
                <span class="section-title">🔥 Deal of the Day — DevOps Tools</span>
                <span class="deal-timer">⏱ Ends in 08:24:59</span>
                <a href="#" class="view-all">VIEW ALL →</a>
            </div>
            <div class="products">
                <div class="card">
                    <div class="card-img">⚙️</div>
                    <div class="assured">F-Assured</div>
                    <div class="card-title">Jenkins CI/CD Server</div>
                    <div class="card-desc">Automate build, test and deploy pipeline</div>
                    <div class="card-rating">★ 4.9</div>
                    <div>
                        <span class="card-price">FREE</span>
                        <span class="card-original">₹9,999</span>
                        <span class="card-discount">100% off</span>
                    </div>
                    <button class="add-btn">🛒 Add to Pipeline</button>
                    <button class="buy-btn">⚡ Deploy Now</button>
                </div>
                <div class="card">
                    <div class="card-img">🐳</div>
                    <div class="assured">F-Assured</div>
                    <div class="card-title">Docker Engine</div>
                    <div class="card-desc">Container runtime for consistent deployments</div>
                    <div class="card-rating">★ 4.8</div>
                    <div>
                        <span class="card-price">FREE</span>
                        <span class="card-original">₹7,999</span>
                        <span class="card-discount">100% off</span>
                    </div>
                    <button class="add-btn">🛒 Add to Pipeline</button>
                    <button class="buy-btn">⚡ Deploy Now</button>
                </div>
                <div class="card">
                    <div class="card-img">🔒</div>
                    <div class="assured">F-Assured</div>
                    <div class="card-title">Trivy Security Scanner</div>
                    <div class="card-desc">Scan images for HIGH & CRITICAL vulnerabilities</div>
                    <div class="card-rating">★ 4.7</div>
                    <div>
                        <span class="card-price">FREE</span>
                        <span class="card-original">₹4,999</span>
                        <span class="card-discount">100% off</span>
                    </div>
                    <button class="add-btn">🛒 Add to Pipeline</button>
                    <button class="buy-btn">⚡ Deploy Now</button>
                </div>
                <div class="card">
                    <div class="card-img">☸️</div>
                    <div class="assured">F-Assured</div>
                    <div class="card-title">Kubernetes K3s</div>
                    <div class="card-desc">Lightweight K8s for local cluster setup</div>
                    <div class="card-rating">★ 4.9</div>
                    <div>
                        <span class="card-price">FREE</span>
                        <span class="card-original">₹14,999</span>
                        <span class="card-discount">100% off</span>
                    </div>
                    <button class="add-btn">🛒 Coming Soon</button>
                    <button class="buy-btn">⚡ Coming Soon</button>
                </div>
                <div class="card">
                    <div class="card-img">📊</div>
                    <div class="assured">F-Assured</div>
                    <div class="card-title">Prometheus + Grafana</div>
                    <div class="card-desc">Monitor your infrastructure in real time</div>
                    <div class="card-rating">★ 4.8</div>
                    <div>
                        <span class="card-price">FREE</span>
                        <span class="card-original">₹6,999</span>
                        <span class="card-discount">100% off</span>
                    </div>
                    <button class="add-btn">🛒 Coming Soon</button>
                    <button class="buy-btn">⚡ Coming Soon</button>
                </div>
                <div class="card">
                    <div class="card-img">🐙</div>
                    <div class="assured">F-Assured</div>
                    <div class="card-title">GitHub Webhooks</div>
                    <div class="card-desc">Auto-trigger pipelines on every git push</div>
                    <div class="card-rating">★ 5.0</div>
                    <div>
                        <span class="card-price">FREE</span>
                        <span class="card-original">₹2,999</span>
                        <span class="card-discount">100% off</span>
                    </div>
                    <button class="add-btn">🛒 Add to Pipeline</button>
                    <button class="buy-btn">⚡ Deploy Now</button>
                </div>
            </div>
        </div>

    </div>

    <footer>
        <div class="footer-grid">
            <div class="footer-col">
                <h4>About</h4>
                <a href="#">About FlipDevOps</a>
                <a href="#">Careers</a>
                <a href="#">Blog</a>
                <a href="#">Press</a>
            </div>
            <div class="footer-col">
                <h4>Help</h4>
                <a href="#">Payments</a>
                <a href="#">Shipping</a>
                <a href="#">FAQ</a>
                <a href="#">Report a Bug</a>
            </div>
            <div class="footer-col">
                <h4>Policy</h4>
                <a href="#">Return Policy</a>
                <a href="#">Terms of Use</a>
                <a href="#">Security</a>
                <a href="#">Privacy</a>
            </div>
            <div class="footer-col">
                <h4>DevOps Lab</h4>
                <a href="#">vm-master :5000</a>
                <a href="#">vm-node1 :5000</a>
                <a href="#">vm-node2 :5000</a>
                <a href="#">Jenkins :8080</a>
            </div>
        </div>
        <div class="footer-bottom">
            © 2026 FlipDevOps · Deployed via Jenkins Pipeline · Running on Ubuntu 24.04 · Built with ❤️ by Bertram
        </div>
    </footer>

</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
