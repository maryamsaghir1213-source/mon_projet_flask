from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return f"Connexion réussie pour {username}"

    return render_template_string('''
        <form method="POST">
            Nom d'utilisateur:
            <input type="text" name="username">
            <input type="submit" value="Se connecter">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)