from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud Pizza Factory</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #ff7e5f, #feb47b);
                color: white;
                text-align: center;
            }

            .container {
                padding: 80px 20px;
            }

            h1 {
                font-size: 55px;
                margin-bottom: 10px;
            }

            h2 {
                font-size: 30px;
                margin-bottom: 30px;
            }

            .card {
                background: white;
                color: #333;
                width: 400px;
                margin: auto;
                padding: 25px;
                border-radius: 20px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            }

            .price {
                color: #ff5722;
                font-size: 28px;
                font-weight: bold;
            }

            button {
                background: #ff5722;
                color: white;
                border: none;
                padding: 12px 25px;
                border-radius: 8px;
                font-size: 18px;
                cursor: pointer;
                margin-top: 15px;
            }

            button:hover {
                background: #e64a19;
            }

            .footer {
                margin-top: 50px;
                font-size: 16px;
            }
        </style>
    </head>
    <body>

        <div class="container">

            <h1>🍕 Cloud Pizza Factory</h1>
            <h2>Freshly Baked in the Cloud ☁️</h2>

            <div class="card">
                <h3>🔥 Today's Special</h3>
                <h2>Paneer Tikka Pizza</h2>

                <p>
                    Loaded with fresh paneer, onions,
                    capsicum, mozzarella cheese and
                    our secret spicy sauce.
                </p>

                <p class="price">₹299 Only</p>

                <button>Order Now 🚀</button>
            </div>

            <div class="footer">
                Running inside Docker 🐳 | Managed by Kubernetes ☸️
            </div>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)