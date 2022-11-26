# from flask import Flask
# app=Flask(__name__)
# @app.route('/')
# def Hello_world():
#     return 'Hello World'
# if __name__=='__main__':
#     app.run()
# #for debug mode
# app.debug=True
# app.run()
# app.run(debug=True)




import random
from flask import Flask, redirect,url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest'%guest

@app.route('/user/<name>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__=='__main__':
    #app.run(use_reloader=False, debug=True)
    port= 5000+ random.randint(0,999)
    url="http://127.0.0.1:{0}".format(port)
    app.run(use_reloader=False, debug=True, port=port)
    
