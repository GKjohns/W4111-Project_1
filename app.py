from flask import Flask, request, render_template, flash,\
                  session, redirect, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = 'comsw4111'
app.debug = True

@app.route('/')
def test_page():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()
