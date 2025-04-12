import flask

app = flask.Flask(__name__)
@app.route('/')

def index():
    return '<h1>Hello world!</h1>'
#app.add_url_rule('/','index',index)

@app.route('/hello/<name>')
def username(name):
 return f"<h2> Hello, {name} </h2>"
if __name__=='__main__':
 app.run(debug=True)