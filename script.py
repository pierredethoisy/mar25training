import requests

# Define your GitGuardian API key - 
API_KEY = "ksdfhjgkejhgekr235346dfdfshtb3254632323432536DFGgdfgdhfdf164535"

# Define the GitGuardian API URL
BASE_URL = 'https://api.gitguardian.com/v1/secrets'
l
# Create headers with your API key for authentication
headers = {
    'Authorization': f'Bearer {API_KEY}'
} ;
def fetch_secrets():
    try:
        # Make a GET request to retrieve the list of secrets
        response = requests.get(BASE_URL, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            secrets_data = response.json()
            # Print the list of secrets
            print(f"Secrets retrieved!: {secrets_data}")
        else:
            print(f"Failed to fetch secrets. Status code: {response.status_code}, Error: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to GitGuardian API: {e}")

# Call the function to fetch secrets
fetch_secrets()
