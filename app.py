from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
    choice = request.form['choice']
    return redirect(url_for(choice))


@app.route('/user')
def user():
    # 'ゲーム大好き!'
    return render_template('branch.html', question='質問1', answer1='答え1', trans1='branch2', answer2='答え2', trans2='notuser')


@app.route('/branch2')
def branch2():
    # 'ゲーム大好き!'
    return render_template('branch.html', question='質問2', answer1='答え3', answer2='答え4')


@app.route('/notuser')
def notuser():
    return render_template('notuser.html')  # 'ゲームやってみたいな!'


if __name__ == '__main__':
    app.run()
