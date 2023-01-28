import requests

# API endpoint URL
url = 'https://safe-transaction-mainnet.safe.global/api/v1/safes/0xBbA4C8eB57DF16c4CfAbe4e9A3Ab697A3e0C65D8/multisig-transactions/'

# Make a GET request to the API
response = requests.get(url)

# Convert the response to JSON
data = response.json()

#print(data['results'])

# Initialize a counter variable
count = 0

# Iterate through each item in the JSON data
for item in data['results']:
    # Check if the field origin contains the string "WalletConnect"
    if 'WalletConnect' in item['origin']:
        # If it does, increment the counter
        count += 1

# Print the final count
print(count) 