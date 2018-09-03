from flask import Flask,redirect, url_for
from flask.templating import render_template
app = Flask(__name__)


@app.route('/<name>')
def index(name):
   return render_template('welcome.html',name=name)

@app.route('/hello')
def hello_world():
 return 'Hello World hi'

@app.route('/hello/<name>')
def hello_name(name):
 return 'Hello %s!' % name
@app.route('/hello/<int:id>')
def hello_id(id):
 return 'Hello %s!' % id
@app.route('/python/')
def hello_python():
 return 'Hello Python'

@app.route('/admin',methods = ['POST', 'GET'])
def hello_admin():
 return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
 return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
 if name =='admin':
  return redirect(url_for('hello_admin'))
 else:
     return redirect(url_for('hello_guest',guest = name))
if __name__ == '__main__':
 app.run(debug=True)
 
   
   
# app.add_url_rule('/', 'hello', hello_world)
