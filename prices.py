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

# Debugging: Print the results dictionary to check its structure
print(json.dumps(results, indent=4))

filtered_results = []

if 'shopping_results' in results:
    for item in results['shopping_results']:
        filtered_item = {
            "product_link": item.get("product_link"),
            "link": item.get("link"),
            "price": item.get("price"),
            "title": item.get("title")
        }
        filtered_results.append(filtered_item)
else:
    print("No shopping results found. Error:", results.get('error', 'Unknown error'))

# Save the results to a JSON file
output_file = os.path.join(os.path.dirname(__file__), 'filtered_results.json')
with open(output_file, 'w') as f:
    json.dump(filtered_results, f, indent=4)

print(f"Filtered results saved to {output_file}")