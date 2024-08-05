from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    choice = request.form['choice']
    if choice == 'する':
        return redirect(url_for('game_lover'))
    else:
        return redirect(url_for('try_game'))

@app.route('/game_lover')
def game_lover():
    return render_template('game_lover.html')#'ゲーム大好き!'

@app.route('/try_game')
def try_game():
    return render_template('game_unlover.html')#'ゲームやってみたいな!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
