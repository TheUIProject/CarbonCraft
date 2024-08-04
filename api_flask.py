from flask import Flask, request, render_template, jsonify
import joblib  # For loading the trained model

app = Flask(__name__,static_folder='static',template_folder='web')
# Load the trained model from a file
ml_model = joblib.load('vemodel.pkl')

# Define the route for the HTML page
@app.route('/')
def index():
    return render_template('cal.html')
print(app.url_map)

# Define the route for the prediction API
@app.route('/predict', methods=['POST'])
def predict():
    try: 
        # Print debug statement
        print("Received request for prediction")

        # Get the input values from the HTML form
        engine_size = float(request.form.get('Engine Size(L)', 0))  # Use parentheses for method call
        cylinders = int(request.form.get('Cylinders', 0))
        fuel = int(request.form.get('Fuel Consumption Comb (L/100 km)', 0))

        # Print input values for debugging
        print(f"Engine Size: {engine_size}, Cylinders: {cylinders}, Fuel: {fuel}")

        # Use the loaded model to make a prediction
        prediction = ml_model.predict([[engine_size, cylinders, fuel]])

        # Return the prediction as JSON
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        # Print any exceptions to the console
        print(f"Error: {e}")
        # Return error message with 400 status code
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
