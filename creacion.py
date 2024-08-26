import requests

# Paso 1: Crear un equipo en el microservicio 2
team_url = "http://localhost:5001/teams"
team_data = {
    "name": "Colo Colo",
    "country": "Chile",  # Asegúrate de que el valor sea uno de los definidos en la enumeración Country
    "description": "god chilean club"
}
team_response = requests.post(team_url, json=team_data)

# Imprimir la respuesta del servidor para más detalles
print(team_response.status_code)
print(team_response.text)

try:
    team_response.raise_for_status()
    team_id = team_response.json()["id"]
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"Other error occurred: {err}")

# Paso 2: Crear un jugador en el microservicio 1
player_url = "http://localhost:5000/players"
player_data = {
    "name": "Felipe",
    "age": 24,
    "number": 4,
    "team_id": "some_team_idd",
    "description": "A new player"
}

try:
    # Verificar la conectividad con una solicitud simple
    response = requests.get(player_url)
    response.raise_for_status()
    print("Conexión exitosa al servidor.")

    # Intentar enviar los datos del jugador
    player_response = requests.post(player_url, json=player_data)
    player_response.raise_for_status()
    print("Jugador creado exitosamente:", player_response.json())

except requests.exceptions.ConnectionError as e:
    print(f"Error de conexión: {e}")
except requests.exceptions.HTTPError as e:
    print(f"Error HTTP: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")