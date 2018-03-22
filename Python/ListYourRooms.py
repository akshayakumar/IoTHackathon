# Importing necessary modules
import requests
import json

#Disable warnings
requests.packages.urllib3.disable_warnings()

# Variables

url = "https://api.ciscospark.com/v1"
api_call ="/rooms"
access_token = "Bearer {access-token}" #Replace the {access-token} with your personal access token.

# Header information
headers = {
            "content-type" : "application/json; charset=utf-8",
            "authorization" : access_token,
          }

# Parameter variable. The email belongs to a bot user, but we can use it for our code
param = ""

# Combine URL, API call and parameters variables
url +=api_call+param

response = requests.get(url, headers=headers, verify=False).json()

# Print user's name and email address from respond body.
for item in response["items"]:
    print('Room Name: ' + item['title'])
