from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    choice = request.form['choice']
    if choice == '現在利用している':
        return redirect(url_for('user'))
    else:
        return redirect(url_for('notuser'))

@app.route('/user')
def user():
    return render_template('user.html')#'ゲーム大好き!'

@app.route('/notuser')
def notuser():
    return render_template('notuser.html')#'ゲームやってみたいな!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
