

import requests

pokemon_name = None
pokemon_height = None
pokemon_type = None
pokemon_habitat = None
temperature = None
weather_code = None

# REQUEST 1: 

POKE_BASE_URL = "https://pokeapi.co/api/v2"

pokemon_name = "pikachu"

try:

    pokemon_response = requests.get(f"{POKE_BASE_URL}/pokemon/{pokemon_name}", timeout=10)

    if pokemon_response.status_code == 200:
        pokemon_data = pokemon_response.json()
        pokemon_name =  pokemon_data["name"]
        pokemon_height = pokemon_data["height"]
        pokemon_type = pokemon_data["types"][0]["type"]["name"]
    else: 
        print("Pokemon Request Failed")

except requests.RequestException:
    print("Pokemon API is unavailable")



# REQUEST 2:

POKE_BASE_URL = "https://pokeapi.co/api/v2"
pokemon_name = "pikachu"

try:
    species_response = requests.get(
        f"{POKE_BASE_URL}/pokemon-species/{pokemon_name}", timeout=10
    )

    if species_response.status_code == 200:
        species_data = species_response.json()
        pokemon_habitat = species_data["habitat"]["name"]
    else: 
        print("Pokemon species request failed")

except requests.RequestException:
    print("Pokemon API is unavailable")



# REQUEST 3: 

WEATHER_BASE_URL = "https://api.open-meteo.com/v1/forecast"

weather_params = {
    "latitude": 34.05,
    "longitude": -118.24,
    "current": "temperature_2m,weather_code",
    "temperature_unit": "fahrenheit"
}

try: 
    weather_response = requests.get(
        WEATHER_BASE_URL,
        params=weather_params,
        timeout=10
    )
    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        temperature = weather_data["current"]["temperature_2m"]
        weather_code = weather_data["current"]["weather_code"]
    else: 
        print("Weather Request Failed")

except requests.RequestException:
    print("Weather API is unavailable")

if temperature is not None:
    if temperature >= 80:
        commentary = f"It's hot in Los Angeles today. {pokemon_name.title()} stay hydrated!"
    else:
        commentary = f"The weather looks cool and breezy for {pokemon_name.title()} today!"


print("\n=== POKEMON OF THE DAY ===")
print(f"Pokemon: {pokemon_name.title()}")
print(f"Type: {pokemon_type.title()}")
print(f"Height: {pokemon_height}")
print(f"Habitat: {pokemon_habitat.title()}")

print("\n=== CURRENT LOS ANGELES WEATHER ===")
print(f"Temperature: {temperature}°F")
print(f"Weather code: {weather_code}")

print("\n=== TODAY'S SUMMARY ===")
print(commentary)