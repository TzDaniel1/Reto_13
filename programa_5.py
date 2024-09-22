import requests

api_urls = [
    "https://catfact.ninja/fact",
    "https://api.genderize.io?name=luc",
    "https://official-joke-api.appspot.com/random_joke"
]

def get_json_and_print_pairs(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        json_data = response.json()
        print(f"\nDatos de la API ({api_url}):")
        print(json_data)  
        print("\nPares clave: valor")
        for key, value in json_data.items():
            print(f"{key}: {value}")
    else:
        print(f"Error al conectarse a {api_url}")

for url in api_urls:
    get_json_and_print_pairs(url)