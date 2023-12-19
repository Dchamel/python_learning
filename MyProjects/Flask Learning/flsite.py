from flask import Flask, render_template, request, flash, url_for

app = Flask(__name__)

menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]


@app.route("/")
def index():
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title="About", menu=menu)


@app.route("/profile/<int:username>")
def profile(username):
    return f"Пользователь: {username}"


@app.route("/contact", methods=["POST", "GET"])
def contact():
    app.config['SECRET_KEY'] = 'sdfghwfghwsfghwsrthwarth'
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено')
        else:
            flash('Ошибка отправки')
        print(request.form)
    return render_template('contact.html', title="Feedback", menu=menu)


# with app.test_request_context():
#     print(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
