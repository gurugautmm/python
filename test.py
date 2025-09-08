import requests
import base64

username = "myuser"
password = "mypassword"

# Combine and encode the credentials
credentials = f"{username}:{password}"
encoded_credentials = base64.b64encode(credentials.encode()).decode('utf-8')

# Create the authorization header
headers = {
    "Authorization": f"Basic {encoded_credentials}"
}

# Make the request with the custom header
response = requests.get("https://api.example.com/data", headers=headers)

print(response.status_code)
