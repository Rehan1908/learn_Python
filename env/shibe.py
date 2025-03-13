# demo.py

# Import the requests library
import requests

# Define a variable with the URL of a different API (JSONPlaceholder - a free fake API for testing)
api_url = "https://jsonplaceholder.typicode.com/todos/1"

# Call the API with GET, store the answer in a response variable
try:
  response = requests.get(api_url, timeout=30)
  
  # Get the status code for the response
  print(f"Response status code is: {response.status_code}")
  
  # Check if the request was successful
  response.raise_for_status()
  
  # Get the result as JSON
  response_json = response.json()
except requests.exceptions.RequestException as e:
  print(f"Error connecting to the API: {e}")
  # Provide a fallback response
  response_json = {"title": "Example fallback todo", "completed": False}

# Print the response data
print(response_json)
