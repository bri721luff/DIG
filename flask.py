from flask import Flask, render_template, request
app = Flask(__name__)

# @ signifies a decorator

@app.route('/')
def index():
  return render_template('form.html')

if __name__ == "__main__":
	app.run(debug=true)

@app.route('/dashboard/<username>', methods=['GET', 'POST'])
def dashboard(username):
	if request.method == 'POST':
		return "You are using POST"
	else:
		return "You are probably using GET"

if __name__ == '__main__':
	app.run(debug=True)

@app.route('/confirm')
def confirm():
	return render_template('confirm.html')

if __name__ == '__main__':
	app.run(debug=True)
