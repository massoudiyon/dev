from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the calculator function as an API endpoint
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get the equation from the request
        data = request.get_json()
        equation = data.get('equation', '')

        # Evaluate the equation
        result = eval(equation)

        # Return the result as JSON
        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

