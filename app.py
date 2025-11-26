# Import the Flask class from the flask package
from flask import Flask, render_template, request, jsonify

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')

# Define a view function associated with the route
def home():
    return render_template('index.html')

@app.route('/deploy', methods=['POST'])
def deploy():
    # Get data sent from the form
    data = request.get_json()
    github_url = data.get('github_url')

    # For now, just send it back
    return jsonify({
        'status': 'received',
        'message': f'Got your URL: {github_url}'
    })

# Check if the script is run directly
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, port=5000)
    