from flask import Flask
from flask import render_template
from flask import request

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

@app.route('/submit', methods=['GET', 'POST'])
def submit() :
   if request.method == 'POST':
      data = request.form['input_name']
      return f'You submitted: {data}'
   return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
