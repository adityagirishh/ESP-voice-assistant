import subprocess
import json

# Your actual API key
api_key = "AIzaSyAnwwXsvyX_kfAnpsmYtZ1ZV00eQtDNyQ0"
with open('output.txt', 'r') as file:
    query = file.read().strip()

# Define the curl command with the API key variable
curl_command = [
    'curl',
    '-H', 'Content-Type: application/json',
    '-d', f'{{"contents":[{{"parts":[{{"text":"{query}"}}]}}]}}',
    '-X', 'POST',
    f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}'
]

# Execute the curl command and capture the output
try:
    result = subprocess.run(curl_command, check=True, capture_output=True, text=True)
    # Parse the JSON response
    response_data = json.loads(result.stdout)
    # Print only the text object
    print(response_data['candidates'][0]['content']['parts'][0]['text'])
except subprocess.CalledProcessError as e:
    print("Error:", e)
