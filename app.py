from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and the corresponding view function
@app.route('/')
def hello_world():
    # Return a string to display on the webpage
    return 'Hello World!'

# Run the Flask app
if __name__ == '__main__':
    app.run()