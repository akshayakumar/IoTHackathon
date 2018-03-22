# Importing necessary modules
import requests
import json

#Disable warnings
requests.packages.urllib3.disable_warnings()

# Variables

url = "https://api.ciscospark.com/v1"
api_call ="/messages"
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

payload = "{\n\"toPersonEmail\": \"{email-id}\",\n\"text\": \"Hello\"\n}" #Replace the {email-id} with your friends email-id.

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
