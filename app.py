from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
    choice = request.form['choice']
    if choice == 'inUse':
        return redirect(url_for('user'))
    else:
        return redirect(url_for('notuser'))


@app.route('/user')
def user():
    # 'ゲーム大好き!'
    return render_template('branch.html', question='質問1', answer1='答え1', answer2='答え2')


@app.route('/notuser')
def notuser():
    return render_template('notuser.html')  # 'ゲームやってみたいな!'


if __name__ == '__main__':
    app.run()
