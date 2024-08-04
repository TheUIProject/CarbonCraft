// Assuming your Flask API is running on http://localhost:5000

// Get the form and result elements
const form = document.getElementById('pred_emission');
const result = document.getElementById('emission');

// Add a submit event listener to the form
form.addEventListener('submit', async (event) => {
  event.preventDefault();

  // Get the user input
  const engineSize = document.getElementById('EngineSize').value;
  const cylinders = document.getElementById('Cylinders').value;
  const fuel = document.getElementById('Fuel').value;

  // Send a POST request to the Flask API with the user input
  const response = await fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded', // Match Flask API expectation
    },
    body: new URLSearchParams({
      'Engine Size(L)': engineSize,
      'Cylinders': cylinders,
      'Fuel Consumption Comb (L/100 km)': fuel,
    }),
  });

  // Handle the response
  if (response.ok) {
    const data = await response.json();
    result.textContent = `Prediction: ${data.prediction}`;
  } else {
    result.textContent = 'Error: ' + response.statusText;
  }
});
