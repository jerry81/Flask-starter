from flask import Flask
from flask import render_template

app  = Flask("Try Flask")

@app.route('/')
def home():
  return 'Hello, Flask!'


@app.route('/about')
def about():
   return 'About Page'

@app.route('/user/<name>')
def user(name):
   return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
