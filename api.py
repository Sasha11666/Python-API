# The API request to get the data (breeds) from the cats database

import requests
response = requests.get("https://api.thecatapi.com/v1/breeds")
response.text
