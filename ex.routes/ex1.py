from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur la page d\'accueil"


@app.route('/contact')
def contact():
    return "Page de contact"


@app.route('/about')
def about():
    return "Page à propos"


if __name__ == '__main__':
    app.run(debug=True)