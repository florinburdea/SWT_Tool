#Init Python file
#Located in the core source

from flask import Flask

# @ is a decorator - way to wrap a function and modifying it's behaviour
app = Flask(__name__)

@app.route('/')
def index():
	return 'This is the Homepage'


if __name__=="__main__":
	app.run(debug=True)