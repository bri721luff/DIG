from flask import Flask, render_template, request
app = Flask(__name__)

# @ signifies a decorator

@app.route('/')
def index():
  return render_template('dashboard.html')

@app.route('/validated')
def validated():
  return render_template('Validated.html')

@app.route('/updated')
def updated():
  return render_template('Updated.html')


if __name__ == '__main__':
	app.run(debug=True)
