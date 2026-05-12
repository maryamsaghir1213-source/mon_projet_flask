from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur la page d'accueil"


@app.route('/profil/<int:id>/<nom>')
def user_profile(id, nom):
    return f"Profil de l'utilisateur avec ID: {id}, et nom: {nom}"

if __name__ == '__main__':
    app.run(debug=True)