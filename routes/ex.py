from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Page d\'accueil'


#route dynamique pour afficher un profile utilisateur
@app.route('/user/admin')
def user_profile():
    return f"Profile de 'Admin'"


#route pour gerer les connexions avec GET et POST
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "connexion reussie"
    else: 
        return "Formulaire de connexion "



# Route pour les erreurs 404
@app.errorhandler(404)
def not_found(error):
    return "Cette page n'existe pas", 404



if __name__ == '__main__':
    app.run(debug=True)