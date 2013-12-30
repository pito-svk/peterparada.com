from flask import Flask, render_template
import os

# Create application
app = Flask(__name__, static_folder='static', static_url_path='',
            template_folder='static')

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)