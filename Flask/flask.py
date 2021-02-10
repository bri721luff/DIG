from flask import Flask, render_template, request
app = Flask(__name__)

# @ signifies a decorator

@app.route('/')
def index():
  return render_template('form.html')

if __name__ == '__main__':
	app.run(debug=True)
