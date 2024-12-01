from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32

# Define a route and the corresponding view function
@app.route('/')
def hello_world():
    # Return a string to display on the webpage
    return f"<h1>Hello World:)</h1>"

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"<h1>Hello {name}!</h1>"


@app.route('/convert/<celsius>')
def convert_temperature(celsius):
    """Convert Celsius to Fahrenheit and display the result."""
    try:
        celsius = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return f"<h1>{celsius}°C is {fahrenheit:.2f}°F</h1>"
    except ValueError:
        return "<h1>Invalid temperature value. Please provide a numeric value.</h1>"

# Run the Flask app
if __name__ == '__main__':
    app.run()
