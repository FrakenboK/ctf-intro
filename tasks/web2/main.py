from flask import Flask, request, session, redirect, render_template
from werkzeug.security import generate_password_hash, check_password_hash

import secrets
import string

def random_str(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

app = Flask(__name__)
app.secret_key = random_str(30)

admin = {
            "id": 1,
            "username": "administrator",
            "password": generate_password_hash(random_str(30)),
            "secret": "flag{H1lL0_Fr0m_ID000R_VULN}"
        }

users = [admin]
username_to_id = {
    "admin": 1
}


@app.route("/")
def index():
    return render_template("index.html", users=users, session=session)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        secret   = request.form["secret"]

        if username in username_to_id:
            return "Username already exists"

        new_id = len(users) + 1

        user = {
            "id": new_id,
            "username": username,
            "password": generate_password_hash(password),
            "secret": secret
        }

        users.append(user)
        username_to_id[username] = new_id

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username not in username_to_id:
            return "Invalid username or password"

        uid = username_to_id[username]
        user = users[uid - 1]

        if not check_password_hash(user["password"], password):
            return "Invalid username or password"

        session["user_id"] = uid
        return redirect(f"/profile?id={uid}")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/profile")
def profile():
    uid = int(request.args.get("id", 0))

    if uid < 1 or uid > len(users):
        return "User not found"

    user = users[uid - 1]
    return render_template("profile.html", user=user, uid=uid)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
