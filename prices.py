from serpapi import GoogleSearch
import json
import os

params = {
  "engine": "google_shopping",
  "q": "burton impact shorts men",
  "device": "desktop",
  "location": "United Kingdom",
  "hl": "en",
  "gl": "uk",
  "api_key": "83dc45d951799e7d27d59d3ef9d7756f4d745f1973d551684c64ea4262d71c3b"
}

search = GoogleSearch(params)
results = search.get_dict()
shopping_results = results["shopping_results"]

# Save the results to a JSON file
file_path = os.path.join(os.path.dirname(__file__), 'shopping_results.json')
with open(file_path, 'w') as json_file:
  json.dump(shopping_results, json_file, indent=4)

print(f"Results saved to {file_path}")