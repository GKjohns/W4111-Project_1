from flask import Flask, request, render_template, flash,\
                  session, redirect, url_for
from forms import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'comsw4111'
app.debug = True

@app.route('/')
def login():
    return render_template('login.html', form=LoginForm())

if __name__ == '__main__':
    app.run()
