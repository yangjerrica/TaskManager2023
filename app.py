from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Your Python logic goes here
    message = "Hello from Python!"

    # Render HTML template and pass the message variable
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)