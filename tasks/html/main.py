from flask import Flask, request, redirect, url_for, render_template, session

import secrets
import string

def random_str(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

app = Flask(__name__)
app.secret_key = random_str(30)

# DON'T DO LIKE THIS ON PROD!
# USE DATABASES PLZ!
users = {
    "administrator": {
        "password": "My_secret_password",
        "secret": "flag{th1$_1$_Y0uRR_F1r$t_W3b_FL4G!}"
    }
}


@app.route("/")
def index():
    if "user" in session:
        return redirect(url_for("profile"))
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        secret = request.form["secret"]

        if username in users:
            return "Пользователь уже существует!"

        users[username] = {"password": password, "secret": secret}
        return redirect(url_for("login"))

    return render_template("register.html", title="Регистрация")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            session["user"] = username
            return redirect(url_for("profile"))

        return "Неверный логин или пароль!"

    return render_template("login.html", title="Логин")


@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect(url_for("login"))

    username = session["user"]
    user = users[username]

    return render_template(
        "profile.html",
        title="Профиль",
        username=username,
        secret=user["secret"]
    )


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
